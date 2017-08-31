from flask import Flask,render_template,request
import uuid
import validators

import redis

app = Flask(__name__)
r = redis.StrictRedis(host='localhost', port=6379, db=0)

#Check database connection
def checkConnection(r):
    try:
        if r.ping() == True:
            return 200
    except Exception as e:
        return 400

def uuid_gen(url):
    if url is None:
        return 401
    else:
        return str(uuid.uuid3(uuid.NAMESPACE_DNS,url))[:7]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten_url',methods=['POST'])
def shorten_url():
    url = request.form['url']

    if validators.url(url):

        #All the database operations from here follow atomic operations
        pipe = r.pipeline()
        unique_id = uuid_gen(url)
        pipe.set('localhost:5000/'+unique_id, url)
        result = pipe.execute()
        return render_template('short_url.html',new_url='localhost:5000/'+unique_id,result=url)
    else:
        return "Please enter a valid url"



if __name__ == '__main__':
    app.run()
