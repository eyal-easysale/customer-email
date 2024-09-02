from flask import Flask, jsonify, request
from flask_mail import Mail, Message
import re

app = Flask(__name__)

# Configuration for mail server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'masofonim.help@gmail.com'
app.config['MAIL_PASSWORD'] = 'djzt bqwl tcrw kihm'
mail = Mail(app)

def is_valid_email(email):
    # Simple regex for validating an email
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route('/receive-data', methods=['POST'])
def receive_data_and_send_email():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    email = data.get('email')
    name = data.get('name')
    callId = data.get('callId')

    if not email or not is_valid_email(email):
        return jsonify({"error": "Invalid or missing email address"}), 400

    # Process the data as needed
    print(f"Received email: {email}, name: {name}, callId: {callId}")

    # Prepare the email content
    try:
        msg = Message(
            subject=f"נפתחה עבורך קריאת שירות מספר: {callId}",
            sender=('קריאת שירות ב easy-sale', 'masofonim.help@gmail.com'),
            recipients=[email]
        )

        msg.body = (
            f"נפתחה עבורך קריאת שירות מספר ,{name} {callId} במערכת easy-sale.\n\n"
            "יש לשמור את מספר הקריאה ע\"מ לזרז את תהליך התמיכה ולמענה מהיר יותר.\n\n"
            "זמני פעילות התמיכה:\n"
            "ימים א-ה משעה 09:00 - 17:00.\n\n"
            "זמן מענה ראשוני משוער: עד 3 שעות בהתאם לזמני פעילות התמיכה.\n\n"
            "תודה שבחרת easy-sale :)\n\n"
            "אין להשיב למייל זה."
        )

        # Send the email
        mail.send(msg)
        return jsonify({"message": "Data received and email sent successfully"}), 200
    except Exception as e:
        print(f"Failed to send email: {e}")
        return jsonify({"error": "Failed to send email"}), 500

if __name__ == '__main__':
    app.run(debug=True)