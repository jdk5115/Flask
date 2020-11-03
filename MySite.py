from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html', message="aloha")
    else:
        username = request.form['username']
        password = request.form['password']
        if username == 'Gordon' and password == 'Ramsay':
            return render_template('index.html', message= 'Login successful')
        else:
            error_message= "Hint: He curses a lot."
            return render_template("index.html", message= error_message)
@app.route('/structure', methods = ['GET'])
def structure():
    return render_template('structure.html'), 200

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html'), 200

if __name__ == '__main__':
    app.run(port= 5000, debug= True)