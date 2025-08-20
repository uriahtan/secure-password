import hashlib

password = "VtO#-3koC=0pcAi"
sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
print(sha1_hash)