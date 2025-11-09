from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("HelperBot")
trainer = ListTrainer(chatbot)

trainer.train([
    "Hi",
    "Hello! How can I help you?",
    "What is your name?",
    "I am HelperBot created for customer support.",
    "Bye",
    "Goodbye! Have a nice day!"
])

while True:
    query = input("You: ")
    if query.lower() == 'exit':
        break
    reply = chatbot.get_response(query)
    print("Bot:", reply)

#pip install chatterbot
#python -m spacy download en_core_web_sm