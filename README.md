# Rotas públicas

## POST - /register

Esta rota é para o registro de usuários. Os campos necessários são os seguintes:

Campos obrigatórios: “name”, “email”, “birth_date”, “password”, “gender”.

Exemplo de requisição abaixo:

`{`

`“name”:”Matheuzin”,`

`“email”:”matheuszin@maioral.com”,` 

`“birth_date”: “27/12/20”,`

`“password”: ”1234567”,`

`“image”: “https://matheuszin.png”`,

`“gender”:”Outros”,`

`}` 

## POST - /login

Esta rota é para o usuário fazer o login. Os campos obrigatórios são os seguintes: “email”, “senha”

Exemplo de requisição abaixo:

`{`

`“email”:”matheuszin@maioral.com”,` 

`“password”: ”1234567”,`

`}` 

# Rotas privadas

---

# Anamnesis

## POST - /user/anamnesis

Esta rota é para o cadastro da anamnese(triagem/histórico) do usuário

Os campos obrigatórios são os seguintes: “allergy”, “diabates”, “hipertension”, “continous_medication”, “smoker”,”drug_user”, “alcoholic”, “physical_activity”, “surgery”

`{` 

`“allergy”:true,`

`“diabates”:false,` 

`“hipertension”:true,`

`“continous_medication”:false,`

`“smoker”:true,`

`”drug_user”:false,`

`“alcoholic”:TRUE,`

`“physical_activity”:true,`

`“surgery”: false`

`}`

## PATCH - /user/anamnesis

Esta rota é para a atualização  da anamnese(triagem/histórico) do usuário

Não há campos obrigatórios, todos os atributos podem ser alterados com exceção do user_id.

Exemplo de requisição abaixo:

`{` 

`“allergy”:true,`

`“diabates”:false,` 

`}`

---

# Exams

## POST - user/exams

Esta rota é para o cadastro de exames relacionados ao usuário. Os campos obrigatórios são:  “name”, “date”, caso o o nome do exame enviado já exista ele irá buscar na base de dados, caso não exista, irá cadastrar um novo exame

Exemplo de requisição abaixo:

`{`

`“date”: “22/02/2022",`

`“name”: “hemograma",`

`}`

Retorno esperado : 

`{
"id": "902c7b3a-9104-4b12-8161-5c54c6a2209c",
"user_id": "ffab9d18-35aa-4ea1-a326-42b25fc94c74",
"exam_id": "897486ef-cbc9-4d90-b7bd-ded29012671e",
"exam_details_id": "5a1f45f4-48f1-429e-9523-38490c7dd96d"
}`

`{
"id": "1",
"user_id": "2",
"exam_id": "3",
"exam_details_id": "1"
}`

## PATCH - user/exams/<int:exam_id>

Esta rota é para a atualização dos exames do usuário, podendo atualizar somente a “date”,”description” e a “upload_img” do exame

Exemplo de requisição:

`{`

`“date”:21/01/2021,`

`“upload_img”: “matheus_pic_profile.png",`

`“description”: “Descrição maneira”`

`}`

## DELETE - user/exams/<int:exam_id

Esta rota é para apagar um exame do usuário. Para realizar a deleção é somente necessário passar o exam_id por query params.

## POST - /exam

Esta rota é para a criação de novos exames não existentes no banco de dados

Para a criação de um novo exame é somente necessário os seguinte campo: “name”

Exemplo de requisição:

`{`

`“name”: “Hemograma”,`

`“description”:”Exame de sangue completo”`

`}`

---

## POST - user/diseases

Esta rota é para o cadastro de doenças  relacionados ao usuário. Sendo obrigatório somente o campo “name”

Exemplo de requisição abaixo:

{
"name":"Gripe",
"description":"gripe forte",
"medication": "paracetamol"
}

## PATCH - user/diseases/<int:user_disease_id>

Esta rota é para a atualização das doenças  do usuário, podendo atualizar somente a “description” e ”medication” 

Exemplo de requisição:

`{`

`“description”:"Tomar 2x ao dia",`

`“medication”: “Insulina",`

`}`

## DELETE - user/diseases/<int:user_disease_id>

Esta rota é para apagar um exame do usuário. Para realizar a deleção é somente necessário passar o disease_id por query params.

## POST - user/user_medication

Esta rota é para o cadastro de medicações relacionados ao usuário. Os campos obrigatórios são: “user_id”, “medication_id” e “medication_detail_id”

Exemplo de requisição abaixo:

`{`

`“user_id”:10,`

 `“medication_id”: 2,`

`“medication_detail_id”:5` 

`}`

## PATCH - user/user_medication/<int:user_medication_id>

Esta rota é para a atualização das medicações do usuário, podendo atualizar somente a ”medication” 

Exemplo de requisição:

`{`

`“medication”: “Insulina",`

`}`

## DELETE - user/user_medication/<int:user_medication_id>

Esta rota é para apagar uma medicação de um usuário. Para realizar a deleção é somente necessário passar o medication_id por query params.

## POST - /medication

Esta rota é para a criação de novas medicações não existentes no banco de dados

Para a criação de uma nova medicação é somente necessário o seguinte campo: “name”

Exemplo de requisição:

`{`

`“name”: “Dramin”`

`}`

---

## POST - user/user_surgery

Esta rota é para o cadastro de cirurgias relacionados ao usuário. Os campos obrigatórios são: “user_id”, “surgery_id” e “surgery_detail_id”

Exemplo de requisição abaixo:

`{`

`“user_id”:10,`

`“surgery_id”: 2,`

`“surgery_detail_id”:5` 

`}`

## PATCH - user/user_surgery/<int:user_surgery_id>

Esta rota é para a atualização das doenças  do usuário, podendo atualizar somente a    “date”,“description” 

Exemplo de requisição:

`{`

`“date”:27/07/12,`

`“description”:"Tomar 2x ao dia"`

`}`

## DELETE - user/user_surgery/<int:user_surgery_id>

Esta rota é para apagar uma cirurgia do usuário. Para realizar a deleção é somente necessário passar o surgery_id por query params.

## POST - /surgery

Esta rota é para a criação de novas alergias não existentes no banco de dados

Para a criação de uma nova alergia é somente necessário o seguinte campo: “name”

Exemplo de requisição:

`{`

`“name”: “Rinite”,`

`"description":"Alergia q me faz espirrar mt xd`

`}`

---

## POST - user/user_drug

Esta rota é para o cadastro de drogas relacionados ao usuário. Os campos obrigatórios são: “user_id”, “frequency” e “description”

Exemplo de requisição abaixo:

`{`

`“user_id”:10,`

`"frequency": "Diaria",`

`"description":"Descrição qualquer"`

`}`

## PATCH - user/user_drug/<int:user_drug_id>

Esta rota é para a atualização das medicações do usuário, podendo atualizar somente a ”description”, “name”, “frequency”

Exemplo de requisição:

`{`

`"name":"Maconha"`

`"frequency": Diaria,`

`"description":"Uso recreativo"` 

`}`

## DELETE - user/user_drug/<int:user_drug_id>

Esta rota é para apagar uma medicação de um usuário. Para realizar a deleção é somente necessário passar o drug_id por query params.

---

## POST - user/user_smoker

Esta rota é para o cadastro de drogas relacionados ao usuário. Os campos obrigatórios são: “user_id”, “frequency” e “description”

Exemplo de requisição abaixo:

`{`

`“user_id”:10,`

`"frequency": "Diaria",`

`"description":"Descrição qualquer"`

`}`

## PATCH - user/user_smoker/<int:user_smoker_id>

Esta rota é para a atualização das medicações do usuário, podendo atualizar somente a ”description”,  “frequency”

Exemplo de requisição:

`{`

`"frequency": Diaria,`

`"description":"Uso recreativo"` 

`}`

## DELETE - user/user_smoker/<int:user_smoker_id>

Esta rota é para apagar uma medicação de um usuário. Para realizar a deleção é somente necessário passar o smoker_id por query params.

---

## POST - user/user_physical_activity

Esta rota é para o cadastro de atividades fisicas relacionados ao usuário. Os campos obrigatórios são: “user_id”, “frequency” e “description”

Exemplo de requisição abaixo:

`{`

`“user_id”:10,`

`"frequency": "Diaria",`

`"description":"Descrição qualquer"`

`}`

## PATCH - user/user_physical_activity/<int:user_physical_activity_id>

Esta rota é para a atualização das medicações do usuário, podendo atualizar somente a ”description”, “frequency”

Exemplo de requisição:

`{`

`"frequency": Diaria,`

`"description":"Uso recreativo"` 

`}`

## DELETE - user/user_physical_activity/<int:user_physical_activity_id>

Esta rota é para apagar uma medicação de um usuário. Para realizar a deleção é somente necessário passar o physical_activity_id por query params.

---

## POST - user/user_alcoholic

Esta rota é para o cadastro do alcoolismo relacionados ao usuário. Os campos obrigatórios são: “user_id”, “frequency” e “description”

Exemplo de requisição abaixo:

`{`

`“user_id”:10,`

`"frequency": "Diaria",`

`"description":"Descrição qualquer"`

`}`

## PATCH - user/user_alcoholic/<int:user_alcoholic_id>

Esta rota é para a atualização das medicações do usuário, podendo atualizar somente a ”description”, “frequency”

Exemplo de requisição:

`{`

`"frequency": Diaria,`

`"description":"Uso recreativo"` 

`}`

## DELETE - user/user_alcoholic/<int:user_alcoholic_id>

Esta rota é para apagar o “alcolismo” de um usuário. Para realizar a deleção é somente necessário passar o alcoholic_id por query params.

Esta rota é para o cadastro de alergias  relacionados ao usuário. Os campos obrigatórios são: “user_id”, “allergie_id” e “allergie_detail_id”

Exemplo de requisição abaixo:

`{`

`“user_id”:10,`

`“allergie_id”: 2,`

`“allergie_detail_id”:5` 

`}`

## POST - /appointments

`{`

`“name”: “consulta ortopedista",”`
`“date”: 12/03/2022,`

`“description”: Optional description`

`“telephone”: 2199999999`

`“doctor_name”: Doutor Vieira`

`“doctor_type”: Ortopedista`

`}`

## POST - doctor

Esta rota é para o usuário cadastrar seus médicos. Os campos obrigatórios são: “name”, “type”, “email”, “phone” e “address_id”.

Exemplo de requisição abaixo:

```python
{
	"name": "John",
	"type": "endocrino",
	"email": "john@mail.com",
	"phone": "(21)98755-6523",
	"address_id": "683511fa-76d7-4293-942e-8c7ba9b3aa9f"
}
```

## GET - doctor

Esta rota é para o usuário pegar os dados de seus médicos. Não há body.

## PATCH - doctor/<int:doctor_id>

Esta rota é para a atualização os dados de um dos seus médicos, é somente necessário passar o doctor_id por query params. Podendo atualizar “name”, “type”, “email”, “phone” e “address_id” .

Exemplo de requisição:

```python
{
	"name": "Gustavo",
	"type": "ginecologista",
	"telephone": "(21)987356583"
}
```

## DELETE - doctor/<int:doctor_id>

Esta rota é para apagar um dos médicos do usuário. Para realizar a deleção é somente necessário passar o doctor_id por query params.

---

## POST - user/allergy

Esta rota é para a criação das alergias de um usuário no banco de dados

Para a criação de uma alergia é somente necessário o seguinte campo: “name” e “description”

Exemplo de requisição:

```python
{
	"name": "A amendoim",
	"description": "Alergia grave a amendoim, podendo até fechar a glote"
}
```

## GET - user/allergy

Esta rota é para a criação de novas alergias não existentes no banco de dados

Para a criação de uma nova alergia é somente necessário o seguinte campo: “name”

Exemplo de requisição:

## PATCH - user/allergy/<int:allergy_id>

Esta rota é para a atualização das doenças  do usuário, podendo atualizar somente a “description”  

Exemplo de requisição:

```python
{
	"description":
}
```

`{`

`“description”:"Tomar 2x ao dia"`

`}`

## DELETE - allergies/<int:allergie_id>

Esta rota é para apagar uma alergia do usuário. Para realizar a deleção é somente necessário passar o allergie_id por query params.

---

# User drug

## POST - user/drug

Esta rota é para o cadastro de informações relacionadas a drogas. Os campos obrigatórios são unicamente:  “frequency” e  “description”.

Exemplo de requisição abaixo:

```python
{
	"frequency": "5x ao mes",
	"description": "Tabaco orgânico"
}
```

```python
{
	"frequency": "5x ao mes",
	"description": 55
}
```

Retorno esperado : 

```python
{
	"id": "98be6255-44c6-4d46-b79d-a8ca81e8dd88",
	"user_id": "98fc5df0-a557-48d1-9c4d-8213ab06c345",
	"frequency": "5x ao mes",
	"description": "Tabaco orgânico"
}
```

## PATCH - user/drug/<drug_id>

Esta rota é para a atualização das informações sobre drogas, podendo atualizar somente a “frequency” e ”description”, qualquer outro campo passado será ignorado.  

Exemplo de requisição:

```python
{
	"frequency": "2x ao dia",
	"description": "cannabis"
}

```

Exemplo de resposta:

```python
{
	"id": "98be6255-44c6-4d46-b79d-a8ca81e8dd88",
	"user_id": "98fc5df0-a557-48d1-9c4d-8213ab06c345",
	"frequency": "2x ao dia",
	"description": "cannabis"
}
```

## DELETE - user/drug/<drug_id>

Esta rota é para a informação sobre drogas cadastrada pelo usuário. Para realizar a deleção é somente necessário passar o drug_id ao final do endpoint user/drug. Caso seja deletado com sucesso, não será retornado corpo. 

## GET - user/drug/<drug_id>

Esta rota é para obtenção de informação da drogas. É necessário somente passar o drug_id no final do endpoint user/drug

Exemplo de retorno:

```python
{
	"id": "98be6255-44c6-4d46-b79d-a8ca81e8dd88",
	"user_id": "98fc5df0-a557-48d1-9c4d-8213ab06c345",
	"frequency": "2x ao dia",
	"description": "cannabis"
}
```