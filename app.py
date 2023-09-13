from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "**** Geisenheim in der Cloud...als App ****"
