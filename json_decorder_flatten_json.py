from pymongo import MongoClient
from module_flatten_json import flatten_json
import json
from datetime import datetime
import pandas as pd


decoder = json.JSONDecoder()
file =r'C:\apps\development\py_proj\fake_data\file'
with open(file, 'r') as content_file:

    content = content_file.read()

    content_length = len(content)
    decode_index = 0

    while decode_index < content_length:
        try:
            json_data, decode_index = decoder.raw_decode(content, decode_index)
            flatten_json_data = flatten_json(json_data)
            file_name=flatten_json_data["id"].replace("-","_")
            sufx = datetime.utcnow().strftime("%Y_%m_%d__%H_%M_%S")
            df_json = pd.DataFrame(flatten_json_data , ['key'])
            df_json.to_csv(rf'C:\apps\development\py_proj\fake_data\output\{sufx}_{file_name}.csv')
            # 
        except:
            print("JSONDecodeError:")
            # Scan forward and keep trying to decode
            decode_index += 1
