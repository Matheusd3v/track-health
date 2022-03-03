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
  "name": "John",
  "type": "cardiologista"
}
```

Retorno esperado :

```json
{
  "id": "c1aaec1c-53b3-4f04-8e68-971141d283a5",
  "name": "John",
  "type": "cardiologista",
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

## DELETE - user/exams/<int:exam_id

Esta rota é para apagar um exame do usuário. Para realizar a deleção é somente necessário passar o exam_id por query params.

Authorization: ` Bearer Token`
