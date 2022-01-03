import requests
response_sal = requests.post("http://127.0.0.1:5000/spam", json={"sal": "[[20, ]]"})
response_sal.json()