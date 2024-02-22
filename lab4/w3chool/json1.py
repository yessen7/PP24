# JSON is a syntax for storing and exchanging data
# JSON is text, written with JavaScript object notation

import json

# Convert from JSON to Python

# some json
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary
print(y["age"])
