# coding:utf-8
from flask import Flask, request, redirect, url_for
import os
import json
import requests


app = Flask(__name__)
folder = "data"

@app.route('/')
def query():
    bundleid = request.args.get('bundleid')
    if not os.path.exists(folder):
        os.mkdir(folder)

    p = os.path.join(folder, bundleid)
    
    version = 1
    if os.path.exists(p):
        f = open(p, "r")
        version = int(f.read()) + 1
        f.close()
    
    f = open(p, "w+")
    f.write(str(version))
    f.close()

    return str(version)

flask_port = 5001
print("Start")
if __name__ == "__main__":
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.secret_key = 'some_secret'
    app.run(debug=True, host="0.0.0.0", threaded=True, processes=0, port=flask_port)
