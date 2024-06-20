from flask import Flask, request
import pandas as pd

app = Flask(__name__)

# Load the data for spam call numbers
spam_call_numbers = pd.read_csv('spam_call.csv')['Phone Number'].tolist()

@app.route('/spam_call/predict', methods=['POST'])
def predict_spam_call():
    phone_number = request.form['phone_number']
    if phone_number in spam_call_numbers:
        result = 'Spam Call'
    else:
        result = 'Safe Number'
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=False)