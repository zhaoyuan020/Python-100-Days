import hashlib
filepath = r"C:/Users/zhaoy/Downloads/wechatbot-v1.1.3.1-windows-amd64.zip"



f = open(filepath, 'rb')
md5obj = hashlib.md5()
md5obj.update(f.read())
hash = md5obj.hexdigest()
f.close()
print(str(hash).lower())
