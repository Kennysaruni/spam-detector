# Spam Detector Using AI

This project is an **AI-powered spam detection system** that classifies messages as either **spam** or **ham** (not spam). It is built using **Python (Flask)** for the backend, **TensorFlow/Keras** for the machine learning model, and **Twilio** for WhatsApp message integration. The frontend can be implemented using **React.js** for a seamless user experience.

## Features
- Detects spam messages using a **trained neural network model**.
- Provides a **REST API** for spam detection.
- Integrates **WhatsApp messaging** using Twilio to classify received messages.
- Supports SMS and form-based input for spam detection.
- Uses **Flask** as the backend framework.

## Tech Stack
- **Backend**: Flask, TensorFlow/Keras, Twilio API
- **Machine Learning**: Pre-trained neural network model (`spam_detector.keras`)
- **Frontend**: React.js (optional, for user interface)
- **Database**: None (model is pre-trained)

## Setup and Installation
### 1. Clone the repository
```sh
$ git clone https://github.com/yourusername/spam-detector.git
$ cd spam-detector
```

### 2. Set up a virtual environment (Recommended)
```sh
$ python -m venv venv
$ source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install dependencies
```sh
$ pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the project root and add the following:
```env
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
```

### 5. Run the Flask API
```sh
$ python app.py
```

### 6. Test the API
You can test it using **Postman** or `curl`:
```sh
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"text": "You have won $1000! Click here to claim."}'
```
**Response:**
```json
{
  "prediction": "spam"
}
```

## WhatsApp Integration (Twilio)
1. **Setup Twilio**
   - Sign up at [Twilio](https://www.twilio.com/whatsapp).
   - Verify your phone number.
   - Get your **Twilio API credentials**.
   
2. **Use WhatsApp for Spam Detection**
   - Send a WhatsApp message to the Twilio sandbox number.
   - The Flask app will process it and return whether it is spam or not.

## API Endpoints
| Method | Endpoint      | Description |
|--------|-------------|-------------|
| POST   | `/predict`   | Detects if a message is spam or ham. |
| POST   | `/whatsapp`  | Receives WhatsApp messages and classifies them. |

## Future Improvements
- **Enhance model accuracy** with more training data.
- **Integrate SMS services** beyond WhatsApp (e.g., Vonage).
- **Create a frontend UI** in React for easier use.

## License
This project is licensed under the **MIT License**.

## Author
Developed by **Saruni**