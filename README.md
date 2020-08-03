# Flask Desafio

Criar uma Estrutura para clientes e grupo de clientes.

#### DataBase
Foi utilizado o postgresSql 9.6

### Migrations
Comando para rodar as migrations:

```sh
flask db init
flask db migrate
flask db upgrade
flask run
```

## Json
``
{
  "name": "Group Name"
}
``
#### Client
``
{
  "name": "Client Name",
  "email":"Email",
  "groupCliente_id":"group client id"
}
``