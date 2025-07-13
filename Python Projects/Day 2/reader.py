import hashlib

with open("testfile.txt", "rb") as f:
    my_file = f.read()

my_hash = hashlib.sha1(my_file)
print("my hash:", my_hash.hexdigest())