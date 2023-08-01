import hashlib

ks = "ZjAwZGU0N2JmZWI4MTc1NjJlYWU4YjEzYThmNmVjODljMzRhN2M3OHw5NTgzMjE7OTU4MzIxOzE2OTA5MTQyODE7MDsxNjkwODI3ODgxLjU5MzY7MDt2aWV3Oiosd2lkZ2V0OjE7Ow=="
appToken = "83d346601b197c5c97bb31cd04ec5fa3"

hashString = hashlib.sha256(ks.encode('ascii') + appToken.encode('ascii')).hexdigest()
print(hashString)