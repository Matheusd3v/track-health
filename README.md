# Exams

## POST - user/exams

Esta rota é para o cadastro de exames relacionados ao usuário. 
Os campos obrigatórios são:  “name”, “date”, caso o o nome do exame enviado já exista ele irá buscar na base de dados, caso não exista, irá cadastrar um novo exame.

Exemplo de requisição abaixo:

Authorization: ` Bearer Token`

```json

  {
	"name": "hemograma",
	"date": "22/02/2022",
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

Esta rota é para o cadastro de doenças  relacionados ao usuário. Sendo obrigatório somente o campo “name”

Exemplo de requisição:

Authorization: ` Bearer Token`

```json
{
"name":"Gripe",
"description":"gripe forte",
"medication": "paracetamol"
}
```
## PATCH - user/diseases/<int:user_disease_id>

Esta rota é para a atualização das doenças  do usuário, podendo atualizar somente a “description” e ”medication” 

Exemplo de requisição:

```json
{
"description":"gripe leve",
"medication": "Antialergico"
}
```

## DELETE - user/diseases/<int:user_disease_id>

Esta rota é para apagar um exame do usuário. Para realizar a deleção é somente necessário passar o disease_id por query params.
