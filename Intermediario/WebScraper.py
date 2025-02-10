import requests
from bs4 import BeautifulSoup

url = "https://www.uol.com.br"

response = requests.get(url)

if response.status_code == 200:
    print("Página carregada com sucesso!")

    soup = BeautifulSoup(response.text, 'html.parser')

    titulos = soup.find_all('h3', class_='title__element headlineMain__title')  

    print("Títulos das notícias:")
    for i, titulo in enumerate(titulos, 1):
        print(f"{i}. {titulo.get_text()}")
else:
    print(f"Erro ao acessar o site: {response.status_code}")
