from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify(message="This is Sims Library project!!")

if __name__ == '__main__':
    app.run()