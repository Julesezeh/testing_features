import json

users = {'James': {'age': 25, 'height': 1.98},
         "Harlem": {'age': 20, 'height': 1.80}}

# Testing dumps
json_users = json.dumps(users)
print(type(json_users))
print(json_users)

# Testing loads

reverted_dict = json.loads(json_users)
print(type(reverted_dict))
print(reverted_dict)
