# Cire um dicionário para armazenar informações de um livro,
# incluindo título, auto e ano de publicação. Imprima cada informação.

from typing import Dict, Any 

livro: Dict[str, Any] = {
"Título": "O Óbvio que Iguinoramos",
"Autor": "Jacob Petry",
"Ano": 2005
}

list_de_elementos: list = livro.items()
for elemento in list_de_elementos:
    print(elemento)