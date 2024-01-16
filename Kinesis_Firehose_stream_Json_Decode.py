import json

decoder = json.JSONDecoder()
file =r'C:\apps\development\py_proj\fake_data\file'
with open(file, 'r') as content_file:

    content = content_file.read()

    content_length = len(content)
    decode_index = 0

    while decode_index < content_length:
        try:
            obj, decode_index = decoder.raw_decode(content, decode_index)
            print("File index:", decode_index)
            print(obj)
            print(type(obj))
        except:
            print("JSONDecodeError:")
            # Scan forward and keep trying to decode
            decode_index += 1
