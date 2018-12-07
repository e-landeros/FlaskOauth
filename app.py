import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] ='1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
from flask import Flask, render_template, url_for, redirect
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

blueprint = make_google_blueprint(client_id='', client_secret='', offline=True, scope=['profile', 'email'])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
 