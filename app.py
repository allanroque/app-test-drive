from flask import Flask, jsonify

app = Flask(__name__)

# Example status data
status_data = {
    'student01': {'Apache01': 'FAIL', 'Apache02': 'FAIL', 'Nginx': 'FAIL', 'Database': 'FAIL', 'JBoss': 'FAIL'},
    'student02': {'Apache01': 'FAIL', 'Apache02': 'FAIL', 'Nginx': 'FAIL', 'Database': 'FAIL', 'JBoss': 'FAIL'}
}

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify(status_data)

if __name__ == '__main__':
    app.run(debug=True)

