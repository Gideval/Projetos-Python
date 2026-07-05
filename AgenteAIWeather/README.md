# 🌦️ Weather AI Assistant

Um assistente de IA desenvolvido em Python utilizando **LangChain** e **Google Gemini**, capaz de conversar naturalmente com o usuário e consultar uma API de previsão do tempo desenvolvida com **FastAPI** e **Open-Meteo**.

O objetivo deste projeto é demonstrar a integração entre um **LLM (Large Language Model)** e uma **API REST**, utilizando a arquitetura moderna do LangChain baseada em **Agents** e **Tools**.

---

## 🚀 Funcionalidades

- 🤖 Conversa natural com o usuário utilizando Google Gemini.
- 🛠️ Utilização de **Tools** do LangChain.
- 🌦️ Consulta de dados meteorológicos através de uma API própria.
- 📄 Prompts armazenados em arquivos `.txt`.
- 🔐 Configuração segura utilizando `.env`.
- 🏗️ Projeto organizado em camadas.
- 💬 Interface interativa via terminal.

---

## 📸 Exemplo de uso

```text
==================================================
Weather Assistant
==================================================

Você: Olá

IA:
Olá! Seja bem-vindo!
Posso ajudá-lo com informações sobre o clima de qualquer cidade.

Você:
Como está o tempo em Aracaju?

IA:
Neste momento em Aracaju:

🌡️ Temperatura: 24.7 °C
💧 Umidade: 76%
🌬️ Velocidade do vento: 10.4 km/h

Com essas condições, o clima está agradável para atividades ao ar livre.
```

---

# 🏛️ Arquitetura

```
Usuário
    │
    ▼
LangChain Agent
    │
    ├───────────────┐
    ▼               │
Google Gemini       │
    │               │
    ▼               │
Weather Tool (@tool)
    │
    ▼
Weather Service
    │
    ▼
FastAPI Weather API
    │
    ▼
Open-Meteo API
```

---

# 📁 Estrutura do Projeto

```text
AgenteAIWeather/

│
├── app/
│   ├── ai/
│   │   ├── agent.py
│   │   ├── gemini.py
│   │   ├── prompt_loader.py
│   │   └── prompts/
│   │       └── weather_agent.txt
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   ├── services/
│   │   └── weather_service.py
│   │
│   ├── tools/
│   │   └── weather_tool.py
│   │
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🛠️ Tecnologias utilizadas

- Python 3.14
- LangChain 1.x
- Google Gemini
- FastAPI
- Requests
- Python Dotenv
- Open Meteo API

---

# ⚙️ Configuração

## 1. Clone o projeto

```bash
git clone https://github.com/seu-usuario/AgenteAIWeather.git
```

Entre na pasta:

```bash
cd AgenteAIWeather
```

---

## 2. Crie um ambiente virtual

Windows

```bash
python -m venv .venv
```

Linux / macOS

```bash
python3 -m venv .venv
```

---

## 3. Ative o ambiente

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 5. Configure o arquivo `.env`

```env
GOOGLE_API_KEY=SUA_CHAVE

WEATHER_API=http://127.0.0.1:8000/clima/tempo/weather/
```

---

# ▶️ Executando

Primeiro execute a API de clima.

Depois execute o assistente:

```bash
python app/main.py
```

---

# 🧠 Como funciona

1. O usuário envia uma mensagem.
2. O Agent interpreta a intenção.
3. Caso seja necessário consultar informações meteorológicas, o Agent utiliza automaticamente a Tool `get_weather`.
4. A Tool chama o `WeatherService`.
5. O serviço consome a API desenvolvida com FastAPI.
6. Os dados retornam ao Gemini.
7. O Gemini gera uma resposta natural para o usuário.

---

# 🛠️ Tool utilizada

O projeto utiliza uma Tool do LangChain para acessar a API de clima.

```python
@tool
def get_weather(city: str):
    ...
```

O Agent decide automaticamente quando utilizar essa ferramenta.

---

# 📄 Prompt Externo

O comportamento do agente não está definido diretamente no código.

O prompt é carregado dinamicamente a partir de um arquivo:

```text
app/ai/prompts/weather_agent.txt
```

Isso facilita alterações de comportamento sem necessidade de modificar o código Python.

---

# 📚 Conceitos aplicados

- LangChain Agents
- LangChain Tools
- Prompt Engineering
- LLM (Google Gemini)
- REST API
- Arquitetura em Camadas
- Injeção de Configuração (.env)
- Organização de Projeto
- Engenharia de Prompts

---

# 🚀 Melhorias futuras

- Memória da conversa.
- Histórico de mensagens.
- Suporte para previsão dos próximos dias.
- Interface Web com FastAPI.
- Interface gráfica utilizando Streamlit.
- Múltiplas Tools (clima, notícias, câmbio, etc.).
- Docker.
- Testes automatizados.
- Logging estruturado.

---

# 👨‍💻 Autor

Desenvolvido por **Gideval Santos** como projeto de estudos sobre **Python**, **Inteligência Artificial**, **LangChain** e **Google Gemini**.