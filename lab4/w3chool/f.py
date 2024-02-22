import json

# Convert from Python to JSON

# a Python object (dict)
x = {
    "name": "Richard",
    "age": 50,
    "city": "New York"
}

# convert into JSON
y = json.dumps(x)

# the result is a JSON string:
print(y)

q = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(q, indent=4, sort_keys=True))  # sort the keys
