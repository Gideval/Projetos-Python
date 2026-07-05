# ViaCEP API - Estudos com FastAPI

## 📖 Sobre o projeto

Este projeto foi desenvolvido com o objetivo de **fixar os conceitos de desenvolvimento de APIs em Python utilizando FastAPI**, aplicando uma arquitetura organizada e inspirada em projetos profissionais.

A aplicação consome a API pública do **ViaCEP**, permitindo consultar endereços por CEP ou realizar buscas por UF, cidade e logradouro.

O foco principal não é apenas consumir uma API externa, mas praticar boas práticas de desenvolvimento, separação de responsabilidades e organização do código.

---

## 🎯 Objetivos de aprendizado

Durante o desenvolvimento deste projeto foram praticados conceitos como:

- Desenvolvimento de APIs REST com FastAPI;
- Organização do projeto em camadas;
- Injeção de dependência (`Depends`);
- Consumo de APIs externas utilizando `httpx`;
- Programação assíncrona (`async`/`await`);
- Modelagem de dados com Pydantic;
- Tratamento de exceções;
- Validação de parâmetros;
- Separação entre regras de negócio e acesso a serviços externos.

---

## 🏛️ Arquitetura

O projeto foi estruturado seguindo o princípio de **separação de responsabilidades**, onde cada camada possui uma função específica.

```text
Cliente
    │
    ▼
Router
    │
    ▼
Service
    │
    ▼
Facade
    │
    ▼
ViaCEP API
```

### Router

Responsável por expor os endpoints da aplicação e receber as requisições HTTP.

### Service

Contém as regras de negócio da aplicação e orquestra a comunicação entre as demais camadas.

### Facade

Responsável pelo consumo da API pública do ViaCEP utilizando `httpx`.

### Models

Representam os objetos utilizados pela aplicação, permitindo trabalhar com dados tipados através do Pydantic.

---

## 📂 Estrutura do projeto

```text
app/
│
├── facades/
│   └── viacep_api_facade.py
│
├── models/
│   └── responses/
│       └── viacep_api_response.py
│
├── routers/
│   └── viacep_api_router.py
│
├── services/
│   └── viacep_api_service.py
│
└── main.py
```

---

## 🚀 Endpoints

### Buscar endereço por CEP

```http
GET /viacep/cep/{zip_code}
```

Exemplo:

```http
GET /viacep/cep/01001000
```

---

### Buscar endereço por UF, cidade e logradouro

```http
GET /viacep/address
```

Parâmetros:

| Parâmetro | Descrição |
|-----------|-----------|
| `uf` | Unidade Federativa |
| `city` | Cidade |
| `street` | Logradouro |

Exemplo:

```http
GET /viacep/address?uf=SE&city=Aracaju&street=Avenida Beira Mar
```

---

## 🛠️ Tecnologias utilizadas

- Python
- FastAPI
- Pydantic
- HTTPX
- Uvicorn

---

## 📚 API utilizada

Este projeto utiliza a API pública do ViaCEP para consulta de endereços.

https://viacep.com.br/

---

## 💡 Finalidade

Este projeto faz parte da minha jornada de aprendizado em desenvolvimento de APIs com Python.

O objetivo é evoluir gradualmente, aplicando conceitos utilizados em aplicações profissionais, como arquitetura em camadas, organização do código, boas práticas de desenvolvimento e consumo de serviços externos.

Assim como meu projeto anterior utilizando a PokéAPI, este repositório foi desenvolvido com foco no aprendizado, buscando consolidar conhecimentos que poderão ser aplicados em projetos maiores e em ambientes corporativos.