import hashlib

ks = ''
appToken = '83d346601b197c5c97bb31cd04ec5fa3'

hashString = hashlib.sha256(ks.encode('ascii') + appToken.encode('ascii')).hexdigest()
print(hashString)