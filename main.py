from flask import Flask, render_template, request
from gpt4all import GPT4All

# Create a Flask app
app = Flask(__name__)

# Load the GPT4All model
model = GPT4All("orca-mini-3b.ggmlv3.q4_0.bin")

# Chat session route
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user_input']
        with model.chat_session():
            response = model.generate(prompt=user_input, top_k=1)
        return render_template('chat.html', user_input=user_input, response=response)
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)
