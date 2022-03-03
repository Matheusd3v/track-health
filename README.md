# Exams

## POST - user/exams

Esta rota é para o cadastro de exames relacionados ao usuário.
Os campos obrigatórios são: “name”, “date”, caso o o nome do exame enviado já exista ele irá buscar na base de dados, caso não exista, irá cadastrar um novo exame.

Exemplo de requisição abaixo:

Authorization: ` Bearer Token`

```json
{
  "name": "hemograma",
  "date": "22/02/2022"
}
```

Retorno esperado :

```json
{
  "id": "9",
  "user_id": "7",
  "exam_id": "8",
  "exam_details_id": "5"
}
```

## PATCH - user/exams/<int:exam_id>

Esta rota é para a atualização dos exames do usuário, podendo atualizar somente a “date”,”description” e a “upload_img” do exame

Exemplo de requisição:

Authorization: ` Bearer Token`

```json
{
  "name": "hemograma",
  "date": "22/02/2022",
  "upload_img": "matheus_pic_profile.png",
  "description": "Descrição maneira"
}
```

## DELETE - user/exams/<int:exam_id

Esta rota é para apagar um exame do usuário. Para realizar a deleção é somente necessário passar o exam_id por query params.

Authorization: ` Bearer Token`

## POST - user/diseases

Esta rota é para o cadastro de doenças relacionados ao usuário. Sendo obrigatório somente o campo “name”

Exemplo de requisição:

Authorization: ` Bearer Token`

```json
{
  "name": "Gripe",
  "description": "gripe forte",
  "medication": "paracetamol"
}
```

## PATCH - user/diseases/<int:user_disease_id>

Esta rota é para a atualização das doenças do usuário, podendo atualizar somente a “description” e ”medication”

Exemplo de requisição:

```json
{
  "description": "gripe leve",
  "medication": "Antialergico"
}
```

## DELETE - user/diseases/<int:user_disease_id>

Esta rota é para apagar um exame do usuário. Para realizar a deleção é somente necessário passar o disease_id por query params.

# DOCTOR

## GET - /doctor

Esta rota é para pegar os médicos do usuário. Não é necessário passar nenhum body.

Authorization: ` Bearer Token`

## POST - /doctor

Esta rota é para o cadastro de médicos relacionados ao usuário.
Os campos obrigatórios são: “name”, “type”,"phone" e "address_id", ele cria um histórico dos médicos e ainda relacionando com o endereço deste.

Exemplo de requisição abaixo:

Authorization: ` Bearer Token`

```json
{
  "name": "john doe",
  "type": "endocrino",
  "phone": "(21)12345-6789",
  "address_id": "10cdd6a6-670b-4df9-9055-4ba711eadb3e"
}
```

Retorno esperado :

```json
{
  "id": "c1aaec1c-53b3-4f04-8e68-971141d283a5",
  "name": "John Doe",
  "type": "Endocrino",
  "email": null,
  "phone": "(21)12345-6789",
  "address": {
    "id": "10cdd6a6-670b-4df9-9055-4ba711eadb3e",
    "street": "rua x",
    "number": 50,
    "district": "A",
    "city": "X",
    "complement": "abc"
  }
}
```

## PATCH - /doctor/<int:exam_id>

Esta rota é para a atualização dos dados de um dos médicos do usuário, podendo atualizar “name”, “type”,"phone", "address_id" e "email".

Exemplo de requisição:

Authorization: ` Bearer Token`

```json
{
	"name": "Gustavo",
	"type": "ginecologista",
	"telephone": "(21)9"
}
}
```

## DELETE - user/exams/<int:exam_id

Esta rota é para apagar um exame do usuário. Para realizar a deleção é somente necessário passar o exam_id por query params.

Authorization: ` Bearer Token`


# Surgerys


## POST  - /surgery
Esta rota é para a criação de cirurgias, estas cirurgias não terão nenhuma relação com o usuário. Só é necessário passar o campo "name" na requisição como mostrado no exemplo abaixo.

```json
	{
		"name":"Cirurgia na visicula"
	}
```
Caso a requisição tenha sucesso irá retornar a seguinte resposta com o status code de 201.

```json

{
  "id": "ba1927e3-4d16-437c-8cc7-229d1bcf92e4",
  "name":"Cirurgia na visicula"
}

```

## POST - user/surgery
Esta rota é para a criação de cirurgias relacionadas ao usuário. Para a realização desta requisição é necessário os campo "name" e "date", o campo "description" no exemplo abaixo é opcional.


Authorization: ` Bearer Token`
```json
{
	"name":"Cirurgia do apendice",
	"description": "Realizei essa cirurgia há 2 anos atrás e não tive nenhuma complicação",
	"date":"03/02/2020"
}

```
Caso dê tudo certo irá retornar a seguinte resposta e código 201
```json
{
	"id":"bf212d16-2681-4f0d-a6e4-0db2318305f1",
	"name":"Cirurgia do apendice",
	"description": "Realizei essa cirurgia há 2 anos atrás e não tive nenhuma complicação",
	"date":"03/02/2020"
}
```

## PATCH - /user/surgery/<surgery_id>
Esta rota é para atualização de uma cirurgia, sendo possível atualizar apenas "date" e "description". Exemplo de requisição abaixo:

Authorization: ` Bearer Token`

```json
{
	"description":"Atualizando a descrição",
	"date":"03/03/2022"
}
```

Caso dê tudo certo a resposta será a seguinte

```json
{
	"id": "9525ab67-d12c-42e8-83de-e98127565743",
	"name": "Cirurgia do apendice",
	"date": "Thu, 03 Mar 2022 00:00:00 GMT",
  	"description": "Atualizando a descrição"
}

``` 



## DELETE -  /user/surgery/<surgery_id>
Esta rota é para deletar alguma cirurgia relacionada ao usuário, não é necessário nenhum corpo na requisição apenas a autenficação com token. Caso dê tudo certo irá retornar o código 204.

Authorization: ` Bearer Token`



## GET - /user/surgery
Não é necessário nenhum corpo apenas a o token. Caso tudo dê certo irá retornar um dicionário com todas as cirurgias do usuários e um status code 200.

#
# Medication
 
## POST - /medication 
Esta rota é para criação de medicamentos sem relação com o usuário. Para a criação de um medicamento é necessário apenas o campo "name" como mostrado na requisição abaixo.

```json
{
  "name": "Dramin"
}
``` 
Caso dê tudo certo irá retornar o código 201 e seguinte json
```json
{
  "id": "3f2a3954-b306-4573-8f80-de210f6aeda6",
  "name": "Dramin"
}

```

## POST - /user/medication
Esta rota é para a criação de medicamentos relacionados ao usuário. Os campos obrigatórios são "name" e "description" como no exemplo abaixo:

Authorization: ` Bearer Token`
```json
{
	"name":"Insulina",
	"description":"Teste de descricação"
}

```
Caso dê tudo certo irá retornar 201
```json
{
  	"id": "19ee0dda-da00-4018-90a1-6d72bbe35ec4",
  	"name": "Insulina",
 	"description":"Teste de descricação"
}

```

## PATCH - /user/medication/<medication_id>
Esta rota é para atualização de uma medicação do usuário. O único campo que pode ser atualizado é "description" como mostrado abaixo.

Authorization: ` Bearer Token`
```json
{
	"description":"Mudando a descrição"
}
```
Caso a requisição seja bem sucedida irá retornar o código 200 e o seguinte json

```json
{
  "id": "788f12e6-c0b9-453c-aaeb-183b8e2d49f7",
  "name": "Insulina",
  "description": "Mudando a descrição"
}
```

## DELETE - /user/medication/<medication_id>
Esta rota é para deletar um medicamento sendo necessário apenas passar o medication_id via url. Caso dê tudo irá retornar 204.

Authorization: ` Bearer Token`


## GET - /user/medication
Não é necessário nenhum corpo apenas a o token. Caso tudo dê certo irá retornar um dicionário com todos os medicamentos do usuários e um status code 200.
