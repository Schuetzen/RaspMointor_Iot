import os
import time
from datetime import datetime
from google.cloud import storage
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import service_account
import subprocess

# command_line = 'gcloud auth application-default set-quota-project test-image-mwc'
# subprocess.run(command_line, shell=True, check=True)

bucket_name = 'rasp_monitor_iot'
folder_path = 'test_images'

# Load service account credentials from JSON file
credentials_path = "/home/pi/gcloud_key.json"
credentials = service_account.Credentials.from_service_account_file(credentials_path)


""" credentials = Credentials.from_authorized_user_info({
	"client_id": "764086051850-6qr4p6gpi6hn506pt8ejuq83di341hur.apps.googleusercontent.com",
	"client_secret": "d-FL95Q19q7MQmFpd7hHD0Ty",
	"refresh_token": "1//041PwNVVOxh0fCgYIARAAGAQSNwF-L9Ir2BvOizAL4GMU_X5yL7EneYMxqrMoJ8Zk9QYTTvqUZ2PnXXC8ZGj0f2dZztGHp68oPmw",
	"token_url": "http://oauth2.googleapis.com/token"
		}) """

client = storage.Client(credentials=credentials)
bucket = client.bucket(bucket_name)

def capture_and_upload():
	timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
	image_path = f"/home/pi/{timestamp}.jpg"
	
	# run command line to capture an image
	capture_command = f'rpicam-still --output {image_path}'
	subprocess.run(capture_command, shell=True, check=True)
	
	# push the time stamped image to Google cloud	
	blob = bucket.blob(f"{folder_path}/{timestamp}.jpg")
	blob.upload_from_filename(image_path)	
	print(f"Uploaded {image_path} to {folder_path}/{timestamp}.jpg")
		
	# push 'new_img.jpg' to Google cloud
	# blob = bucket.blob(f"{folder_path}/new_image.jpg")
	# blob.upload_from_filename(image_path)
	# print("image updated on cloud!")
	
	os.remove(image_path)
	
try:
	while True:
		capture_and_upload()
		time.sleep(300)
		
except KeyboardInterrupt:
	print("Program stopped by user.")	
	
