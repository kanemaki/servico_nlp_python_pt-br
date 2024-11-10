FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de requisitos
COPY ./requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt; \
    python -m nltk.downloader punkt wordnet; \
    python -m spacy download pt_core_news_sm; \
    python -m nltk.downloader rslp; \
    mkdir -p /app/utils

# Copia o código da aplicação
COPY ./* /app/
COPY ./utils/* /app/utils/

# Expõe a porta
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
