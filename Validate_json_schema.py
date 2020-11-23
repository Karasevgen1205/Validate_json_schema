import json
import jsonschema
import os


directory_schema = 'D:/Python 3.8.3/Project/task_folder/schema'
files_schema = os.listdir(directory_schema)
full_files_schema = []
for a in files_schema:
    full_name_schema = directory_schema + "/" + a
    full_files_schema.append(full_name_schema)

    
directory_json = 'D:/Python 3.8.3/Project/task_folder/event'
files_json = os.listdir(directory_json)
full_files_json = []
for b in files_json:
    full_name_json = directory_json + "/" + b
    full_files_json.append(full_name_json)

    
def get_schema(lo):    
    with open(lo, 'r') as file:
        schema = json.load(file)
    return schema


def validate_json(json_data,net):
    with open(json_data, 'r') as f:
        json_load = json.load(f)
    execute_api_schema = get_schema(net)

    try:
        validate(instance=json_load, schema=execute_api_schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is InValid"
        return False, err

    message = "Given JSON data is Valid"
    return True, message


# Convert json to python object.
for i in full_files_schema:
    
    for j in full_files_json:
        print(i)
        print(j)
        msg = validate_json(j,i)
        print(msg)