# YTubers
---

## Setup

The first thing to do is to clone the repository:
- create folder and inside folder run this command
```
git clone https://github.com/princepatoliya/ytubers.git
```

- Create a virtual environment to install pakages to using **requirement.txt** file(inside ytuber folder). razorpay support 3.6 or below python version.[razorpay docs](https://razorpay.com/docs/payment-gateway/server-integration/python/)
```
pip install pipenv
pipenv shell --python 3.6
```
- Then install the dependencies:
```
pipenv install -r ytubers/requirements.txt
```
- create file '.env' and enter you passwords and apis(razorpay => KEY_ID, KEY_SECRET),
I used Postgresql.
```
DB_NAME=<Value>
DB_USER=<Value>
DB_PASSWORD=<Value>
DB_HOST=<Value>


EMAIL_PORT = <Value>
EMAIL_USE_TLS = <Value>
EMAIL_HOST_USER = <Value>
EMAIL_HOST_PASSWORD = <Value>


KEY_ID = <Value>
KEY_SECRET = <Value>
```



