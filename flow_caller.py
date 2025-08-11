import requests
import os

# Alterar para a sua chave de API
api_key = "sk-kFcxmX6Kq-KFMr2En_uRdN3wzQuu2Ted3SOmbysE43c"
# Alterar para o ID do fluxo criado no Langflow
url = "http://localhost:7860/api/v1/run/128d0325-0fa5-4366-974d-fff34a00f144"

payload = {
    "output_type": "text",
    "input_type": "text",
    "input_value": "faça um estudo de viabilidade para um terreno na zona zeu com 1300m2, 15000 valor de venda, 2000 valor de outorga, na rua osvaldo arannha"
}

headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key
}

try:
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status() 

    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")