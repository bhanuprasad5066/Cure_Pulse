# 🚀 Cure_Pulse - Deployment & Troubleshooting Guide

## 📋 Table of Contents
1. [System Requirements](#system-requirements)
2. [Step-by-Step Installation](#step-by-step-installation)
3. [Configuration Guide](#configuration-guide)
4. [Testing the Application](#testing-the-application)
5. [Common Errors & Solutions](#common-errors--solutions)
6. [Production Deployment](#production-deployment)

---

## System Requirements

### Minimum Requirements:
- **Operating System**: Windows 10/11, macOS 10.14+, or Linux
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 500MB free space
- **Python**: Version 3.7 or higher
- **Browser**: Chrome, Firefox, Safari, or Edge (latest versions)

### Required Software:
1. **XAMPP** - For Apache and MySQL servers
2. **Python 3.7+** - Backend runtime
3. **pip** - Python package manager

---

## Step-by-Step Installation

### 1️⃣ Install XAMPP

**Windows:**
1. Download from https://www.apachefriends.org/download.html
2. Run the installer
3. Choose installation directory (default: C:\xampp)
4. Install with default components (Apache, MySQL, PHP)
5. Launch XAMPP Control Panel
6. Start **Apache** and **MySQL** modules

**macOS:**
1. Download XAMPP for macOS
2. Mount the .dmg file
3. Drag XAMPP to Applications folder
4. Open XAMPP and start Apache & MySQL

**Linux:**
```bash
wget https://www.apachefriends.org/xampp-files/8.2.12/xampp-linux-x64-8.2.12-0-installer.run
chmod +x xampp-linux-*-installer.run
sudo ./xampp-linux-*-installer.run
sudo /opt/lampp/lampp start
```

### 2️⃣ Verify XAMPP Installation

1. Open browser
2. Navigate to: `http://localhost`
3. You should see XAMPP dashboard
4. Click "phpMyAdmin" or go to: `http://localhost/phpmyadmin`
5. You should see the phpMyAdmin interface

### 3️⃣ Install Python

**Windows:**
1. Download from https://www.python.org/downloads/
2. Run installer
3. ✅ **IMPORTANT**: Check "Add Python to PATH"
4. Click "Install Now"

**macOS:**
```bash
# Using Homebrew
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**Verify Installation:**
```bash
python --version  # Should show Python 3.7+
pip --version     # Should show pip version
```

### 4️⃣ Set Up Database

1. Open phpMyAdmin: `http://localhost/phpmyadmin`
2. Click on **"SQL"** tab at the top
3. Open the `schema.sql` file from Cure_Pulse folder
4. Copy **ALL** the SQL code
5. Paste into the SQL query box
6. Click **"Go"** button

**Verify Database Creation:**
- Look for `cure_pulse_db` in the left sidebar
- Click on it to expand
- You should see 4 tables: `users`, `doctors`, `patients`, `appointments`
- Click on `doctors` table
- Click "Browse" - you should see 3 doctors listed

### 5️⃣ Install Python Dependencies

Open terminal/command prompt and navigate to Cure_Pulse folder:

**Windows:**
```cmd
cd C:\path\to\Cure_Pulse
pip install -r requirements.txt
```

**macOS/Linux:**
```bash
cd /path/to/Cure_Pulse
pip3 install -r requirements.txt
```

**If you encounter permission errors (macOS/Linux):**
```bash
pip3 install -r requirements.txt --user
```

**Individual Package Installation (if requirements.txt fails):**
```bash
pip install Flask
pip install flask-mysqldb
pip install twilio
pip install werkzeug
```

### 6️⃣ Configure the Application

1. Open `config.py` in a text editor
2. Check MySQL password:
   ```python
   MYSQL_PASSWORD = ''  # Empty for default XAMPP
   ```
   - If you set a password in XAMPP, enter it here
   - Most default XAMPP installations have no password

3. (Optional) Configure Twilio for SMS:
   - Sign up at https://www.twilio.com/
   - Get your Account SID, Auth Token, and Phone Number
   - Update in `config.py`:
   ```python
   TWILIO_ACCOUNT_SID = 'your_account_sid'
   TWILIO_AUTH_TOKEN = 'your_auth_token'
   TWILIO_PHONE_NUMBER = '+1234567890'
   ```

### 7️⃣ Run the Application

```bash
python app.py
```

**Expected Output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
```

### 8️⃣ Access the Application

Open your browser and go to:
```
http://127.0.0.1:5000
```
or
```
http://localhost:5000
```

You should see the Cure_Pulse landing page!

---

## Configuration Guide

### Database Configuration

**Custom MySQL Port:**
If MySQL runs on a different port (default: 3306):
```python
# In config.py
MYSQL_HOST = 'localhost:3307'  # Change port number
```

**Remote Database:**
```python
MYSQL_HOST = 'your-database-host.com'
MYSQL_USER = 'your_username'
MYSQL_PASSWORD = 'your_password'
MYSQL_DB = 'cure_pulse_db'
```

### File Upload Configuration

**Change Upload Directory:**
```python
# In config.py
UPLOAD_FOLDER = os.path.join('static', 'custom_uploads')
```

**Change Maximum File Size:**
```python
# In config.py (size in bytes)
MAX_CONTENT_LENGTH = 32 * 1024 * 1024  # 32MB
```

### Security Configuration

**Production Secret Key:**
```python
# Generate a random secret key
import secrets
secrets.token_hex(16)

# Use the generated key in config.py
SECRET_KEY = 'your-generated-key-here'
```

---

## Testing the Application

### Patient Registration Flow

1. **Navigate to Registration:**
   - Click "Get Started (Patient)"

2. **Fill Personal Information:**
   - Full Name: John Doe
   - Email: john.doe@example.com
   - Phone: +1234567890
   - Date of Birth: 1990-01-01
   - Gender: Male
   - Address: 123 Main St

3. **Medical Details:**
   - Primary Physician: Dr. Smith
   - Insurance Provider: Blue Cross
   - Policy Number: BC123456
   - Allergies: None
   - Current Medications: None
   - Family History: None

4. **Identification:**
   - Type: Driver's License
   - Number: DL123456
   - Upload: Any image or PDF file

5. **Privacy Consent:**
   - ✅ Check the consent box

6. **Submit:**
   - Click "Submit & Continue"
   - You should be redirected to booking page

### Appointment Booking Flow

1. **Select Doctor:**
   - Choose from dropdown (e.g., Dr. Adam Smith - Cardiologist)

2. **Choose Date/Time:**
   - Select future date and time

3. **Reason for Visit:**
   - Enter: "Annual checkup"

4. **Submit:**
   - Click "Confirm Booking"
   - You should see success message

### Admin Dashboard Flow

1. **Access Admin:**
   - Return to home page
   - Click "Admin Access"

2. **Enter Passkey:**
   - Type: 123456
   - Click "Verify"

3. **View Dashboard:**
   - See statistics (Scheduled, Pending, Cancelled)
   - View appointments table

4. **Manage Appointments:**
   - Find the appointment you created
   - Click "Approve" to schedule
   - Status changes to "scheduled"
   - Statistics update automatically

---

## Common Errors & Solutions

### 🔴 Error: "Can't connect to MySQL server"

**Cause:** MySQL is not running or wrong credentials

**Solution:**
1. Open XAMPP Control Panel
2. Click "Start" next to MySQL
3. Check `config.py` for correct password
4. Verify database exists in phpMyAdmin

### 🔴 Error: "No module named 'flask_mysqldb'"

**Cause:** Package not installed

**Solution:**
```bash
pip install flask-mysqldb
```

**If still fails (Windows):**
```bash
# Install mysqlclient separately
pip install mysqlclient
pip install flask-mysqldb
```

**macOS/Linux:**
```bash
# Install MySQL dependencies
# Ubuntu/Debian:
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential

# macOS:
brew install mysql

# Then install Python packages
pip3 install mysqlclient
pip3 install flask-mysqldb
```

### 🔴 Error: "OSError: [Errno 98] Address already in use"

**Cause:** Port 5000 is already in use

**Solution 1 - Change Port:**
```python
# In app.py, last line:
app.run(debug=True, port=5001)
```
Access at: `http://127.0.0.1:5001`

**Solution 2 - Kill Process:**
```bash
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F

# macOS/Linux:
lsof -ti:5000 | xargs kill -9
```

### 🔴 Error: "Table 'cure_pulse_db.doctors' doesn't exist"

**Cause:** Database not properly created

**Solution:**
1. Go to phpMyAdmin
2. Select `cure_pulse_db` database
3. Click "SQL" tab
4. Re-run the entire `schema.sql` script
5. Verify tables are created

### 🔴 Error: File upload fails silently

**Cause:** Upload directory doesn't exist or no permissions

**Solution:**
```bash
# Create directory manually
mkdir static/uploads

# Windows - Set permissions:
# Right-click folder → Properties → Security → Edit

# macOS/Linux - Set permissions:
chmod 777 static/uploads
```

### 🔴 Error: "Session expired. Please register or login"

**Cause:** Session data lost

**Solution:**
1. Complete registration again
2. Ensure cookies are enabled in browser
3. Don't use incognito/private mode
4. Check `SECRET_KEY` is set in config.py

### 🔴 Error: "Invalid Admin Passkey"

**Cause:** Wrong passkey entered

**Solution:**
- Default passkey is: `123456`
- Ensure no spaces before/after
- Check caps lock is off

### 🔴 Browser shows source code instead of rendered page

**Cause:** Apache serving .py files instead of Flask

**Solution:**
- Don't place project in XAMPP htdocs folder
- Run using `python app.py`, not through Apache
- Access via `127.0.0.1:5000`, not `localhost/cure_pulse`

---

## Production Deployment

### 🚀 Preparing for Production

**1. Security Updates:**

```python
# config.py
import os

class Config:
    # Use environment variables
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-this'
    MYSQL_HOST = os.environ.get('DB_HOST', 'localhost')
    MYSQL_PASSWORD = os.environ.get('DB_PASSWORD', '')
    
    # Disable debug
    DEBUG = False
```

**2. Update app.py:**

```python
# Change last line
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

**3. Use Production WSGI Server:**

```bash
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

**4. Set Up Reverse Proxy (Nginx):**

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /path/to/Cure_Pulse/static;
    }
}
```

**5. Enable HTTPS:**
```bash
# Using Let's Encrypt
sudo certbot --nginx -d yourdomain.com
```

### 📊 Monitoring & Logs

**Enable Logging:**
```python
# In app.py
import logging

logging.basicConfig(
    filename='cure_pulse.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

---

## 📞 Support & Resources

### Documentation
- Flask: https://flask.palletsprojects.com/
- MySQL: https://dev.mysql.com/doc/
- Tailwind CSS: https://tailwindcss.com/docs

### Community
- Stack Overflow: Tag questions with `flask` `mysql` `cure-pulse`
- GitHub Issues: Report bugs and feature requests

### Updates
Check for updates regularly to get new features and security patches.

---

**🎉 Congratulations! Your Cure_Pulse system should now be fully operational!**
