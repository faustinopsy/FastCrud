# FastAPI CRUD com MySQL e MongoDB
Este é um exemplo de aplicação CRUD (Create, Read, Update, Delete) usando o framework FastAPI do Python. O aplicativo é projetado para alternar entre dois bancos de dados diferentes, MySQL e MongoDB, usando o padrão de design Strategy.

## Recursos
CRUD completo para manipulação de usuários.
Suporte para MySQL e MongoDB como bancos de dados subjacentes.
Uso do padrão Strategy para alternar entre os bancos de dados.
no arquivo controller_usuario tem a linha abaixo que poderá alterar o banco de dados a ser utilizado, 
e dentro de cada classe do banco precisa´ra colocar todos os métodos a serem manipulados no banco de dados para cada entidade do banco, o modelo poderá ser melhorado para deixar mais genérica isso deixo como desafio para quem quiser usar..
outro recurso aqui é o token JWT ao realizar o login receberá o token que o forntend precisa armazenar para reenviar nas requisições, as requisições até o momento são listar_usuarios e verificar token para realizar a validação.

```
#db = MySQL()
db = MongoDB()

```
se for utilizado o MySQL use a tabela:

```
CREATE TABLE `usuarios` (
  `id` varchar(50) NOT NULL,
  `nome` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `senha` text,
  PRIMARY KEY (`id`)
)

```

Sobre o token jwt, toda a lógica esta encapsulada no arquivo token.py dentro do diretorio controller, e para proteger uma rota adicione a dependência

```
@router.get("/usuarios/", dependencies=[Depends(verificar_token)])
def listar_usuarios():
    return controller.listar_usuarios()
```

## Requisitos
- Python 3.x
- FastAPI
- MySQL Connector Python
- PyMongo
## Instalação
Clone este repositório:
```
git clone https://github.com/faustinopsy/fastapi-crud.git
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
Experimente as rotas CRUD fornecidas para manipulação de usuários.
## Estrutura do Projeto
- main.py: Arquivo principal que inicializa o aplicativo FastAPI.
- router/routes_usuario.py: Define as rotas para manipulação de usuários.
- controller/controller_usuario.py: Controlador que lida com as operações CRUD.
- controller/token.py: controlador que lida com a geração e validação do token JWT.
- database/: Pasta que contém os módulos relacionados aos bancos de dados.
- db_mysql.py: Implementação da classe para interagir com o MySQL.
- db_mongo.py: Implementação da classe para interagir com o MongoDB.
- database_strategy.py: Definição da interface Strategy.
- model/: Pasta que contém os modelos de dados Pydantic.
- config/: Pasta que contém o helper para gerenciar o Cors.
## Contribuindo
Sinta-se à vontade para abrir uma issue para relatar problemas, fazer sugestões ou contribuir com código.

## Licença
Este projeto está licenciado sob a MIT License.