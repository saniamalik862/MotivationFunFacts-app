
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/motivation', methods=['GET'])
def get_motivation():
    return jsonify({"message": "Believe in yourself! Every day is a new opportunity."})

@app.route('/fun-facts', methods=['GET'])
def get_fun_facts():
    return jsonify({"fact": "Bananas are berries, but strawberries aren't!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
