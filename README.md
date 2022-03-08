|Methods  |Endpoint|Responsability|
----------------------------------|  -------|  -------------------------------------|
|POST    |/user/register||
|POST    |/user/login||
|GET     |/user/exam||
|POST    |/user/exam||
|PATCH   |/user/exam/<exam_id>||
|DELETE  |/user/exam/<exam_id>||
|DELETE  |/user/exam/file/<exam_id>||
|POST    |/user/exam/file/<exam_id>||
|POST    |/user/allergy||
|GET     |/user/allergy||
|PATCH   |/user/allergy/<allergy_id>||
|DELETE  |/user/allergy/<allergy_id>||
|POST    |/user/medication||
|DELETE  |/user/medication/<medication_id>||
|GET     |/user/medication||
|PATCH   |/user/medication/<medication_id>||
|GET     |/user/diseases||
|POST    |/user/diseases||
|PATCH   |/user/diseases/<disease_id>||
|DELETE  |/user/diseases/<disease_id>||
|POST    |/user/surgery||
|DELETE  |/user/surgery/<id>||
|GET     |/user/surgery||
|PATCH   |/user/surgery/<id>||
|POST    |/user/drug||
|DELETE  |/user/drug||
|GET     |/user/drug||
|PATCH   |/user/drug||
|POST    |/user/physical_activity||
|DELETE  |/user/physical_activity||
|GET     |/user/physical_activity||
|PATCH   |/user/physical_activity||
|POST    |/user/smoker||
|DELETE  |/user/smoker||
|GET     |/user/smoker||
|PATCH   |/user/smoker||
|POST    |/user/alcoholic||
|GET     |/user/alcoholic/<string:alcoholic_id>||
|DELETE  |/user/alcoholic/<string:alcoholic_id>||
|PATCH   |/user/alcoholic/<string:alcoholic_id>||
|POST    |/user/anamnesis||
|GET     |/user/anamnesis||
|PATCH   |/user/anamnesis||
|DELETE  |/user/image-profile||
|GET     |/user/image-profile||
|POST    |/user/image-profile||
|DELETE  |/user||
|GET     |/user||
|PATCH   |/user||
|POST     |/address|  Criação de um endereço. |
|GET      |/address|Vizualizar os endereços.| 
|PATCH    |/address|Atualização de um endereço.| 
|DELETE   |/address|Deletar um endereço.| 
|POST    |/allergy|Criação de uma alergia.|  
|POST    |/appointments| Criação de um agendamento.
|GET     |/appointments/<string:appointment_id>| Vizualação dos agendamentos.|
|PATCH   |/appointments/<string:appointment_id>| Atualização de um agendamento.| 
|DELETE  |/appointments/<string:appointment_id>| Deletar um agendamento. | 
|POST    |/doctor|Criação de um médico relacionado ao usuário.| 
|GET     |/doctor| Ver todos os médicos relacionao ao usuário. | 
|DELETE  |/doctor/<doctor_id>| Deletar um médico relacionado ao usuário.|
|PATCH   |/doctor/<doctor_id>|Atualizar os dados de um médico.| 
|POST    |/exams| Criar um exame.|
|POST    |/medication|Criar uma medicação.| 
|GET     |/pdf| Retorna um PDF com os dados do usuário. |
|POST    |/surgery|Criação de uma cirurgia.| 


# Rotas Públicas

# User

## POST - user/register

Essa rota é para o cadastro de usuário. Os campos obrigatórios são: name, email, birth_date e password. Passar os campos gender e sex é opcional.

Exemplo de requisição:

```json
{
  "name": "malaquias brandão",
  "email": "malaquias@email.com",
  "birth_date": "25/12/25",
  "password": "1234",
  "gender": "hetero",
  "sex": " masculino"
}
```

Exemplo de resposta, caso esta tudo correto o status retornado será 201 - CREATED:

```json
{
  "id": "8a067378-ed52-4d67-85ca-0daa8cf000b4",
  "name": "Malaquias Brandão",
  "email": "malaquias@email.com",
  "birth_date": "Thu, 25 Dec 2025 00:00:00 GMT",
  "gender": "Hetero",
  "sex": "Masculino",
  "allergy": [],
  "medications": [],
  "surgerys": [],
  "alcohol": null,
  "user_drug": null,
  "smoker": null,
  "physical_activity": null,
  "anamnesis": [],
  "diseases": [],
  "exams": [],
  "image_profile": null
}
```

## POST - user/login

Essa rota é para o login do usuário. Os campos obrigatórios são: email e password.

Exemplo de requisição:

```json
{
  "email": "malaquias@email.com",
  "password": "1234"
}
```

Exemplo de resposta, caso esteja tudo correto será retornado status 200 - OK:

```json
{
  "user_data": {
    "id": "8a067378-ed52-4d67-85ca-0daa8cf000b4",
    "name": "Malaquias Brandão",
    "email": "malaquias@email.com",
    "birth_date": "Thu, 25 Dec 2025 00:00:00 GMT",
    "gender": "Hetero",
    "sex": "Masculino",
    "allergy": [],
    "medications": [],
    "surgerys": [],
    "alcohol": null,
    "user_drug": null,
    "smoker": null,
    "physical_activity": null,
    "anamnesis": [],
    "diseases": [],
    "exams": [],
    "image_profile": null
  },
  "access_token": TOKEN
}
```

# Rotas privadas

Para acessar essas rotas é necessário o envio do jwt por bearer token.

# User

## GET - user

Essa rota é para obter os dados do usuário. Deverá ser passado somente o jwt por bearer token, não havendo necessidade de corpo de requisição.

Exemplo de resposta:

```json
{
  "id": "8a067378-ed52-4d67-85ca-0daa8cf000b4",
  "name": "Malaquias Brandão",
  "email": "malaquias@email.com",
  "birth_date": "Thu, 25 Dec 2025 00:00:00 GMT",
  "gender": "Hetero",
  "sex": "Masculino",
  "allergy": [],
  "medications": [],
  "surgerys": [],
  "alcohol": null,
  "user_drug": null,
  "smoker": null,
  "physical_activity": null,
  "anamnesis": [],
  "diseases": [],
  "exams": [],
  "image_profile": null
}
```

## PATCH - user

Essa rota é para atualização de cadastro do usuário. Os unicos campos que serão alterados, caso sejam passados, são: name, email, birth_date, password, sex e gender. Poderá ser passado somente um ou todos de uma vez. Qualquer campo extra, será ignorado.

Exemplo de requisição:

```json
{
  "name": " matheus gomes",
  "campo_extra": "extra"
}
```

Exemplo de resposta, retornando status 200 - OK se estiver tudo correto:

```json
{
  "id": "8a067378-ed52-4d67-85ca-0daa8cf000b4",
  "name": "Matheus Gomes",
  "email": "malaquias@email.com",
  "birth_date": "Thu, 25 Dec 2025 00:00:00 GMT",
  "gender": "Hetero",
  "sex": "Masculino",
  "allergy": [],
  "medications": [],
  "surgerys": [],
  "alcohol": null,
  "user_drug": null,
  "smoker": null,
  "physical_activity": null,
  "anamnesis": [],
  "diseases": [],
  "exams": [],
  "image_profile": null
}
```

## DELETE - user

Essa rota é para deletar um usuário. Não necessita de corpo de requisição, somente o bearer token. Não é retornado corpo, somente status 204 caso tudo ocorra bem.

# Exams

## GET - user/exam

Esta rota é para a visualização dos exames cadastradas pelo usuário.

Exemplo de requisição:

Authorization: ` Bearer Token`

Retorno esperado :
```json
[
  {
    "id": "ed3ef1f1-e82b-48b5-ba03-18c6e4f79402",
    "name": "Hemograma",
    "description": "Controle de glicemia",
    "date": "Fri, 25 Dec 2020 00:00:00 GMT",
    "upload_img": null,
  },
  {
    "id": "ed3ef1f1-e82b-48b5-ba03-18c6e4f79402",
    "name": "Galilei G4",
    "description": "exame de vista",
    "date": "Fri, 25 Dec 2020 00:00:00 GMT",
    "upload_img": "www.google.com.br/exame.jpg",
  }
]
```

## POST - user/exam

Esta rota é para o cadastro de exames relacionados ao usuário.
Os campos obrigatórios são: “name”, “date”, caso o o nome do exame enviado já exista ele irá buscar na base de dados, caso não exista, irá cadastrar um novo exame.

Exemplo de requisição abaixo:

Authorization: ` Bearer Token`

```json
{
  "name": "hemograma",
  "date": "12/27/20"
}
```

Retorno esperado :

```json
{
  "id": "9",
	"name": "Hemograma",
	"date": "Sun, 27 Dec 2020 00:00:00 GMT",
	"description": null,
	"upload_img": null
}
```

## PATCH - user/exam/<int:exam_id>

Esta rota é para a atualização dos exames do usuário, podendo atualizar somente a “date”,”description” e a “upload_img” do exame

Exemplo de requisição:

Authorization: ` Bearer Token`

```json
{
  "date": "22/02/2022",
  "upload_img": "matheus_pic_profile.png",
  "description": "Descrição maneira"
}
```

## DELETE - user/exam/<int:exam_id>

Esta rota é para apagar um exame do usuário. Para realizar a deleção é somente necessário passar o exam_id por query params.

Authorization: ` Bearer Token`


# DISEASE

## GET - user/diseases

Esta rota é para a visualização das doenças cadastradas pelo usuário.

Exemplo de requisição:

Authorization: ` Bearer Token`

Retorno esperado :

```json
[
  {
    "id": "ed3ef1f1-e82b-48b5-ba03-18c6e4f79402",
    "name": "Diabete",
    "description": "Diabete tipo 2",
    "medication": "Insulina"
  },
  {
    "id": "ed3ef1f1-e82b-48b5-ba03-18c6e4f79402",
    "name": "Diabete",
    "description": "Diabete tipo 2",
    "medication": "Insulina"
  }
]
```

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

Retorno esperado :

```json
{
  "id": "8437341d-fe35-4532-ad0e-5c9005e34555",
  "name": "Gripe",
  "medication": "Paracetamol",
  "description": "Gripe forte"
}
```

## PATCH - user/diseases/<int:user_disease_id>

Esta rota é para a atualização das doenças do usuário, podendo atualizar somente a “description” e ”medication”.

Authorization: ` Bearer Token`

Exemplo de requisição:

```json
{
  "description": "gripe leve",
  "medication": "Antialergico"
}
```

Retorno esperado :

```json
{
  "id": "8437341d-fe35-4532-ad0e-5c9005e34555",
  "name": "Gripe",
  "medication": "Paracetamol",
  "description": "Gripe forte"
}
```

## DELETE - user/diseases/<int:user_disease_id>

Esta rota é para apagar um doença do usuário. Para realizar a deleção é somente necessário passar o user_disease_id por query params.

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

## DELETE - user/doctor/<int:doctor_id

Esta rota é para apagar um médico do usuário. Para realizar a deleção é somente necessário passar o doctor_id por query params.

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

```json
{
  "frequency": "uma vez por semana",
  "description": "tabaco orgânico"
}
```

Exemplo de resposta, retornando status 201 - CREATED caso esteja tudo correto:

```json
{
  "id": "4807bb8c-2dd1-4236-8f96-eae16df96b0b",
  "frequency": "uma vez por semana",
  "description": "tabaco orgânico"
}
```

## PATCH - user/drug

Essa rota é para alterar informações referente a uso de drogas. Será alterado somente os campos frequency e description, campos extras serão ignorados.

Exemplo de requisição:

```json
{
  "frequency": "uma vez ao dia"
}
```

Exemplo de resposta, retornando status 200 - OK caso tudo ocorra bem:

```json
{
  "id": "4807bb8c-2dd1-4236-8f96-eae16df96b0b",
  "frequency": "Uma vez ao dia",
  "description": "tabaco orgânico"
}
```

## GET - user/drug

Essa rota é para obtenção das informações sobre dogras. Não é necessário enviar corpo de requisição, somente o token jwt.

Exemplo de resposta, com status 200 - OK caso esteja tudo correto:

```json
{
  "id": "4807bb8c-2dd1-4236-8f96-eae16df96b0b",
  "frequency": "Uma vez ao dia",
  "description": "tabaco orgânico"
}
```

## DELETE user/drug

Essa rota é para deletar as informações. Não é necessário enviar corpo de requisição, somente o token. Não será retornado corpo, somente status 204 se estiver tudo correto.

# User Smoker

## POST - user/smoker

Essa rota é para que o fumante possa decrever seus hábitos com mais detalhes se quiser. Os campos requeridos são frequency e description, sendo description opcional.

Exemplo de requisição:

```json
{
  "frequency": "Duas vezes ao dias.",
  "description": "Cigarro de palha com cravo."
}
```

Exemplo de resposta, , retornando status 201 - CREATED caso tudo seja passado corretamente:

```json
{
  "id": "51ff0f8d-e7ff-4f72-8cd2-0f67201c8292",
  "frequency": "Duas vezes ao dias.",
  "description": "Cigarro de palha com cravo."
}
```

## PATCH - user/smoker

Essa rota é para atualizar os dados referentes as informações do usuário fumante. Deverá ser passado unicamente os campos frequency e description, não necessáriamente os dois ao mesmo tempo.

Exemplo de requisição:

```json
{
  "frequency": "5 vezes ao dias"
}
```

Exemplo de resposta - status 200 - OK

```json
{
  "id": "096c21f2-4181-49c4-a279-9de9b3d88f66",
  "frequency": "5 vezes ao dias",
  "description": "Cigarro de palha com cravo."
}
```

## GET - user/smoker

Essa rota é para visualizar as informações sobre os detalhes cadastrado na tabela smoker. Não é necessario corpo de requisição. Somente o token.

Exemplo de resposta, status 200 - OK:

```json
{
  "id": "096c21f2-4181-49c4-a279-9de9b3d88f66",
  "frequency": "5 vezes ao dias",
  "description": "Cigarro de palha com cravo."
}
```

## DELETE - user/smoker

Essa rota é para deletar as informações cadastradas na tabela smoker. Não é necessário enviar corpo de requisição, somente o token. Não será retornado corpo, somente status 204 - CONTENT

# User Physical Activity

## POST - user/physical_activity

Essa rota é para cadastro de informaçoes relacionadas a atividades fisicas. É necessário passar somente os campos frequency e description no corpo de requisição, sendo o campo description opcional.

Exemplo de requisição:

```json
{
  "frequency": "uma vez por semana",
  "description": "caminhada na praia"
}
```

Exemplo de resposta status 201 - CREATED

```json
{
  "id": "d727da29-7937-4f53-9a7e-9bd7080234e3",
  "frequency": "Uma vez por semana",
  "description": "Caminhada na praia"
}
```

## PATCH - user/physical_activity

Essa rota atualiza os dados cadastrados sobre atividades físicas. Serão aceitos somente os campos frequency e description.

Exemplo de requisição:

```json
{
  "frequency": "3x na semana",
  "description": " academia   "
}
```

Exemplo de resposta, status 200 - OK:

```json
{
  "id": "d727da29-7937-4f53-9a7e-9bd7080234e3",
  "frequency": "3x na semana",
  "description": "Academia"
}
```

## GET - user/physical_activity

Essa rota é para obter as informações cadastradas sobre atividades físicas. Não é necessário enviar corpo de requisição.

Exemplo de resposta:

```json
{
  "id": "ed5ed43e-371b-48ce-864a-aedc941e736a",
  "frequency": "3x na semana",
  "description": "Academia"
}
```

## DELETE - user/physical_activity

Essa rota é para deletar as informações cadastradas sobre atividade física. Não é necessário enviar corpo de requisição, somente o token. Será caso tudo ocorra bem, será retornado status 204 - NO CONTENT

# Address

## POST - address

Esta rota é para o cadastro do consultório do médico.
Os campos obrigatórios são: “street”, “number”, campos facultativos: "disctrict", "city", "complement"

Exemplo de requisição abaixo:

Authorization: ` Bearer Token`

```json
{
  "street": "rua blah",
  "number": 25,
  "district": "madureira",
  "city": "rio   de janeiro",
  "complement": "do lado do posto de gasolina"
}
```

Exemplo de resposta, com status 200 - OK caso esteja tudo correto:

```json
{
  "id": "71d9b03b-a27f-4f97-9145-8785b04bbb08",
  "street": "Rua Blah",
  "number": 25,
  "district": "Madureira",
  "city": "Rio De Janeiro",
  "complement": "Do lado do posto de gasolina"
}
```

## PATCH - address

Esta rota é para a atualização do consultório de um médico, podendo atualizar todos os dados

Exemplo de requisição:

Authorization: ` Bearer Token`

```json
{
  "address_id": "71d9b03b-a27f-4f97-9145-8785b04bbb08",
  "street": "Rua Bler",
  "number": 50,
  "district": "barra da tijuca",
  "city": "rio de janeiro",
  "complement": "De frente pra praia"
}
```

Exemplo de resposta, com status 200 - OK caso esteja tudo correto:

```json
{
  "id": "71d9b03b-a27f-4f97-9145-8785b04bbb08",
  "street": "Rua Bler",
  "number": 50,
  "district": "barra da tijuca",
  "city": "rio de janeiro",
  "complement": "De frente pra praia"
}
```

## DELETE - address

Esta rota é para apagar consultório existente.

Exemplo de requisição:

Authorization: ` Bearer Token`

```json
{
  "address_id": "71d9b03b-a27f-4f97-9145-8785b04bbb08"
}
```

Exemplo de resposta, com status 204 - OK caso esteja tudo correto.

# Profile image

## POST user/image-profile

Essa rota é para cadastro e upload da imagem de perfil do usuário. É necessário que o envio seja feito como multipart/form-data, sendo obrigatório o formulário ter o campo name preenchido e que uma imagem seja enviada.

Exemplo de resposta, retornando status 201-CREATED caso tudo ocorra de forma correta:

```json
{
  "id": "ir_pp-kL_730S2jwzk-n3hu_4VFIT_PAXjrpw5XZzMnHEuZPuUriNAMKTOtcNq6FGLiqHm8lTu_QAckAq6Y_mA",
  "name": "Frutas",
  "url": "https://my_bucket.s3.nu-rtrg9.amazonaws.com/ir_pp-kL_730S2jwzk-n3hu_4EuZPuUriNAMKTOtcNq6FGLiqHm8lTu_QAckAq6Y_mA"
}
```

## GET user/image-profile

Essa rota é para verificar os dados da imagem de perfil. Não há necessidade de corpo de requisição, somente o token precisa ser enviado.

Exemplo de resposta, retornando status 200 - OK caso tudo ocorra bem:

```json
{
  "id": "ir_pp-kL_730S2jwzk-n3hu_4VFIT_PAXjrpw5XZzMnHEuZPuUriNAMKTOtcNq6FGLiqHm8lTu_QAckAq6Y_mA",
  "name": "Frutas",
  "url": "https://my-bucket.s3.wyaffs.amazonaws.com/5XZzMnHEuZPuUriNAMKTOtcNq6FGLiqHm8lTu_QAckAq6Y_mA"
}
```

## DELETE - user/image-profile

Essa rota é para deletar a imagem de perfil do usuário. Não é necessário corpo de requisição, somente o token.

Caso tudo ocorra bem, será retornado status 204 - NO CONTENT.

# Exam Files

## POST - user/exam/file/<exam_id>

Essa rota é para upload e cadastro do documento de exame. É necessário passar o id do exame no final da rota. É aceito somente imagens(png, jpg e jpeg) e pdf. Deverá ser enviado por formulário multipart/form-data com o campo name preenchido.

Exemplo de resposta, retornando status 201 - CREATED caso tudo ocorra bem:

```json
{
  "success": "https://my-bucket.s3.wdsvvc.amazonaws.com/fE45VCFnI4sB8l4vsVh1ffXiVwAng9UkqwoiETodwCxJ0Drml9KMGS5FznSJ55aaHZ"
}
```

## DELETE - user/exam/file/<exam_id>

Essa rota é para deletar o documento. É necessário passar somente o id do exame que contém o documento no final da rota e o token. Será retornado status 204 - NO CONTENT caso tudo ocorra bem.

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
  "id": "16770b6a-70c7-40ed-88d5-a237dcb5dfd0",
  "name": "Camarão"
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
  "id": "dffa762a-05cd-4bb1-a52c-0d4506d69d15",
  "description": "Alergia grave a frutos do mar",
  "name": "Frutos Do Mar"
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
  "name": "Cachorro"
  }
}
```

## DELETE - /user/allergy/<int:allergy_id

Esta rota é para deletar uma das alergias do usuário. Para realizar a deleção é somente necessário passar o id da alergia do usuário por query params.

Authorization: ` Bearer Token`

#
# Anamnesis 

## POST - /user/anamnesis
Esta rota é para criação de anamnesis relacionada ao usuário. A seguir os campos obrigatórios:  'diseases', 'allergy','continous_medication', 'surgery', 'alcoholic','drug_user', 'smoker', 'physical_activity', 'diabetes', 'hipertension'

Authorization: ` Bearer Token`

Segue abaixo o exemplo de requisição:

```json

{  
  "diseases":true,
  "allergy":true,
  "continous_medication":true,
  "surgery":false,
  "alcoholic":true,
  "drug_user":false,
  "smoker":true,
  "physical_activity":false,
  "diabetes":false,
  "hipertension":true
}

```

Caso tudo dê certo irá retornar o código 201 e uma resposta similar a esta abaixo:

```json
{
  "id": "117b8a38-4c59-4149-911f-e3f42fa5c7f3",
  "diseases": true,
  "allergy": true,
  "continous_medication": true,
  "surgery": false,
  "alcoholic": true,
  "drug_user": false,
  "smoker": true,
  "physical_activity": false,
  "diabetes": false,
  "hipertension": true
}
```



## PATCH - /user/anamnesis
Esta rota é para atualização da anamnesis do usuário todos os campos podem ser atualizados, caso dê tudo certo irá retornar 204.

Authorization: ` Bearer Token`


## GET - /user/anamnesis
Esta rota é para pegar a anamnesis relacionada ao usuário, caso dê tudo certo irá retornar a anamnesis do usuário, como mostrado no exemplo abaixo:
Authorization: ` Bearer Token`

```json
{
  "id": "117b8a38-4c59-4149-911f-e3f42fa5c7f3",
  "diseases": true,
  "allergy": true,
  "continous_medication": true,
  "surgery": false,
  "alcoholic": true,
  "drug_user": false,
  "smoker": true,
  "physical_activity": false,
  "diabetes": false,
  "hipertension": true
}
```