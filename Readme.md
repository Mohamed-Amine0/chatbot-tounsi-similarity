# Chatbot Tounsi

This project is a Tunisian dialect chatbot implemented in Python using the ChatterBot library.

## Files

- [chatbot.py](chatbot.py): The main chatbot script.
- [cleaner.py](cleaner.py): Contains functions for cleaning the chat corpus.
- [chatbot-Tounsi.ipynb](chatbot-Tounsi.ipynb): A Jupyter notebook version of the chatbot.


## The chatbot in chatbot-Tounsi.ipynb is created through several steps:

1. **Importing necessary modules**: Modules like `chatterbot`, `chatterbot.trainers`, `cleaner`, `weather`, `wikipediaprocess`, and `newsapi` are imported. These modules provide the functionalities for chatbot training, weather information retrieval, Wikipedia search, and news retrieval.

2. **Creating a ChatBot instance**: An instance of `ChatBot` is created with the name "Chatbot tounsi". This instance is configured with logic adapters for mathematical evaluation and best match conversation.

3. **Training the chatbot**: The chatbot is trained using a `ListTrainer` and a cleaned corpus. The corpus is cleaned using the `clean_corpus` function from the `cleaner` module.

4. **Running the chatbot**: The chatbot runs in a loop, waiting for user input. It can handle different types of queries:
   - If the query is an exit command (":q", "quit", "exit"), the loop breaks and the chatbot stops.
   - If the query starts with "chnowa ta9s fi ", the chatbot interprets it as a request for weather information. It uses the `get_weather` function from the `weather` module to retrieve the weather for the specified location.
   - If the query starts with "wiki ", the chatbot interprets it as a request for a Wikipedia search. It uses the `search_wikipedia` function from the `wikipediaprocess` module to search Wikipedia for the specified topic.

This approach allows the chatbot to provide interactive responses based on real-time weather updates and Wikipedia information.

## Setup

1. Install the required Python packages:

```sh
pip install chatterbot
pip install chatterbot_weather
pip install newsapi-python