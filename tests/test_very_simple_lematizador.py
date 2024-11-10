import nltk
nltk.download('punkt')

import spacy
# Rodar :: python -m spacy download pt_core_news_sm
nlp = spacy.load('pt_core_news_sm')

def lematizar_texto(texto):
    # Tokenização usando NLTK
    palavras = nltk.word_tokenize(texto, language='portuguese')

    # Processamento com spaCy
    doc = nlp(' '.join(palavras))

    # Extração das lemmas
    lemmas = [token.lemma_ for token in doc]

    return ' '.join(lemmas)

if __name__ == "__main__":
    texto = "Os meninos estão correndo no parque."
    print("Texto original:", texto)
    texto_lematizado = lematizar_texto(texto)
    print("Texto lematizado:", texto_lematizado)