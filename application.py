from flask import Flask, request, app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd


application = Flask(__name__)
app=application

model = pickle.load(open("models/modelForPrediction.pkl", "rb"))


## Route for Single data point prediction
@app.route('/',methods=['GET','POST'])
def predict_datapoint():
    result=""

    if request.method=='POST':
        
        amount=float(request.form.get("amount"))
        latitude = float(request.form.get('latitude'))
        longitude = float(request.form.get('longitude'))
        cityPopulation = int(request.form.get('cityPopulation'))
        hour = int(request.form.get('hour'))
        miniute = int(request.form.get('miniute'))
        seconds = int(request.form.get('seconds'))
        year = int(request.form.get('year'))
        month = int(request.form.get('month'))
        day = int(request.form.get('day'))
        new_data=[[amount,latitude,longitude,cityPopulation,hour,miniute,seconds,year,month,day]]
        predict=model.predict(new_data)
        
        print(predict)
        if predict[0] == 1 :
            result = 'Fraud'
        else:
            result ='Not Fraud'
            
        return render_template('home.html',result=result)

    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0" , debug=True)
