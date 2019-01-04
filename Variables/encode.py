## enconding schemes
from base64 import encode

str_1 = "nirmal"

print(str_1.encode("UTF-8"))
print(str_1.encode("ASCII"))

en_str = str_1.encode("UTF-8")
print(en_str.decode("UTF-8"))