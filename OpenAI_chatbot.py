from openai import OpenAI

API_KEY = "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"

client = OpenAI(
    api_key = API_KEY
)

history = []

def ask(question):
    question_msg = {
        "role": "user",
        "content": question
    }

    history.append(question_msg)
    response = client.chat.completions.create(
        messages= history,
        model = "gpt-3.5-turbo"
    )

    answer_msg = response.choices[0].message
    history.append(answer_msg)
    return answer_msg.content

while(True):
    question = input("You: ")

    if(question.strip() == ''):
        break

    answer = ask(question)
    print('\n')
    print(f'bot: {answer}')
    print('\n')