
![Logo](https://aws.github.io/chalice/_images/chalice-logo-whitespace.png)


# To Do API usando Chalice AWS e Domain Driven Disign (DDD)

Essa é uma simples API que usa Chalice AWS e DDD, ela foi desenvolvida para estudos da arquitetura.





## Autor

- [Luis Henrque](https://www.github.com/luishenrique01)


## Tecnologias

**Server:** Lambda, API Gateway e DynamoDB.

**Framework:** Chalice AWS e Boto3.


## Features

- Criar tabela de usuários.
- Criar sistema de autenticação.
- Utilizar o Amazon SES para enviar notificações.
- Utilizar o CloudWatch para criar lembretes antes do vencimento da tarefa.
- Utilizar uma Lambda para enviar mensagem de atividade criada.
- Criar sistema de grupos de usuários.


## Rodar local

Para rodar o projeto, você precisará de uma instância do DynamoDB. Caso não queira pagar por uma instância, você pode utilizar o Docker.

```bash
  docker pull amazon/dynamodb-local
  docker run -d -p 8000:8000 --network=dynamo-local-network --name dynamo-local amazon/dynamodb-local -jar DynamoDBLocal.jar -sharedDb
```

Agora é só rodar o Chalice localmente, como a porta 8000 tá ocupada irei usar 8001.

```bash
  chalice local --port 8001
```
