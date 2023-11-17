# Crypto Market Price Watch

**\***Important**\***
IT IS SAFE TO ADVANCE, ISSUE WITH SSH KEYS! IT IS RUNNING ON THE LOCAL HOST OF AN EC2 ALL GOOD!
make sure when cloning this git repo to create the proper virtual enviorment and utilizew python3 and pip3, NOT python and pip. Follow the commands bellow

Create a Virtual Environment (Optional but Recommended):
python3 -m venv venv

Activate the virtual environment:
source venv/bin/activate

Install Flask and Dependencies:
pip3 install flask

Set the FLASK_APP environment variable:
export FLASK_APP=main.py

Run the Flask app:
flask run

If you encounter any issues with the flask command, you can use the following alternative:

python3 main.py

TO RUN IN THE BACKGROUND
nohup flask run --host=0.0.0.0 --port=5000 --cert=cert.pem --key=key.pem &

ps aux | grep "flask run"

TO KILL APP
kill -9 PID
