import requests
from flask import Flask,render_template,Response

app = Flask(__name__)

SeriesList = []
@app.route('/',methods=['GET'])

def Series():
    req = requests.get('https://www.episodate.com/api/most-popular?page=1')
    content = req.json()
    for data in content['tv_shows']:
        if data not in SeriesList:
              SeriesList.append(data)
    return render_template('SeriesList.html',serieslist = SeriesList)

if __name__ == '__main__':
    app.run(debug=True)

