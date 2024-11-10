import json


def main():

    arr = [10, 20, 30]
    dictionary = {"nome":"maria", "idade": 20}

    # Converte para Json
    json_arr = json.dumps(arr)
    json_dict = json.dumps(dictionary)

    print(f"""
    ----------------------------
    Array em Json: "{json_arr}"
    
    Dicionário em Json: "{json_dict}"
    ----------------------------
    Tipos : "{type(json_arr)}" e "{type(json_dict)}"
    """)

    arr_reverse = json.JSONDecoder().decode(json_arr)
    print(f"""
    Array reverso: {arr_reverse}
    """)

    dict_reverse = json.JSONDecoder().decode(json_dict)
    print(f"""
    Dicionário reverso: {dict_reverse}
    """)

if __name__ == "__main__":
    main()