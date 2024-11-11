from fastapi import FastAPI, Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import socket
import datetime
from nltk.tokenize import PunktTokenizer
from utils.baixa_arquivos import verifica_e_baixa_arquivos

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
def token(sentence: Sentence, envia_copia : bool):
    # Eu envio o sentença completa (como uma página no caso)
    # usando o formato "{ "text": "texto a ser tokenizado" }"
    # como retorno teremos 3 campos de retorno:
    # "original (texto)
    # "tokens" (array de string)
    # count (int quantidade de tokens)
    stok = PunktTokenizer("portuguese")
    arr = stok.tokenize(sentence.text)
    if envia_copia:
        return {
            "original": sentence.text,
            "tokens": arr,
            "count": len(arr)
        }
    else:
        return {"tokens": arr, "count": len(arr)}


@app.post("/lematize/copia={envia_copia}")
def lemmatize(sentence: Sentence, envia_copia : bool):
    original_text = sentence.text
    lemmatized_text = lemmatize_sentence(original_text)
    if envia_copia:
        return {"original": original_text, "lematizado": lemmatized_text}
    else:
        return {"lematizado": lemmatized_text}


# Serviço 3: Radicalização
@app.post("/radical/copia={envia_copia}")
def stem(sentence: Sentence, envia_copia: bool):
    original_text = sentence.text
    stemmed_text = stem_sentence(original_text)
    if envia_copia:
        return {"original": original_text, "radical": stemmed_text}
    else:
        return {"radical": stemmed_text}
