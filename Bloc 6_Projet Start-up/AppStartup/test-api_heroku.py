import requests
#response_sal = requests.post("https://wineflask2.herokuapp.com/predict", json={"sal": [3,]})
#str_format= response_sal.json()
#print(str_format["predict"])
url = "https://wineflask2.herokuapp.com/predict"
# This a simple example of input
input_simple = {
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
}

"""
# This a simple example of input
res = requests.post(url, json=input_simple)
assert res.status_code == 200
print("prediction:{}".format(res.json()["predict"]))
"""

# This a example of input with several inputs
input_multiple = {
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8],
             [5.0, 0.98, 0.32, 18.9, 0.050, 75.0, 122.0, 0.401, 3.1, 0.21, 1.2]]
}


res = requests.post(url, json=input_simple)
assert res.status_code == 200
fres= list(res.json().values())
fres= [int(x) for x  in list(fres[0][1:-1].split(" "))]

#print(list(fres[0].replace(" ",",")))
print("predictions:{}".format(fres))
#fres= [fres[0]]

#print(fres)
#print("Value(s) predicted",str(fres))
#print("Value(s) predicted",list(fres2).str.split(" ") )

