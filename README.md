# vehicles_nork

# Como Usar:
  - Clonar o repositório
  - criar virtualenv e ativar
  - pip install -r requirements.txt
  - export FLASK_APP=run
  - flask run


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

## Referências:
1 - Clean Architecture Python: https://www.youtube.com/playlist?list=PLAgbpJQADBGJmTxeRZKWvdJAoJj8_x3si
2 - https://www.sqlalchemy.org/
3 - https://flask.palletsprojects.com/en/2.2.x/
