from pymongo import MongoClient
from module_flatten_json import flatten_json
import json
import pandas as pd
from datetime import datetime

user ='admin'
password = 'admin'
output =r'C:\apps\development\py_proj\fake_data\output'

mongo_uri = f"mongodb+srv://{(user)}:{(password)}@poccluster.sjsfbns.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongo_uri)
db = client["centric_poc_0"]
collection = db["dummy_orders"]

json_document_list =[]

for json_data in collection.find({}).limit(5):
    print(type(json_data) , '---- ',json_data)
    flatten_json_data = flatten_json(json_data)
    # print(type(flatten_json_data),' - ',flatten_json_data, '\n')
    file_name=flatten_json_data["_id"]
    sufx = datetime.utcnow().strftime("D_%Y_%m_%d_T_%H_%M_%S")
    # df_json = pd.DataFrame(flatten_json_data.items() , columns= ['key','value'])
    # df_json = df_json.set_index('key').T

    df_json = pd.DataFrame(flatten_json_data , ['key'])
    df_json.to_csv(rf'C:\apps\development\py_proj\fake_data\output\{sufx}_{file_name}.csv')

