from flask import Flask, jsonify
from flask_restplus import Api
app = Flask(__name__)

@app.route("/<float:nota1>/<float:nota2>", methods=["GET"])
def segundo_endpoint(nota1: float , nota2: float)-> float:
  media = nota1 + nota2/2
  message= (f"A Média do Aluno: {media}")  
  return jsonify(message)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)