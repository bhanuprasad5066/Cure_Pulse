import os

class Config:
    # Database Config (XAMPP Defaults)
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''  # Leave empty for default XAMPP
    MYSQL_DB = 'cure_pulse_db'
    MYSQL_CURSORCLASS = 'DictCursor'
    
    # App Security
    SECRET_KEY = 'cure_pulse_secret_key'  # Change this for production
    UPLOAD_FOLDER = os.path.join('static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB Max Upload

    # Twilio (Optional: Leave placeholder if not using SMS yet)
    TWILIO_ACCOUNT_SID = 'AC_YOUR_ACCOUNT_SID'
    TWILIO_AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
    TWILIO_PHONE_NUMBER = '+1234567890'
