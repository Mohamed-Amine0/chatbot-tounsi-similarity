from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot_weather import WeatherLogicAdapter
from cleaner import clean_corpus
from weather import get_weather
from wikipediaprocess import search_wikipedia
from newsapi import NewsApiClient


newsapi = NewsApiClient(api_key='a1d8789da28b4df282afbabff793c211')


chatbot = ChatBot("Chatbot tounsi",logic_adapters=[      {
            'import_path': 'chatterbot.logic.MathematicalEvaluation',
        },
        {'import_path': 'chatterbot.logic.BestMatch',}
        ])
CORPUS_FILE="chat2.txt"
#CORPUS_FILE2="chat.txt"
trainer = ListTrainer(chatbot)
cleaned_corpus=clean_corpus(CORPUS_FILE)
#cleaned_corpus2=clean_corpus(CORPUS_FILE2)
trainer.train(cleaned_corpus)
#trainer.train(cleaned_corpus2)



exit_conditions = (":q", "quit", "exit")
while True:
    print("*********************************************************\nbech tchouf ta9s mtaa bled ekteb : Chnowa ta9s fi + pays\nbech tchouf e5er a5bar ekteb  : e5er a5bar aala + sujet\nbecht tchouf definition mtaa 7aja ekteb : wiki +Sujet\nbech to5rej ekteb quit wala exit\n************************************************************")
    query = input("> ")
    #print(query)
    if query in exit_conditions:
        break
    elif query.startswith("chnowa ta9s fi "):
        # Get the country name from the input
        country = query.replace("chnowa ta9s fi ", "")
        # Get the weather for the country
        weather = get_weather(country)
        print(f"ta9s: {weather}")
    elif query.startswith("wiki "):
        topic=query.replace("wiki ","")
        wiki=search_wikipedia(topic)
        print(wiki)
    elif query.startswith("e5er a5bar aala "):
        theme=query.replace("e5er a5bar aala ","")
        top_headlines = newsapi.get_everything(q=theme, sort_by='relevancy',language='fr')
        for article in top_headlines['articles']:
            print(article['title'])


    else:
        print(f"🤖 {str(chatbot.get_response(query))}")