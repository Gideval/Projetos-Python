from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError
from app.ai.agent import agent

print("=" * 50)
print("Weather Assistant")
print("=" * 50)

while True:

    message = input("Você: ")

    if message.lower() == "sair":
        break

    try:
        response = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            }
        )

        print("\nIA:")
        print(response["messages"][-1].content)
        print()

    except ChatGoogleGenerativeAIError as e:
        print("\nErro ao consultar o Gemini.")
        print("O limite de uso da API foi atingido. Aguarde alguns instantes e tente novamente.")