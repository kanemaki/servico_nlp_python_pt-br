from datetime import datetime, timedelta

from authlib.jose import jwt

import json

# Chave secreta para codificação do token JWT
SECRET_KEY = "ds;c.c s;fdksfko  &(kfd;dl;k EEs;s.,s sSps´.rpgmb;weptnb  lkdsc.sd;"
ALGORITHM = "HS256"


# Função para autenticar o usuário
def authenticate_user(username: str, password: str) -> bool:
    # Para simplificação, usamos credenciais fixas
    return username == "admin" and password == "admin"


# Função para criar um token de acesso
# Função para criar um token de acesso

str_format_date_time = "__%a %b %d %H:%M:%S %Y__"
def create_access_token(username: str, expires: int = 30) -> str:
    expire = (datetime.utcnow() + timedelta(minutes=expires)).strftime(str_format_date_time)
    payload = {"sub": username, "exp": expire}
    print("---------------------------")
    print("UTC NOW = " + datetime.utcnow().strftime(str_format_date_time))
    print("Expire = " + expire)
    print("Payload = ", payload)
    dt = datetime.strptime(expire, str_format_date_time)
    print("Data Expiração:", dt)
    print(type(payload))
    print("---------------------------")
    payload_str = json.dumps(payload)
    ## payload_str = json.dumps(payload, indent=4)

    ## Outras alternativas: HS384 ou HS512, (deve mudar o tamanho do chave)
    header = {'alg': 'HS256'}
    encoded_jwt = jwt.encode(header, payload_str, SECRET_KEY, check=False)
    # Converte o token de bytes para uma string usando decode
    return encoded_jwt.decode("utf-8") if isinstance(encoded_jwt, bytes) else encoded_jwt
    ##return encoded_jwt


def valid_access_token(token: str, user: str) -> dict:
    ## Outras alternativas: HS384 ou HS512, (deve mudar o tamanho do chave)
    header = {'alg': 'HS256'}
    payload_str = jwt.decode(token, SECRET_KEY)
    payload_map = json.loads(payload_str)

    if payload_map["sub"] != user:
        raise ValueError("Usuário não confere")

    if datetime.utcnow() > int(payload_map["exp"]):
        raise ValueError("Token expirado")

    return payload_map


token = create_access_token("admin")
print("Token de Acesso:", token)
print(valid_access_token(token, "admin"))

# Converte o token de bytes para uma string usando decode
##return encoded_jwt.decode("utf-8") if isinstance(encoded_jwt, bytes) else encoded_jwt
data_string = valid_access_token(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTczMTIwODgyMn0.moB31a2G6rK2UQ_T0ZAPYL6FLRD5M_3pX71LHqFq9Dk",
    "admin")

import ast

print(data_string)
# String que representa um dicionário
# data_string = "{'sub': 'admin', 'exp': 1731208822}"
# data_string = "{'sub': 'admin', 'exp': 1731208822}"
# Converte a string para um dicionário usando eval
data_dict = eval(data_string)
print(data_string)
# Converte a string em um dicionário
data_dict = ast.literal_eval(data_string)

print("Estrutura de mapa (dict):", data_dict)
print("Tipo:", type(data_dict))
print("User:", data_dict["sub"])
