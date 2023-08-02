# flask_rest_api_usuarios

<p align="center">
  <img src="https://exemplo.com/caminho/para/imagem.png" alt="Homem de Ferro" width="200"/>
</p>

## Descrição

Esse é um projeto de uma API REST simples para gerenciar uma lista de usuários. A API foi construída usando Python e o framework Flask. O objetivo é permitir realizar operações básicas (criar, ler, atualizar e deletar) em uma lista de usuários.

Com certeza! Vamos atualizar o arquivo README.md para incluir exemplos de uso para cada uma das funcionalidades da API. Abaixo estão os exemplos de uso para cada item:

## Funcionalidades

### Listar todos os usuários

**Descrição**: Lista todos os usuários cadastrados na API.

**URL**: `http://localhost:5000/users`

**Método**: GET

**Exemplo de Uso**:
```bash
curl http://localhost:5000/users
```

**Resposta de Exemplo**:
```json
[
    {"id": 1, "name": "Tony Stark", "age": 35},
    {"id": 2, "name": "Steve Rogers", "age": 100},
    {"id": 3, "name": "Natasha Romanoff", "age": 32},
    {"id": 4, "name": "Bruce Banner", "age": 45},
    {"id": 5, "name": "Clint Barton", "age": 40},
    {"id": 6, "name": "Thor Odinson", "age": 1500},
    {"id": 7, "name": "Wanda Maximoff", "age": 29},
    {"id": 8, "name": "Scott Lang", "age": 40},
    {"id": 9, "name": "Peter Parker", "age": 23},
    {"id": 10, "name": "Carol Danvers", "age": 35}
]
```

### Obter um usuário por ID

**Descrição**: Obtém informações de um usuário específico por seu ID.

**URL**: `http://localhost:5000/users/<user_id>`

**Método**: GET

**Parâmetro**: `user_id` (int) - ID do usuário a ser buscado.

**Exemplo de Uso**:
```bash
curl http://localhost:5000/users/3
```

**Resposta de Exemplo**:
```json
{"id": 3, "name": "Natasha Romanoff", "age": 32}
```

### Adicionar um novo usuário

**Descrição**: Adiciona um novo usuário à lista de usuários.

**URL**: `http://localhost:5000/users`

**Método**: POST

**Corpo da Requisição**: JSON com os campos `name` e `age`.

**Exemplo de Uso**:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"Bruce Wayne", "age": 40}' http://localhost:5000/users
```

**Resposta de Exemplo**:
```json
{"id": 11, "name": "Bruce Wayne", "age": 40}
```

### Atualizar um usuário existente

**Descrição**: Atualiza as informações de um usuário existente por seu ID.

**URL**: `http://localhost:5000/users/<user_id>`

**Método**: PUT

**Parâmetro**: `user_id` (int) - ID do usuário a ser atualizado.

**Corpo da Requisição**: JSON com os campos `name` e `age`.

**Exemplo de Uso**:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name":"Diana Prince", "age": 35}' http://localhost:5000/users/10
```

**Resposta de Exemplo**:
```json
{"id": 10, "name": "Diana Prince", "age": 35}
```

### Deletar um usuário

**Descrição**: Deleta um usuário da lista por seu ID.

**URL**: `http://localhost:5000/users/<user_id>`

**Método**: DELETE

**Parâmetro**: `user_id` (int) - ID do usuário a ser deletado.

**Exemplo de Uso**:
```bash
curl -X DELETE http://localhost:5000/users/9
```

**Resposta de Exemplo**:
```json
{"message": "Usuário deletado"}
```

Lembre-se de substituir `localhost:5000` pelo endereço correto da API se ela estiver em execução em outro servidor. Esses exemplos mostram como fazer as requisições usando o comando `curl`, mas você também pode testar as funcionalidades usando outras ferramentas, como o Postman.

## Tecnologias Utilizadas

- Python
- Flask

## Como Usar

### Pré-requisitos

- Python (versão 3.x)
- Pip

### Instalação

1. Clone o repositório para o seu computador:

```bash
git clone https://github.com/seu-usuario/flask_rest_api_usuarios.git
```

2. Navegue até o diretório do projeto:

```bash
cd flask_rest_api_usuarios
```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

### Execução

1. Inicie a API:

```bash
python app.py
```

2. Acesse a API em `http://localhost:5000/`.

### Uso da API

- `GET /users` - Lista todos os usuários.
- `GET /users/<int:user_id>` - Obtém o usuário com ID especificado.
- `POST /users` - Adiciona um novo usuário. Envie os dados em JSON no corpo da requisição.
- `PUT /users/<int:user_id>` - Atualiza o usuário com ID especificado. Envie os dados em JSON no corpo da requisição.
- `DELETE /users/<int:user_id>` - Deleta o usuário com ID especificado.

## Contribuindo

Se você quiser contribuir com melhorias ou correções, sinta-se à vontade para abrir um Pull Request. Será um prazer receber sua ajuda!

## Licença

Este projeto está sob a licença [MIT](LICENSE).

## Criador

Criado por Marcos Silva.