from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Chamado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200))

@app.route("/")
def index():
    return "API Online"

if __name__ == "__main__":
    app.run(debug=True)
