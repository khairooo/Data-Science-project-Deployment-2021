from flask import Flask, render_template, request, jsonify
import requests
import jsonify
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('final_prediction.pickle', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    support_type_website=0
    if request.method == 'POST':
        device_model_iphone = 0
        support_type_website = 0
        bidfloor = float(request.form['bidfloor'])
        won_price=float(request.form['won_price'])
        verticals_0=int(request.form['verticals_0'])
        verticals_1=int(request.form['verticals_1'])
        verticals_2=float(request.form['verticals_2'])
        vertical_3=int(request.form['vertical_3'])
        bid_price=float(request.form['bid_price'])
        
        support_type_app=request.form['support_type_app']
        if(support_type_app =='app'):
            support_type_app=1
            support_type_website=0
        else:
            support_type_app=0
            support_type_website=1
        

        device_model_ipod=request.form['device_model_ipod']

        if(device_model_ipod=='ipod'):
            device_model_ipod=1
            device_model_iphone=0
        else:
            device_model_iphone=1
            device_model_ipod=0

        prediction=model.predict([[bidfloor,won_price,verticals_0,verticals_1,verticals_2,vertical_3,bid_price,support_type_app,support_type_website,device_model_iphone,device_model_ipod]])
        output= prediction[0]
        if output == 0:
            return render_template('index.html',prediction_texts="doesn't omitted on purpose : {} ".format(output))
        else:
            return render_template('index.html',prediction_text="omitted on purpose : {} ".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)