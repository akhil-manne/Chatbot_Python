import openai

openai.api_key = "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"
# Make sure to go to the openAI website and secure a new secret API key. The above key has been revoked.

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
