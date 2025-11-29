from flask import Flask
from src.dices_route import dices_bp

app = Flask(__name__)

app.register_blueprint(dices_bp)

@app.get("/")
def home():
    return "Olá, Flask está rodando!"

if __name__ == "__main__":
    app.run(debug=True)