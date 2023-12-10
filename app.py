from flask import Flask, jsonify, request

app = Flask(__name__)

# Example status data
status_data = {
    'student01': {'Apache01': 'FAIL', 'Apache02': 'FAIL', 'Nginx': 'FAIL', 'Database': 'FAIL', 'JBoss': 'FAIL'},
    'student02': {'Apache01': 'FAIL', 'Apache02': 'FAIL', 'Nginx': 'FAIL', 'Database': 'FAIL', 'JBoss': 'FAIL'}
}

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify(status_data)

@app.route('/api/status', methods=['POST'])
def update_status():
    data = request.get_json()
    student = data.get('student')
    service = data.get('service')
    status = data.get('status')

    if student in status_data and service in status_data[student]:
        status_data[student][service] = status
        return jsonify({'message': 'Status updated successfully'})
    else:
        return jsonify({'error': 'Student or service not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
