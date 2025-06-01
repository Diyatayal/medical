from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('trial.html')  # Or 'trial.html' if that's your main page

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

# Optional: health assistance if you link to it
@app.route('/health-assistance')
def health_assistance():
    return render_template('index.html')
# Run the app
if __name__ == '__main__':
    app.run(debug=True)