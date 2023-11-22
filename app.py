from flask import Flask, redirect, request, render_template 
import pickle
import numpy as np

app=Flask(__name__)

@app.route("/")

def fun1():

    return render_template("info.html")

@app.route("/predict", methods = ["post"])

def fun2():
    age = float(request.form['age'])
    sex = float(request.form['sex'])
    bmi = float(request.form['bmi'])
    children = float(request.form['children'])
    smoker = float(request.form['smoker'])
    region = float(request.form['region'])
    mymodel = pickle.load(open('health_model.pkl', "rb"))
    premium = round(mymodel.predict([[age, sex, bmi, children, smoker, region]])[0],2)
    #return "<h1> Hi <br/> your predicted Premium is {} </h1>".format(premium)

    return render_template("second.html",  premium=premium)

if __name__=="__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)
