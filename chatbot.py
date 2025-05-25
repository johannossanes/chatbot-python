import google.generativeai as genai

genai.configure(api_key=" ")

model = genai.GenerativeModel("gemini-1.5-flash")  


def chatbot(prompt):
    response = model.generate_content(prompt)
    return response.text

print("Bem-vindo ao chatbot! Digite 'sair' para encerrar.")

while True:

    user_input = input("Você: ")

    if user_input == 'sair'.lower():
        print('Até logo e até a próxima!')
        break

    response = chatbot(user_input)
    print(f'Chat: `{response}')