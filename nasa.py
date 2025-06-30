import requests

def parametro(data, api_key):
    par = {
        'date' : data,
        'api_key': api_key
    }

    return par

url ='https://api.nasa.gov/planetary/apod?'
api ='io8DE2I2EuJf64OkLcXHp4DWTjA7eSlYNVMsFp0A'
data = input("formato yyyy-mm-dd")
param = parametro(data, api)

response = requests.get(url, params=param) 

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Converte a resposta para JSON
    data = response.json()
    print(data)
else:
    print(f"Erro na requisição: {response.status_code}")
    print(response.text)  # Mostra a mensagem de erro da API
