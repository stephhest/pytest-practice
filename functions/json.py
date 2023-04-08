import json

# convert dict to json and return
def convert_dict_to_json(obj):
    return json.dumps(obj)

# convert json to dict and return
def convert_json_to_dict(json_str):
    return json.loads(json_str)

# write to json file
def write_to_json_file(filepath, json_str):
    with open(filepath, 'w') as f:
        f.write(json_str)

# read from json file
def read_from_json_file(filepath):
    with open(filepath, 'r') as f:
        json_str = f.read()
        return json_str
