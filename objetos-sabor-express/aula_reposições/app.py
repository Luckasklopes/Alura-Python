import requests
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)

print(response)

if response.status_code == 200:
    dados_json = response.json() #cria o arquivo resposta json
    dados_restaurante = {} #dicionario que vai conter os dados
    for item in dados_json: #para cada item no arquivo resposta
        nome_do_restaurante = item["Company"] #o nome do restaurante é o dado company
        if nome_do_restaurante not in dados_restaurante: #se o nome ja existir
            dados_restaurante[nome_do_restaurante] = []#cria uma lista para cada restaurante diferente
        
        dados_restaurante[nome_do_restaurante].append({ #incrementa na lista o nome do restaurante
            "item": item["Item"],
            "price": item["price"],
            "description": item["description"]
        })


else:
    print(f"o erro foi: {response.status_code}") #imprime qualquer codigo que nao o de sucesso

for nome_do_restaurante, dados in dados_restaurante.items(): #para cada dado em uma lista de dados de um restaurante
    nome_do_arquivo = f"{nome_do_restaurante}.json" #cria uma variavel .json com o nome do restaurante
    with open(nome_do_arquivo, "w") as arquivo_restaurante: #abre um arquivo com permissoes de escrita, com o nome do restaurante
        json.dump(dados, arquivo_restaurante, indent=4) #coloca no arquivo os dados do restaurante