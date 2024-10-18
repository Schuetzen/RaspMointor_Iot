# RaspMointor_Iot

Describe: This script is intended to capture images using a Raspberry Pi and upload them to a Google Cloud Storage bucket at regular intervals.
Object: To upload data periodically from your Raspberry Pi to Google Cloud Storage.
Update_Date: Oct.18 2024

## Necessary

Install Google Cloud SDK and Python Libraries

## Connect with Google Cloud
Google cloud service account is `raspbot`, the key is saved in the folder `/google_cloud_tocken`

* Trasnfer the key to Raspberry Pi using scp

`scp path/google_cloud_tocken/storied-parser-439001-p7-bae26682bb14 pi@raspberry_ip:/home/pi/`

Replace raspberry_ip with your Raspberry Pi’s IP address.

* (Optional) Save the credentials file to a secure location on the Raspberry Pi, like `/home/pi/gcloud_key.json`.

