from flask import Flask, request, Response
from flask_cors import CORS
from io import StringIO
import pandas as pd

app = Flask(__name__)
CORS(app)

def process_payroll(file):
    df = pd.read_csv(file)

    # change hours to 8 if employee forgets to clock out
    df['hours'] = df['hours'].apply(lambda x: 8 if x == 24 else x)

    # calculate total hours per person
    total_hours = df.groupby('name')['hours'].sum().reset_index()

    # return as buffer
    output = StringIO()
    total_hours.to_csv(output, index=False)
    output.seek(0)

    return output


@app.route('/upload_payroll', methods=['POST'])
def upload_file():
    file = request.files['file']
    return Response(process_payroll(file))


if __name__ == '__main__':
    app.run(debug=True)