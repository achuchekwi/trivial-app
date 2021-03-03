from flask import Flask
import json
import datetime
app = Flask(__name__)


@app.route("/")
def hello():
    return {
        'statusCode': 200,
        'body': 'Hello world'
    }

@app.route("/status/alive")
def hello1():
    return {
        'statusCode': 200
    }

@app.route("/status/ready")
def hello2():
    timeAfter10Sec=datetime.datetime.now()+datetime.timedelta(seconds=10)

    print("Application is running")

    if datetime.datetime.now() > timeAfter10Sec:
        return {
            'statusCode': 200,
            'ready': json.dumps('True')
        }
    else:
        return {
            'statusCode': 500,
            'ready': json.dumps('False')
        }


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)
