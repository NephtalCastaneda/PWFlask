from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hola Mundo realizado con Flask ejecutado en Render"
