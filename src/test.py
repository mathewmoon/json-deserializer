from json import dumps
from collections import UserDict
from json_deserializer import deserialize

class MyDict(UserDict):
    pass
d = MyDict({"foo": "bar"})
try:
    dumps(d)
except Exception as e:
    print(e)

dumps(d, default=deserialize)
