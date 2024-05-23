from flask import Flask,render_template,request
import requests


app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/weatherapp',methods=['POST','GET'])
def get_data():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {
        'q':request.form["city"],
        'appid':request.form["appid"],
        'units':request.form["units"]
    }
    response = requests.get(url,params=param)
    data = response.json()
    return f"date: {data}"

if __name__=='__main__':
        app.run(host="0.0.0.0",port = 5000)    
        
        
        