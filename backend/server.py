from flask import Flask, request
from flask_cors import CORS
from io import StringIO
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

def process_csv(file):
    df = pd.read_csv(StringIO(file.decode('utf-8')))

    # CSV processing code here

    report = {
        # Fill in with the processed data
    }

    return report


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    df = pd.read_csv(file)
    return json.dumps({'data': df.to_string()})


if __name__ == '__main__':
    app.run(debug=True)