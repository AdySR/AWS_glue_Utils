import boto3
 
def list_files_in_folder(bucket_name, folder_name):
    # Create a Boto3 client for S3
    s3_client = boto3.client('s3')
 
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)
 
 
    if 'Contents' in response:
    
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print("Folder is empty.")



bucket_name = bucket
folder_name = 'zipped/'
list_files_in_folder(bucket_name, folder_name)

"""
Use this list to re occur in below pasted  function.
"""


import boto3
import zipfile
import io
from contextlib import closing

s3 = boto3.client("s3")
bucket = "s3-ohio"
prefix = 'zipped/employee_2.zip'
unzip_prefix = "unzipped/"


s3 = boto3.client('s3')
s3r = boto3.resource('s3')

obj = s3r.Object(
    bucket_name=bucket, key = prefix
)

buffer = io.BytesIO(obj.get()["Body"].read())
z = zipfile.ZipFile(buffer)
list = z.namelist()
for filerr in list:
    y=z.open(filerr)
    arcname = key + filerr
    x = io.BytesIO(y.read())
    arcname = key + filerr

    # print(f'{bucket}/{unzip_prefix}{filerr}')
    s3.upload_fileobj(x, bucket, f'{unzip_prefix}{filerr}')
    
    y.close()
# print(list)
