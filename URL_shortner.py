from flask import Flask,render_template,request
import uuid
import validators


from collections import defaultdict
app = Flask(__name__)

shortened_urls = defaultdict()

@app.route('/')
def index():
    print(render_template('index.html'))
    return render_template('index.html')

@app.route('/shorten_url',methods=['POST'])
def shorten_url():
    url = request.form['url']

    if validators.url(url):
        unique_id = str(uuid.uuid3(uuid.NAMESPACE_DNS,url))[:7]
        shortened_urls['localhost:5000/'+unique_id] = url

        return render_template('short_url.html',new_url='localhost:5000/'+unique_id,shortened_urls=shortened_urls)
    else:
        return "Please enter a valid url"



if __name__ == '__main__':
    app.run()
