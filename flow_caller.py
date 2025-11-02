import requests
import os

# Alterar para a sua chave de API
api_key = "sk-Eqj7t6vKap9G9BWUNggVyiIHQMLZslF-RdNvBbwXkeY"
# Alterar para o ID do fluxo criado no Langflow
url = "http://localhost:7860/api/v1/run/205fcaf2-61e4-4aea-ab4e-ea2c87e99308"

payload = {
    "output_type": "text",
    "input_type": "text",
    "input_value": "O que é outorga onerosa?"
}

headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key
}

try:
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status() 
    response_data = response.json()
    output = response_data.get("outputs")[0]["outputs"][0]["results"]["text"]["data"]["text"]
    print(output)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")