import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAI437F2EHPUGKRDMA'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'koilos-static-files'

print('Ini')
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)


print ("1")
data = open('bitmoji.png', 'rb')
s3.Bucket(BUCKET_NAME).put_object(Key='other/path/my-image-test1.png', Body=data, ACL='public-read')

print ("2")
data = open('bitmoji.png', 'rb')
s3.Bucket(BUCKET_NAME).put_object(Key='other/path/my-image-test2.png', Body=data, ACL='public-read')

print ("3")
data = open('bitmoji.png', 'rb')
s3.Bucket(BUCKET_NAME).put_object(Key='other/path/my-image-test3.png', Body=data, ACL='public-read')

print ("Done")
