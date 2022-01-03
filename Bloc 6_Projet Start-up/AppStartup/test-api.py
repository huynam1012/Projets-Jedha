import requests
#response_sal = requests.post("http://127.0.0.1:5000/predict", json={"sal": [3,]})
#str_format= response_sal.json()
#print(str_format["predict"])
url = "http://127.0.0.1:5000/predict"
# This a simple example of input
input_simple = {
    "input": [[300,5,"2001-01-01","2004-11-10","2006-09-12"]]
}

"""
# This a simple example of input
res = requests.post(url, json=input_simple)
assert res.status_code == 200
print("prediction:{}".format(res.json()["predict"]))
"""

# This a example of input with several inputs
#[["funding_total_usd",  "funding_rounds", "founded_at", "first_funding_at", "last_funding_at"]]
input_multiple = {"input": [[38730470,1,"2011-01-01","2011-01-01","2011-01-01"],[7998800,2,"2001-01-01","2008-07-10","2008-11-12"]]}


res = requests.post(url, json=input_multiple )
assert res.status_code == 200
fres= list(res.json().values())

#print(list(fres[0].replace(" ",",")))
print("predictions:{}".format(fres))


