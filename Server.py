from flask import Flask
app = Flask(__name__)

@app.routo("/", methods = ["GET"])
def index():
    return "Cargador"

if __name__ == "__main__":
    app.run()
