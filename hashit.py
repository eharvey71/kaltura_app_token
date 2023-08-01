import hashlib

ks = ''
appToken = ''

hashString = hashlib.sha256(ks.encode('ascii') + appToken.encode('ascii')).hexdigest()
print(hashString)