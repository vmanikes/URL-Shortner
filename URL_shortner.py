from flask import Flask,render_template,request
import uuid
import validators

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/shorten_url',methods=['POST'])
def shorten_url():
    url = request.form['url']

    if validators.url(url):
        unique_id = str(uuid.uuid3(uuid.NAMESPACE_DNS,url))[:7]
    else:
        return "Please enter a valid url"



if __name__ == '__main__':
    app.run()
