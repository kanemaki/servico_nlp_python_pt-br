from fastapi import FastAPI
from pydantic import BaseModel
import socket
import datetime
from nltk.tokenize import PunktTokenizer
from utils.baixa_arquivos import verifica_e_baixa_arquivos
import re
from utils.nlp import lemmatize_sentence, stem_sentence

# Recursos necessários do NLTK
verifica_e_baixa_arquivos("tokenizers", "punkt.zip")
verifica_e_baixa_arquivos("tokenizers", "punkt_tab.zip")
verifica_e_baixa_arquivos("stemmers", "rslp.zip")

app = FastAPI()

class Sentence(BaseModel):
    text: str

# Função auxiliar genérica para processar texto
def process_text(sentence: str, processor_function, envia_copia: bool, process_name: str):
    if is_not_palavras(sentence):
        return {"estado": f"Texto inválido para processamento: {process_name}"}
    
    processed_text = processor_function(sentence)
    if envia_copia:
        return {"original": sentence, process_name: processed_text, "estado": "ok"}
    else:
        return {process_name: processed_text, "estado": "ok"}

# Função auxiliar para verificar se o texto contém palavras comuns
def is_not_palavras(text):
    palavras = re.split(r'[\s\t\n.]+', text)
    total_numeros = sum(c.isdigit() for c in text)
    total_letras = sum(c.isalpha() for c in text)
    total_letras_com_numeros = total_numeros + total_letras

    if total_letras_com_numeros == 0:
        return True  # Não há palavras

    palavras_longas = [palavra for palavra in palavras if len(palavra) > 60]
    palavras_curtas = [palavra for palavra in palavras if len(palavra) <= 2]

    if len(palavras) == 0:
        return False  # Evita divisão por zero

    porcentagem_longa = (len(palavras_longas) / len(palavras)) * 100
    porcentagem_curta = (len(palavras_curtas) / len(palavras)) * 100
    porcentagem_numeros = (total_numeros / total_letras_com_numeros) * 100

    return (porcentagem_longa > 80 or porcentagem_curta > 80 or porcentagem_numeros > 80)

@app.get("/")
def read_root():
    return {
        "message": "Hello, World!",
        "date_time": datetime.datetime.utcnow().__str__(),
        "hostname": socket.gethostname()
    }

@app.post("/token/copia={envia_copia}")
def token(sentence: Sentence, envia_copia: bool):
    def tokenize_text(text):
        stok = PunktTokenizer("portuguese")
        return stok.tokenize(text)
    return process_text(sentence.text, tokenize_text, envia_copia, "tokens")

@app.post("/lematize/copia={envia_copia}")
def lemmatize(sentence: Sentence, envia_copia: bool):
    return process_text(sentence.text, lemmatize_sentence, envia_copia, "lematizado")

@app.post("/radical/copia={envia_copia}")
def stem(sentence: Sentence, envia_copia: bool):
    return process_text(sentence.text, stem_sentence, envia_copia, "radical")
