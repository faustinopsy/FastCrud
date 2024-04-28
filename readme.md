# FastAPI CRUD com MySQL e MongoDB
Este é um exemplo de aplicação CRUD (Create, Read, Update, Delete) usando o framework FastAPI do Python. O aplicativo é projetado para alternar entre dois bancos de dados diferentes, MySQL e MongoDB, usando o padrão de design Strategy.
para saber mais sobre o fastAPI: https://fastapi.tiangolo.com/learn/
um framework python muito poderoso que facilita a criação de rotas e documentação automatica de API

## Branch monitoracao ***
- nova branch (https://github.com/faustinopsy/FastCrud/tree/monitoracao)
- nela foi adicionada um dashboard protegido com login e token jwt, mas o recurso dessa branch é a capacidade de inserir no banco toda tentativa de acesso às rotas gerando um log de uso da API, e outro recurso para monitorar é o dashboard com gráfico usando um recurso avançado chamado SSE.

- SSE (Server-Sent Events) é uma tecnologia web que permite que um servidor envie automaticamente dados para um cliente assim que esses dados estiverem disponíveis, sem a necessidade de uma solicitação explícita do cliente, é uma forma de comunicação unidirecional do servidor para o cliente.

O SSE foi projetado para facilitar a transmissão de dados em tempo real do servidor para o navegador, permitindo a criação de aplicativos que exibam informações dinamicamente sem fazer varias requisições para o servidor, como feeds de notícias, atualizações de status, feeds de redes sociais em tempo real, entre outros.

### Principais características e usos do SSE:

- Comunicação assíncrona: 
O SSE permite que os servidores enviem dados para os clientes de forma assíncrona, o que significa que os clientes não precisam fazer solicitações repetidas para obter atualizações.
- Padrão baseado em eventos: 
Os dados enviados pelo servidor são organizados em eventos, cada um com um nome e opcionalmente um corpo de dados associado. O cliente pode então ouvir esses eventos e responder a eles conforme necessário.
- Compatibilidade com navegadores: 
SSE é suportado nativamente por todos os principais navegadores modernos, o que torna uma opção acessível para desenvolvedores web.
- Simplicidade de implementação: 
Comparado a outras tecnologias de comunicação em tempo real, como WebSockets, SSE é mais simples de implementar e não requer configuração adicional no servidor.
-Baixa latência: 
Como os dados são enviados do servidor para o cliente assim que estão disponíveis, o SSE pode fornecer atualizações em tempo real com baixa latência, tornando-o adequado para aplicativos que exigem respostas rápidas.
- Eficiência de largura de banda: 
SSE usa uma conexão HTTP única e mantém essa conexão aberta enquanto necessário, reduzindo a sobrecarga de conexão e tornando-o eficiente em termos de largura de banda.

### Implicações e potenciais do SSE:

- Aplicações em tempo real: 
SSE é amplamente utilizado em aplicativos da web que exigem atualizações em tempo real, como feeds de notícias ao vivo, salas de bate-papo, sistemas de monitoramento em tempo real e notificações em tempo real.
- Feedback em tempo real: 
Podemos usar SSE para fornecer feedback instantâneo aos usuários sobre ações realizadas no aplicativo, como confirmações de envio de formulário, progresso de operações e atualizações de estado, ou atualização de dados no banco de dados.
- Streaming de dados: 
SSE pode ser usado para transmitir dados de forma contínua para o cliente, como transmissões de áudio e vídeo, atualizações de jogos online e dados de sensores em tempo real.


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
);
CREATE TABLE `logs` (
  `id` char(45) NOT NULL,
  `path` varchar(255) NOT NULL,
  `method` varchar(10) NOT NULL,
  `client_ip` varchar(45) NOT NULL,
  `data_ini` datetime NOT NULL,
  `data_fim` datetime NOT NULL,
  `process_time` varchar(50) NOT NULL,
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
git clone https://github.com/faustinopsy/FastCrud.git
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