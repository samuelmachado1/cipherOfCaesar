import json, requests
import hashlib

response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=YouToken')

def get_characters():
    list = []
    for id_ in range(ord("a"), ord("z") + 1):
        caractere = chr(id_)
        list.append(caractere)
    
    return list

def decript(text, chave):
    text = text.lower()

    list = get_characters()
    
    new_text = ""

    for caractere in text:
        if caractere == " ":
            new_character = " "
        elif caractere == ".":
            new_character = "."
        else:
            posicao = list.index(caractere)
            posicao = posicao - chave

            new_character = list[posicao]
        new_text = new_text + new_character
        
    return new_text

with open('answer.json', 'r', encoding='utf8') as file:
    data=json.loads(file.read())
    
mensagem_cod = data['cifrado']
key = data['numero_casas']

decript(mensagem_cod, key)
new = decript(mensagem_cod, key)
abstract = hashlib.sha1(new.encode())
data['decifrado'] = new
data['resumo_criptografico'] = abstract.hexdigest()

with open('answer.json', 'w', encoding='utf8') as file:
    json.dump(data, file)
