import json

# a Python object (dict):
dictionary = {
    "name": "Ray",
    "age": 23,
    "city": "New York"
}

# convert into JSON:
# output = '{ "name": "Ray", "age": 23, "city": "New York"}'
jsonString = json.dumps(dictionary)
print('jsonString:', jsonString, type(jsonString))

# parse jsonString to dictionary:
parsedJSON = json.loads(jsonString)
print('parsedJSON:',  parsedJSON, type(parsedJSON))

# the result is a dictionary:
print('name =', parsedJSON["name"])  # output = Ray
print('age =', parsedJSON["age"])  # output = 23

'''
We have created dictionary(name, age, city) and convert it to JSON format
with `json.dumps` function.
Then parse `jsonString` to Python dictionary
with `json.loads`.
'''
