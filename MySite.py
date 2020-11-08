from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html', message="aloha")
    else:
        username = request.form['username']
        password = request.form['password']
        if username == "Jon" and password == "Kelly":
            message = model.my_name('Jon')
            return render_template('index.html', message=message)
        else:
            error_message= "Hint: It's you."
            return render_template("index.html", message= error_message)
@app.route('/structure', methods = ['GET'])
def structure():
    return render_template('structure.html'), 200

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html'), 200

@app.route('/terms', methods = ['GET'])
def terms():
    return render_template('terms.html'), 200

@app.route('/privacy', methods = ['GET'])
def privacy():
    return render_template('privacy.html'), 200

if __name__ == '__main__':
    app.run(port= 5000, debug= True)