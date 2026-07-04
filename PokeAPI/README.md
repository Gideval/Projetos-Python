# 📦 API Pokémon com FastAPI

## 📖 Sobre o projeto

Esta API foi desenvolvida com o objetivo de consolidar meus conhecimentos no desenvolvimento de APIs utilizando **FastAPI**, aplicando uma arquitetura estruturada e organizada baseada na separação de responsabilidades.

Em vez de concentrar toda a lógica em um único arquivo, o projeto foi dividido em camadas, tornando o código mais limpo, reutilizável e de fácil manutenção, seguindo práticas comuns em projetos profissionais.

A API consome dados da **PokeAPI** e disponibiliza um endpoint que retorna informações simplificadas de um Pokémon, demonstrando como integrar serviços externos e organizar a aplicação de forma escalável.

---

## 🚀 Tecnologias utilizadas

- Python 3
- FastAPI
- HTTPX
- PokeAPI

---

## 🏛️ Arquitetura

O projeto foi dividido nas seguintes camadas:

### Router
Responsável por receber as requisições HTTP, definir os endpoints da API e encaminhar as chamadas para a camada de serviço.

### Service
Contém a regra de negócio da aplicação, sendo responsável por processar e formatar os dados retornados pela PokeAPI antes de enviá-los ao cliente.

### Facade
Centraliza toda a comunicação com a API externa (PokeAPI), isolando a lógica de consumo de serviços externos do restante da aplicação.

### Main
Ponto de entrada da aplicação, responsável por inicializar o FastAPI e registrar as rotas.

---

## 🔄 Fluxo da requisição

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
PokeAPI
    │
    ▲
Facade
    │
    ▲
Service
    │
    ▲
Router
    │
    ▼
Cliente
```

---

## 📌 Endpoint

### Buscar um Pokémon

```http
GET /pokemon/{name}
```

### Exemplo

```http
GET /pokemon/pikachu
```

### Resposta

```json
{
    "name": "Pikachu",
    "id": 25,
    "abilities": [
        "static",
        "lightning-rod"
    ]
}
```

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido como parte do meu processo de aprendizado para praticar:

- Estruturação de APIs com FastAPI;
- Organização do código em camadas;
- Consumo de APIs externas utilizando HTTPX;
- Programação assíncrona (`async/await`);
- Tratamento de exceções;
- Injeção de dependências com `Depends`;
- Boas práticas de organização e manutenção de projetos Python.

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto foi possível compreender melhor conceitos importantes como:

- Separação de responsabilidades (Separation of Concerns);
- Arquitetura em camadas;
- Facade Pattern;
- Dependency Injection;
- Desenvolvimento de APIs REST;
- Consumo de serviços externos;
- Código limpo e reutilizável.

---

## 📄 Licença

Este projeto foi desenvolvido para fins de estudo e prática utilizando a PokeAPI como fonte de dados.