from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from langchain import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI


app = Flask(__name__, template_folder='templates')
CORS(app)

# Create a prompt template with instruction for short replies
template = """You are a helpful medical chatbot.
{history}
User: {input}
Bot:"""
prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=template
)

# Configure Gemini
gemini = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key="AIzaSyB-BAXi1UFXd1ofAo65T2QNUt7d5pVhk_k")
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(
    llm=gemini,
    memory=memory,
    prompt=prompt,
    verbose=True
)

@app.route("/")
def index():
    return render_template("index.html")  # Render the HTML page

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = conversation.predict(input=user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
