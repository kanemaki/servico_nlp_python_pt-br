import nltk
import spacy

lemmatizer = nltk.stem.RSLPStemmer()
stemmer = nltk.stem.RSLPStemmer()

# Tem que executar o módulo para fazer download durante a instalação da lib
#  python -m spacy download pt_core_news_sm
nlp = spacy.load('pt_core_news_sm')


def lemmatize_sentence(sentence: str) -> str:
    words = nltk.word_tokenize(sentence, language='portuguese')
    # Processamento com spaCy
    doc = nlp(' '.join(words))
    lemmatized_words = [word.lemma_ for word in doc]
    return ' '.join(lemmatized_words)


def stem_sentence(sentence: str) -> str:
    words = nltk.word_tokenize(sentence, language='portuguese')
    stemmed_words = [stemmer.stem(word) for word in words]
    return ' '.join(stemmed_words)

