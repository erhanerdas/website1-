from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/accueil')
def accueil():
    return render_template('accueil.html')

@app.route('/nosprix')
def nosprix():
    return render_template('nosprix.html')

@app.route('/notreequipe')
def notreequipe():
    return render_template('notreequipe.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

app.run(host='0.0.0.0', port=81)