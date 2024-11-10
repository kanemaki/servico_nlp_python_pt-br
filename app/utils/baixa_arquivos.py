from pathlib import Path
import nltk
import os

def verifica_e_baixa_arquivos(str_dir, str_file):
    str_base = os.path.join(Path.home(),"nltk_data")
    path_download = Path(os.path.join(str_base,str_dir,str_file))

    if not path_download.exists():
        nltk.download(str_file.replace(".zip",""))
    else:
        print(f"{str_file} already downloaded.")