from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/api/hello")
def hello_world():
    """
    Endpoint que exibe uma mensagem incrivel no mundo da programação"
    """
    return {"Hello":"World"}

@app.get("/api/restaurantes/")
def get_restaurantes(restaurante: str = Query(None)):
    """
    Endpoint para ver os cardapios dos restaurantes
    """
    
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        dados_json = response.json() #cria o arquivo resposta json
        dados_restaurante = [] #dicionario que vai conter os dados
        if restaurante is None: #caso o restaurante esteja vazio
            return {"Dados":dados_json}
        
        for item in dados_json: #para cada item no arquivo resposta
            if item["Company"] == restaurante:
                dados_restaurante.append({ #incrementa na lista o nome do restaurante
                    "item": item["Item"],
                    "price": item["price"],
                    "description": item["description"]
                })
        return {"Restaurante": restaurante, "Cardapio": dados_restaurante}
    else:
        return {"Erro":f"{response.status_code} - {response.text}"}