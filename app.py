from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/med')
def med():
    return render_template('med.html')
#
# @app.route('/surg')
# def surg():
#     return render_template('surg.html')
#
# @app.route('/ped')
# def ped():
#     return render_template('ped.html')
#
# @app.route('/obs')
# def obs():
#     return render_template('obs.html')
#
# @app.route('/other')
# def other():
#     return render_template('other.html')

if __name__ == '__main__':
    app.run()
