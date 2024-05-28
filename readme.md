# FastAPI CRUD com MySQL e MongoDB
Este é um exemplo de aplicação CRUD (Create, Read, Update, Delete) usando o framework FastAPI do Python. O aplicativo é projetado para alternar entre dois bancos de dados diferentes, MySQL e MongoDB, usando o padrão de design Strategy.

## Recursos
CRUD completo para manipulação de usuários.
Suporte para MySQL e MongoDB como bancos de dados subjacentes.
Uso do padrão Strategy para alternar entre os bancos de dados.
## Requisitos
- Python 3.x
- FastAPI
- MySQL Connector Python
- PyMongo
## Instalação
Clone este repositório:
```
git clone https://github.com/seu_usuario/fastapi-crud.git
```

Navegue até o diretório do projeto:
```
cd fastcrud
```
Instale as dependências:
```
pip install -r requirements.txt
```
Uso
Execute o aplicativo:
```
uvicorn main:app --reload

ou 

python main.py
```
Acesse a documentação interativa do Swagger em:
```
http://localhost:8000/docs
```
Uso com MySQL

```
CREATE TABLE `usuarios` (
  `id` varchar(50) NOT NULL,
  `nome` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `senha` text,
  PRIMARY KEY (`id`)
) ;


```
Experimente as rotas CRUD fornecidas para manipulação de usuários.
## Estrutura do Projeto
- main.py: Arquivo principal que inicializa o aplicativo FastAPI.
- router/routes_usuario.py: Define as rotas para manipulação de usuários.
- controller/controller_usuario.py: Controlador que lida com as operações CRUD.
- database/: Pasta que contém os módulos relacionados aos bancos de dados.
- db_mysql.py: Implementação da classe para interagir com o MySQL.
- db_mongo.py: Implementação da classe para interagir com o MongoDB.
- database_strategy.py: Definição da interface Strategy.
- model/: Pasta que contém os modelos de dados Pydantic.
- config/: Pasta que contém arquivos de configuração e utilitários.
## Contribuindo
Sinta-se à vontade para abrir uma issue para relatar problemas, fazer sugestões ou contribuir com código.

## Licença
Este projeto está licenciado sob a MIT License.