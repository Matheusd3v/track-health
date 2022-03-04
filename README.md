# Rotas Públicas

# User

## POST - user/register

Essa rota é para o cadastro de usuário. Os campos obrigatórios são: name, email, birth_date e password. Passar os campos gender e sex é opcional.

Exemplo de requisição:

```
{
	"name":"  matheus   teste",
	"email":"matheus@email.com",
	"birth_date": "27/12/20",
	"password": "1234",
	"gender": "hetero",
	"sex": " masculino"
}
```

Exemplo de resposta, caso esta tudo correto o status retornado será 201 - CREATED:

```
{
	"id": "1af610f7-291d-49a3-8967-f430bd755fcb",
	"name": "Matheus Teste",
	"email": "matheus@email.com",
	"birth_date": "Sun, 27 Dec 2020 00:00:00 GMT",
	"gender": "Hetero",
	"sex": "Masculino",
	"allergy": [],
	"medications": [],
	"surgerys": [],
	"alcohol": null,
	"user_drug": null,
	"smoker": null,
	"physical_activity": null
}
```

## POST - user/login

Essa rota é para o login do usuário. Os campos obrigatórios são: email e password.

Exemplo de requisição:

```
{
	"email":"matheus@email.com",
	"password": "1234"
}
```

Exemplo de resposta, caso esteja tudo correto será retornado status 200 - OK:

```
{
	"user_data": {
		"id": "1af610f7-291d-49a3-8967-f430bd755fcb",
		"name": "Matheus Teste",
		"email": "matheus@email.com",
		"birth_date": "Sun, 27 Dec 2020 00:00:00 GMT",
		"gender": "Hetero",
		"sex": "Masculino",
		"allergy": [],
		"medications": [],
		"surgerys": [],
		"alcohol": null,
		"user_drug": null,
		"smoker": null,
		"physical_activity": null
	},
	"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NjM1MTkyNSwianRpIjoiMTQxMjRiNmMtNjNlYS00ZTUyLWE1NmYtZjJiYWRjMWYxYThhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6IjFhZjYxMGY3LTI5MWQtNDlhMy04OTY3LWY0MzBiZDc1NWZjYiIsIm5hbWUiOiJNYXRoZXVzIFRlc3RlIiwiZW1haWwiOiJtYXRoZXVzQGVtYWlsLmNvbSIsImJpcnRoX2RhdGUiOiJTdW4sIDI3IERlYyAyMDIwIDAwOjAwOjAwIEdNVCIsImdlbmRlciI6IkhldGVybyIsInNleCI6Ik1hc2N1bGlubyIsImFsbGVyZ3kiOltdLCJtZWRpY2F0aW9ucyI6W10sInN1cmdlcnlzIjpbXSwiYWxjb2hvbCI6bnVsbCwidXNlcl9kcnVnIjpudWxsLCJzbW9rZXIiOm51bGwsInBoeXNpY2FsX2FjdGl2aXR5IjpudWxsfSwibmJmIjoxNjQ2MzUxOTI1LCJleHAiOjE2NDYzNjYzMjV9.ZXeFle8qve-GlIB_GYR7A7CwBYadAtUc1rErlEEL55k"
}
```

# Rotas privadas

Para acessar essas rotas é necessário o envio do jwt por bearer token.

# User

## GET - user

Essa rota é para obter os dados do usuário. Deverá ser passado somente o jwt por bearer token, não havendo necessidade de corpo de requisição.

Exemplo de resposta:

```
{
	"id": "1af610f7-291d-49a3-8967-f430bd755fcb",
	"name": "Matheus Teste",
	"email": "matheus@email.com",
	"birth_date": "Sun, 27 Dec 2020 00:00:00 GMT",
	"gender": "Hetero",
	"sex": "Masculino",
	"allergy": [],
	"medications": [],
	"surgerys": [],
	"alcohol": null,
	"user_drug": null,
	"smoker": null,
	"physical_activity": null
}
```

## PATCH - user

Essa rota é para atualização de cadastro do usuário. Os unicos campos que serão alterados, caso sejam passados, são: name, email, birth_date, password, sex e gender. Poderá ser passado somente um ou todos de uma vez. Qualquer campo extra, será ignorado.

Exemplo de requisição:

```
{
	"name": " matheus gomes",
	"campo_extra": "extra"
}
```

Exemplo de resposta, retornando status 200 - OK se estiver tudo correto:

```
{
	"id": "1af610f7-291d-49a3-8967-f430bd755fcb",
	"name": "Matheus Gomes",
	"email": "matheus@email.com",
	"birth_date": "Sun, 27 Dec 2020 00:00:00 GMT",
	"gender": "Hetero",
	"sex": "Masculino",
	"allergy": [],
	"medications": [],
	"surgerys": [],
	"alcohol": null,
	"user_drug": null,
	"smoker": null,
	"physical_activity": null
}
```

## DELETE - user

Essa rota é para deletar um usuário. Não necessita de corpo de requisição, somente o bearer token. Não é retornado corpo, somente status 204 caso tudo ocorra bem.

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

# DISEASE

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
Os campos obrigatórios são: “name”, “type”, "phone" e "address_id", ele cria um histórico dos médicos e ainda relacionando com o endereço deste.

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

## PATCH - /doctor/<int:doctor_id>

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

## DELETE - /doctor/<int:doctor_id

Esta rota é para deletar um dos médicos do usuário. Para realizar a deleção é somente necessário passar o doctor_id por query params.

Authorization: ` Bearer Token`

# Surgerys

## POST - /surgery

Esta rota é para a criação de cirurgias, estas cirurgias não terão nenhuma relação com o usuário. Só é necessário passar o campo "name" na requisição como mostrado no exemplo abaixo.

```json
{
  "name": "Cirurgia na visicula"
}
```

Caso a requisição tenha sucesso irá retornar a seguinte resposta com o status code de 201.

```json
{
  "id": "ba1927e3-4d16-437c-8cc7-229d1bcf92e4",
  "name": "Cirurgia na visicula"
}
```

## POST - user/surgery

Esta rota é para a criação de cirurgias relacionadas ao usuário. Para a realização desta requisição é necessário os campo "name" e "date", o campo "description" no exemplo abaixo é opcional.

Authorization: ` Bearer Token`

```json
{
  "name": "Cirurgia do apendice",
  "description": "Realizei essa cirurgia há 2 anos atrás e não tive nenhuma complicação",
  "date": "03/02/2020"
}
```

Caso dê tudo certo irá retornar a seguinte resposta e código 201

```json
{
  "id": "bf212d16-2681-4f0d-a6e4-0db2318305f1",
  "name": "Cirurgia do apendice",
  "description": "Realizei essa cirurgia há 2 anos atrás e não tive nenhuma complicação",
  "date": "03/02/2020"
}
```

## PATCH - /user/surgery/<surgery_id>

Esta rota é para atualização de uma cirurgia, sendo possível atualizar apenas "date" e "description". Exemplo de requisição abaixo:

Authorization: ` Bearer Token`

```json
{
  "description": "Atualizando a descrição",
  "date": "03/03/2022"
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

## DELETE - /user/surgery/<surgery_id>

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
  "name": "Insulina",
  "description": "Teste de descricação"
}
```

Caso dê tudo certo irá retornar 201

```json
{
  "id": "19ee0dda-da00-4018-90a1-6d72bbe35ec4",
  "name": "Insulina",
  "description": "Teste de descricação"
}
```

## PATCH - /user/medication/<medication_id>

Esta rota é para atualização de uma medicação do usuário. O único campo que pode ser atualizado é "description" como mostrado abaixo.

Authorization: ` Bearer Token`

```json
{
  "description": "Mudando a descrição"
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

# Drug

## POST - user/drug

Essa rota é para o cadastro de informação referente ao uso de drogas. É necessário enviar unicamente os campos: frequency e description.

Exemplo de requisição:

```
{
	"frequency": "uma vez por semana",
	"description": "tabaco orgânico"
}
```

Exemplo de resposta, retornando status 201 - CREATED caso esteja tudo correto:

```
{
	"id": "4807bb8c-2dd1-4236-8f96-eae16df96b0b",
	"frequency": "uma vez por semana",
	"description": "tabaco orgânico"
}
```

## PATCH - user/drug

Essa rota é para alterar informações referente a uso de drogas. Será alterado somente os campos frequency e description, campos extras serão ignorados.

Exemplo de requisição:

```
{
	"frequency": "uma vez ao dia"
}
```

Exemplo de resposta, retornando status 200 - OK caso tudo ocorra bem:

```
{
	"id": "4807bb8c-2dd1-4236-8f96-eae16df96b0b",
	"frequency": "Uma vez ao dia",
	"description": "tabaco orgânico"
}
```

## GET - user/drug

Essa rota é para obtenção das informações sobre dogras. Não é necessário enviar corpo de requisição, somente o token jwt.

Exemplo de resposta, com status 200 - OK caso esteja tudo correto:

```
{
	"id": "4807bb8c-2dd1-4236-8f96-eae16df96b0b",
	"frequency": "Uma vez ao dia",
	"description": "tabaco orgânico"
}
```

## DELETE user/drug

Essa rota é para deletar as informações. Não é necessário enviar corpo de requisição, somente o token. Não será retornado corpo, somente status 204 se estiver tudo correto.

# ALLERGY

## POST - /allergy

Esta rota é para adicionar uma alergia na tabela de alergias. Campo obrigatório é apenas o "name".

Authorization: ` Bearer Token`

```json
{
  "name": "camarão"
}
```

Retorno esperado :

```json
{
  "id": "df85ee37-0766-4c7c-bd78-0489596e398d",
  "name": "camarão"
}
```

## GET - /user/allergy

Esta rota é para pegar todas as alergias do usuário, não sendo necessário passar nenhum body.

Authorization: ` Bearer Token`

## POST - /user/allergy

Esta rota é para o cadastro das alergias de um usuário, caso a alergia não exista na tabela ela a cria.
Os campos obrigatórios são: “name”, "description" sendo facultativo.

Exemplo de requisição abaixo:

Authorization: ` Bearer Token`

```json
{
  "name": "frutos do mar",
  "description": "alergia grave a frutos do mar"
}
```

Retorno esperado :

```json
{
  "id": "0d3316dd-bd68-4e27-984c-98b40b2fbb76",
  "description": "Alergia grave a frutos do mar",
  "allergy": {
    "id": "83cbe018-eaff-4fc2-87f7-f1cbdc7773a6",
    "name": "Frutos Do Mar"
  }
}
```

## PATCH - /user/allergy/<int:allergy_id>

Esta rota é para a atualização dos dados de uma das alergias do usuário, podendo atualizar “name” e “description".
Para realizar a atualização é somente necessário passar o id da alergia do usuário por query params.

Exemplo de requisição:

Authorization: ` Bearer Token`

```json
{
  "name": "camarão",
  "description": "Alergia grave a camarão"
}
```

Retorno esperado :

```json
{
  "id": "f3498206-47cd-4eca-acf7-03617dd31670",
  "description": "Alergia grave a pelo de cachorro",
  "allergy": {
    "id": "205d4f8e-a236-4410-8faf-559ac69244f3",
    "name": "Cachorro"
  }
}
```

## DELETE - /user/allergy/<int:allergy_id

Esta rota é para deletar uma das alergias do usuário. Para realizar a deleção é somente necessário passar o id da alergia do usuário por query params.

Authorization: ` Bearer Token`
