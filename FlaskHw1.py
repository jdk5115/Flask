from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    message = "<body><h1>" + 'Hello World!!!' + "</h1></body>"
    return (message), 200

if __name__ == '__main__':
    app.run(port= 8000, debug= True)