import random
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/api/ServiceCalls/ServiceCallAdd', methods=['POST'])
def service_call_add():
    form_data = request.json

    # Generate a dummy callId for the purpose of this example
    callId = random.randint(1, 100)

    # Log the received form data
    print('Form Data:', form_data)

    # Create the response object
    response = {
        'callId': callId,
        'data': form_data
    }

    # Send the response
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=False)