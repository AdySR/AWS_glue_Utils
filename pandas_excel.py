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

"""
--additional-python-modules	openpyxl """


import pandas as pd

df = pd.read_excel(r's3://s3-ohio/unzipped/employees.xlsx', sheet_name='employees')

print(df)

job.commit()
