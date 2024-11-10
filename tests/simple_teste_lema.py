from app.utils import verifica_e_baixa_arquivos
import nltk

from nltk.tokenize import PunktTokenizer


def main():

    verifica_e_baixa_arquivos("tokenizers","punkt.zip")
    verifica_e_baixa_arquivos("tokenizers","punkt_tab.zip")
    verifica_e_baixa_arquivos("stemmers","rslp.zip")

    #path_rslp = Path(os.path.join(str_base,"stemmers","rslp.zip"))

    #if not path_punkt.exists():
    #    nltk.download("punkt")
    #else:
    #    print("Punkt already downloaded.")

    #if not path_rslp.exists():
    #    nltk.download("rslp")
    #else:
    #    print("Rslp already downloaded.")

    # Initialize Python porter stemmer
    stok = PunktTokenizer("portuguese")

    arr = stok.tokenize("Hoje eu fui a escola. Lá, o que eu mais \nqueria é voltar para a casa. Assim como \na minha Mãe falou: Um dia vc vai precisar disso.")

    print(arr)
    for i in arr:
        print(f"Frase: {i}")
        print("----------------------------------------")

    stemmer = nltk.stem.RSLPStemmer()

    # Example inflections to reduce
    example_words = ["programa", "programando", "programador", "programas", "programado"]

    # Perform stemming
    print("{0:20}{1:20}".format("--Word--", "--Stem--"))
    for word in example_words:
        print("{0:20}{1:20}".format(word, stemmer.stem(word)))


if __name__ == "__main__":
    main()
