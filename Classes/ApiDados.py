import requests
from requests.auth import HTTPBasicAuth

class ApiDados:
    def __init__(self):
        self._headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': None
        }
#        self._baselink = 'https://api.jmduque.com.br'

    def AutenticarApi(self):
        try:
            response = requests.post(url = f'{self._baselink}/auth', headers = self._headers, auth = HTTPBasicAuth('login', 'senha'))
            return response.json()
        except Exception as e:
            print(f'Erro ao autenticar a API: {e}\n--------------------------------------\n')

    def EnviarDadosFatura(self, dados_json):
        try:
            token = self.AutenticarApi()
            
            self._headers['Authorization'] = f'Bearer {token["data"]["token"]}'

            response = requests.post(url = f'{self._baselink}/envio', headers = self._headers, data = dados_json)
            print(response.json())
        except Exception as e:
            print(f'Erro ao enviar os dados para a API: {e}\n-------------------------------------------\n')