from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html'), 200

@app.route('/structure', methods = ['GET'])
def structure():
    return render_template('structure.html'), 200

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html'), 200

if __name__ == '__main__':
    app.run(port= 5000, debug= True)