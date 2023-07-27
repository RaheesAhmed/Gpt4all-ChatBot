# GPT4All Chatbot Web App

The GPT4All Chatbot Web App allows users to interact with a chatbot powered by the GPT4All language model. Users can input messages into the chat interface, and the chatbot will generate responses based on the provided prompts using the GPT4All model.

## Requirements

To run the web app locally, you will need the following:

- Python 3.6 or higher
- Flask (install using `pip install Flask`)
- GPT4All Python package (install using `pip install gpt4all`)
- A modern web browser to interact with the web app

## Installation and Usage

1. Clone the repository to your local machine:

```bash
   git clone https://github.com/RaheesAhmed/Gpt4all-ChatBot.git

2. Install the required Python packages:

```bash
   pip install Flask gpt4all

Start the web app:
```bash
   python main.py

Access the web app in your web browser:
Open your web browser and go to http://127.0.0.1:5000/ to access the chat interface. You can now chat with the GPT4All-powered chatbot.

## How it Works
The web app is built using the Flask web framework and interacts with the GPT4All language model to generate responses. When you input a message in the chat interface and click "Send," the message is sent to the Flask server as an HTTP POST request. The server then uses the GPT4All model to generate a response, which is sent back to the web page and displayed in the chat interface.

## Model Selection
The web app uses the GPT4All language model with the following specifications:

Model Name: orca-mini-3b.ggmlv3.q4_0.bin
You can replace the model file with your own GPT4All model if desired. Make sure to update the model = GPT4All("path_to_your_model") line in the app.py file accordingly.

## Contributions
Contributions to the web app are welcome! If you find any bugs or have ideas for improvements, feel free to open an issue or submit a pull request.

## License
This web app is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
The GPT4All Python package and language model used in this web app are developed by the GPT4All project (insert link to the GPT4All project if available).
## Disclaimer
This web app is meant for demonstration purposes and may not be suitable for production use without further development and consideration of security and scalability aspects.
