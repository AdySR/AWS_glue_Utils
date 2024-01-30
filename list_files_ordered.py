import boto3

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('s3-cal')
files = my_bucket.objects.filter()
files = [obj.key for obj in sorted(files, key=lambda x: x.last_modified, 
    reverse=True)]
