# vehicles_nork

# Como Usar:
1 - Clonar o repositório
2 - criar virtualenv e ativar
3 - pip install -r requirements.txt


## Rota: Criar usuário.

{
	"name": "Gabriel",
	"password": "123456"
}


## Rota: Cadastrar Veículo (Até 3 por usuário).
{
	"model": "sedan",
	"color": "yellow",
	"user_information": {
		"user_id": 1
	}
}

Referências:
Clean Architecture Python: https://www.youtube.com/playlist?list=PLAgbpJQADBGJmTxeRZKWvdJAoJj8_x3si
https://www.sqlalchemy.org/
https://flask.palletsprojects.com/en/2.2.x/