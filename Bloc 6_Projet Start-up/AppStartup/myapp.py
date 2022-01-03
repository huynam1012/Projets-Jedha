from flask import Flask, request, jsonify, render_template

import joblib
import numpy

app = Flask(__name__)


from datetime import datetime
from datetime import date
def calculate_age(start,end):
    start = datetime.strptime(start, "%Y-%m-%d").date()
    end = datetime.strptime(end, "%Y-%m-%d").date()
    return end.year - start.year - ((end.month, end.day) < (start.month, start.day))

def calculate_diff_date(start,end):
    print("start in calculate diff",start)
    print("end in calculate diff",end)
    start = datetime.strptime(start, "%Y-%m-%d").date()
    end = datetime.strptime(end, "%Y-%m-%d").date()
    return (end - start).days


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Check if request has a JSON content
    if request.json:
        # Get the JSON as dictionnary
        req = request.get_json()
        # Check mandatory key
        if "input" in req.keys():
            # Load model
            classifier = joblib.load("lr.joblib")
            scaler = joblib.load("sc_x.joblib")
            # Predict
            print("befor numpy",req["input"])
            data= req["input"]
            print("dattatata",data[0])
            #df1['funding_day'] = (df1['first_funding_at'] - df1['founded_at'])/np.timedelta64(1,'D')
            #df1['funding_range_1_2'] = (df1['last_funding_at'] - df1['first_funding_at'])/np.timedelta64(1,'D')
                        
            ####requests
            #in =>df4[["funding_total_usd",  "funding_rounds", "founded_at",   "first_funding_at", "last_funding_at"]]
            #out =>df4[["funding_total_usd", "funding_rounds", "company_age", "funding_day",      "funding_range_1_2"]]
            for i in data:
                print("i",i)
                #geting the values of inputs 
                founded_at= str(i[2])
                first_funding_at=str(i[3])
                last_funding_at= str(i[4])
                i[2]=calculate_age(founded_at,str(date.today()))
                #print(f"i[2] after =====>{i[2]}<======")
                first_funding_at=i[3]
                i[3]=calculate_diff_date(founded_at,first_funding_at)
                i[4]=calculate_diff_date(first_funding_at,last_funding_at)               
           
            
            X=scaler.transform(data)
            print("x",X)            
            prediction = classifier.predict(X)
            # Return the result as JSON but first we need to transform the
            # result so as to be serializable by jsonify()
            prediction = str(prediction).replace(" ",",")
            #print(prediction)
            return jsonify({"predict": prediction}), 200
    return jsonify({"msg": "Error: not a JSON or no input key in your request"})


if __name__ == "__main__":
    app.run(host='0.0.0.0')