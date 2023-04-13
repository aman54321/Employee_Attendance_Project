from django.test import TestCase

# Create your tests here.
import json

data = {
    'name': "Aman",
    'age': 23,
}

print(json.dumps(data))
x = json.dumps(data)
print(type(x))

print(json.loads(x))

y = json.loads(x)
print(type(y))