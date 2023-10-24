# app.py

from flask import Flask, render_template, request, jsonify
import openai
import pyttsx3

app = Flask(__name__)

# Initialize chat history as an empty list
chat_history = []

# Set up OpenAI API credentials (Uncomment and add your API key)
openai.api_key = 'xxxxx'

    

@app.route('/')
def index():
    response_text = "I'm not available right now. I will contact you soon."
    return render_template('index.html', chat_history=chat_history, success=True, response=response_text)

@app.route('/process_message', methods=['POST'])
def process_message():
    engine = pyttsx3.init()
    user_input = request.form['user_input'].strip()  # Remove leading/trailing whitespace
    chat_history.append({'role': 'user', 'message': user_input})

    if openai.api_key is None:
        # If API key is not attached, respond with the default message
        bot_response = "Hi! This is Hassan. I'm not available right now. I will contact you soon." 
    else:
        # Process the user's message using OpenAI GPT-3.5
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=50
        )

        bot_response = completion['choices'][0]['message']['content']
        engine.say(bot_response)
        engine.runAndWait()
        
    chat_history.append({'role': 'bot', 'message': bot_response})

    # Generate the voice for the response after setting the bot_response
   
        

    
    
    
    
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)