from flask import Flask, render_template
import requests


app = Flask(__name__)

resp = requests.get(
        url='http://127.0.0.1:9080/crawl.json?start_requests=true&spider_name=best_selling'
    ).json()

@app.route('/')
def index():
    items = resp.get('items')

    return render_template('index.html', games=items)

@app.route('/api')
def api():
    return resp


if __name__ == '__main__':
    from flask_ngrok import run_with_ngrok
    
    run_with_ngrok(app)
    
    
    app.run()