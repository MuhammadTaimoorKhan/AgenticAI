from flask import Flask, redirect,url_for
app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to my youtube channel"

@app.route('/success/<int:score>')
def success(score):
    return 'Thr person has passed and the marks is '+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'Thr pereson has failed and thr marks is '+str(score)

@app.route('/result/<int:marks>')
def result(marks):
    
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result,score=marks))



if __name__=='__main__':
    app.run(debug=True)