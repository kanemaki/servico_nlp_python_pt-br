from fastapi import FastAPI, Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import socket
import datetime
from nltk.tokenize import PunktTokenizer
from utils.baixa_arquivos import verifica_e_baixa_arquivos
import re

# Certifique-se de que os recursos necessários do NLTK estão instalados

from utils.nlp import lemmatize_sentence, stem_sentence

app = FastAPI()
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
verifica_e_baixa_arquivos("tokenizers", "punkt.zip")
verifica_e_baixa_arquivos("tokenizers", "punkt_tab.zip")
verifica_e_baixa_arquivos("stemmers", "rslp.zip")


class Sentence(BaseModel):
    text: str


@app.get("/")
def read_root():
    return {
        "message": "Hello, World!",
        "date_time": datetime.datetime.utcnow().__str__(),
        "hostname": socket.gethostname()}


@app.post("/token/copia={envia_copia}")
def token(sentence: Sentence, envia_copia: bool):
    # Eu envio o sentença completa (como uma página no caso)
    # usando o formato "{ "text": "texto a ser tokenizado" }"
    # como retorno teremos 3 campos de retorno:
    # "original (texto)
    # "tokens" (array de string)
    # count (int quantidade de tokens)


    if is_not_palavras(sentence.text):
        return {"estado": "isso não tem palavras comuns, ou tem somente números"}

    stok = PunktTokenizer("portuguese")
    arr = stok.tokenize(sentence.text)
    if envia_copia:
        return {
            "original": sentence.text,
            "tokens": arr,
            "count": len(arr),
            "estado": "ok"
        }
    else:
        return {"tokens": arr, "count": len(arr), "estado": "ok"}


def is_not_palavras(text):
    # Divide a string por espaços, tabulações e quebras de linha
    palavras = re.split(r'[\s\t\n.]+', text)
    #palavras = [palavra for palavra in text.split()]

    total_numeros = sum(c.isdigit() for c in text)
    total_letras = sum(c.isalpha() for c in text)
    total_letras_com_numeros = total_numeros + total_letras
    if total_letras_com_numeros  == 0:
        return True  # Não há nenhuma palavra

    # Conta quantas palavras têm mais de 60 caracteres
    palavras_longas = [palavra for palavra in palavras if len(palavra) > 60]

    # Conta palavras curtas
    palavras_curtas = [palavra for palavra in palavras if len(palavra) <= 2]

    # Verifica se não há nenhuma palavra com mais de 60 caracteres
    if len(palavras_longas) == 0 and len(palavras_curtas) == 0:
        return True  # Todas as palavras são curtas ou não tem palavras com mais de 60 caracteres

    # Verifica se não há nenhuma palavra com mais de 60 caracteres
    if len(palavras_longas) == 0:
        return False  # Todas as palavras são curtas

    # Verifica se não há nenhuma palavra curta

    # Calcula a porcentagem de palavras com mais de 60 caracteres
    if len(palavras) == 0:
        return False  # Evita divisão por zero se não houver palavras

    porcentagem_longa = (len(palavras_longas) / len(palavras)) * 100
    porcentagem_curta = (len(palavras_curtas) / len(palavras)) * 100
    porcentagem_numeros = (total_numeros / total_letras_com_numeros) * 100
    # Verifica se mais de 80% das palavras curtas ou longas
    ## Quaisquer um dos casos pode ser ruido.
    return (porcentagem_longa > 80
            or porcentagem_curta > 80
            or porcentagem_numeros > 80)


@app.post("/lematize/copia={envia_copia}")
def lemmatize(sentence: Sentence, envia_copia: bool):
    original_text = sentence.text

    if is_not_palavras(sentence.text):
        return {"estado": "isso não tem palavras comuns, ou não tem palavras"}

    lemmatized_text = lemmatize_sentence(original_text)
    if envia_copia:
        return {"original": original_text, "lematizado": lemmatized_text, "estado": "ok"}
    else:
        return {"lematizado": lemmatized_text, "estado": "ok"}


# Serviço 3: Radicalização
@app.post("/radical/copia={envia_copia}")
def stem(sentence: Sentence, envia_copia: bool):

    if is_not_palavras(sentence.text):
        return {"estado": "isso não tem palavras comuns"}

    original_text = sentence.text
    stemmed_text = stem_sentence(original_text)

    if envia_copia:
        return {"original": original_text, "radical": stemmed_text, "estado": "ok"}
    else:
        return {"radical": stemmed_text, "estado": "ok"}
