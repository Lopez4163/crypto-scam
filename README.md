# Crypto Market Price Watch

# 📈 Crypto Market Price Watch

** 🚨 Important 🚨 **  
- IT IS SAFE TO ADVANCE, ISSUE WITH SSH KEYS! IT IS RUNNING ON THE LOCAL HOST OF AN EC2 ALL GOOD!_
- APP MAY NORT DISPLAY ALL COINS DUE TO ITS AGE_

Make sure when cloning this git repo to create the proper virtual environment and utilize Python3 and pip3, NOT python and pip. Follow the commands below:

## Create a Virtual Environment (Optional but Recommended):
```bash
python3 -m venv venv
```

## Install Flask and Dependencies:
```bash
pip3 install flask
```
## Set the FLASK_APP environment variable:
```bash
export FLASK_APP=main.py
```
## Run the Flask app:
```bash
flask run
```
## or
```bash
python3 main.py
```
## TO RUN IN THE BACKGROUND IN AWS EC2
```bash
nohup flask run --host=0.0.0.0 --port=5000 --cert=cert.pem --key=key.pem &
ps aux | grep "flask run"
```
## Install Flask and Dependencies:
```bash
pip3 install flask
```
