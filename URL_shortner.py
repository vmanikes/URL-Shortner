from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/shorten_url',methods=['POST'])
def shorten_url():
    url = request.form['url']
    return url


if __name__ == '__main__':
    app.run()
