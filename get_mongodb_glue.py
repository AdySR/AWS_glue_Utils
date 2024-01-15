--additional-python-modules  :  pymongo


import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

from pymongo import MongoClient
user ='admin'
password = 'admin'

mongo_uri = f"mongodb+srv://{(user)}:{(password)}@poccluster.sjsfbns.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongo_uri)
db = client["centric_poc_0"]
collection = db["dummy_orders"]

for x in collection.find({}):
    print(x)

job.commit()
