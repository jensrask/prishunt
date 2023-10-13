from flask import Flask, request, jsonify, make_response, render_template
import openai

def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

app = Flask(__name__)
app.after_request(add_cors_headers)

@app.route('/')
def index():
    return render_template('index.html')

openai.api_key = "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"

@app.route('/ask', methods=['POST'])
def ask():
    print("Request data type:", type(request.data))  # Debug line
    print("Request data:", request.data.decode("utf-8"))  # Debug line
    user_message = request.json['message']
    print("User message:", user_message)  # Debug line
    response = openai.Completion.create(
    engine="text-davinci-002",  # Update this to a non-deprecated version if needed
    prompt=f"User says: {user_message}. How should I respond?",
    max_tokens=100
)

    print("API Response:", response)  # Debug line
    bot_message = response.choices[0].text.strip()
    print("Bot message:", bot_message)  # Debug line
    return jsonify({'message': bot_message})

if __name__ == '__main__':
    app.run()
