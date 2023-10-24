from flask import Flask, render_template, request
import pyttsx3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_voice', methods=['POST'])
def generate_voice():
    text = request.form['text']
    
    # Generate the voice for the response
    response_text = "Hi! This is Hassan. I'm not available right now. I will contact you soon."
    generate_voice_for_text(response_text)

    return render_template('index.html', success=True, response=response_text)

def generate_voice_for_text(text):
    # Generate voice for the provided text
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    app.run(debug=True)