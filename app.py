from flask import Flask, request, jsonify
import numpy as np
from twilio.rest import Client
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences
from dotenv import load_dotenv
import os


app = Flask(__name__)

# Load trained model
model = load_model("spam_detector.keras")

load_dotenv()

# Preprocessing constants
VOCAB_SIZE = 11330  
MAX_LENGTH = 171  

# Twilio Credentials (For Testing)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def predict_message(pred_text):
    """Predict if a message is spam or ham."""
    class_dict = {0: "ham", 1: "spam"}
    encoded_message = [one_hot(pred_text, VOCAB_SIZE)]
    padded_message = pad_sequences(encoded_message, maxlen=MAX_LENGTH, padding='post')
    prediction_prob = model.predict(padded_message)[0][0]
    prediction_label = class_dict[np.round(prediction_prob)]
    return prediction_label

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    prediction = predict_message(text)
    return jsonify({'prediction': prediction})

@app.route("/whatsapp", methods=["POST"])
def receive_whatsapp():
    sender = request.form.get("From")  
    text = request.form.get("Body")    

    if not text:
        return "Invalid request", 400

    # Predict if spam or ham
    result = predict_message(text)

    # Send response via WhatsApp
    client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        to=sender,
        body=f"Spam Detection Result: {result.upper()}",
    )

    return "Message Processed", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
