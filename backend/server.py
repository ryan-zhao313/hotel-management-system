from flask import Flask, request
from flask_cors import CORS
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    df = pd.read_csv(file)
    return json.dumps({'data': df.to_string()})