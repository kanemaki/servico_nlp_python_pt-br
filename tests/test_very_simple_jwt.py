from authlib.jose import jwt

# Chave secreta para assinar o token
secret = '324234234ecredfsi0987)oiASKSsoidfjsoLIJidfjsvcl(*&vl,z.mxcvlijwemrwefo'

# Dados a serem incluídos no token
header = {'alg': 'HS256'}
payload = {'user_id': 123, 'role': 'admin'}

# Gerar o token JWT
token = jwt.encode(header, payload, secret)

print(token)

untoken = jwt.decode(token, secret)
print(untoken)
print(payload)