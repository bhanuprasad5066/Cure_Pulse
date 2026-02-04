# 🚀 QUICK START: Deploy in 10 Minutes (FREE)

## The Fastest Way to Get Your App Online

Follow these exact steps to deploy Cure_Pulse for **FREE** on PythonAnywhere.

---

## ⏱️ 10-Minute Deployment Checklist

### ✅ STEP 1: Create Free Account (2 minutes)

1. Visit: **https://www.pythonanywhere.com**
2. Click **"Pricing & signup"**
3. Click **"Create a Beginner account"**
4. Enter:
   - Username: `yourname` (becomes yourname.pythonanywhere.com)
   - Email: your@email.com
   - Password: (create strong password)
5. Click **"Register"**
6. Check email and verify

---

### ✅ STEP 2: Upload Project (2 minutes)

**Method 1: Upload ZIP (Easiest)**

1. Login to PythonAnywhere
2. Click **"Files"** tab (top menu)
3. Click **"Upload a file"** (blue button)
4. Choose `Cure_Pulse.zip`
5. Click `Cure_Pulse.zip` in file list
6. Click **"unzip"** button
7. Wait for extraction

**Method 2: Create via Console**

1. Click **"Consoles"** tab
2. Click **"Bash"**
3. Type:
```bash
git clone https://github.com/yourusername/Cure_Pulse.git
cd Cure_Pulse
```

---

### ✅ STEP 3: Install Libraries (2 minutes)

1. In **"Consoles"** tab, click **"Bash"**
2. Type these commands one by one:

```bash
cd Cure_Pulse
pip3 install --user flask
pip3 install --user flask-mysqldb
pip3 install --user werkzeug
```

Wait for each to complete (green "Successfully installed" message).

---

### ✅ STEP 4: Create Database (2 minutes)

1. Click **"Databases"** tab
2. Find **"Create database"** section
3. Database name will be: `yourusername$cure_pulse_db`
4. Click **"Create"**
5. Note your MySQL password (shown on this page)

**Import Tables:**

6. Scroll to **"Start a console"** → click your database
7. Or click **"Go to phpMyAdmin"**
8. In phpMyAdmin:
   - Select your database (left sidebar)
   - Click **"SQL"** tab
   - Copy this and paste:

```sql
CREATE TABLE IF NOT EXISTS doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100),
    image_url VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    dob DATE NOT NULL,
    gender VARCHAR(20),
    address TEXT,
    primary_physician VARCHAR(100),
    insurance_provider VARCHAR(100),
    insurance_policy_number VARCHAR(50),
    allergies TEXT,
    current_medications TEXT,
    family_medical_history TEXT,
    identification_type VARCHAR(50),
    identification_number VARCHAR(50),
    document_path VARCHAR(255),
    privacy_consent BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    appointment_date DATETIME NOT NULL,
    reason TEXT,
    status ENUM('scheduled', 'pending', 'cancelled') DEFAULT 'pending',
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

INSERT INTO doctors (name, specialization) VALUES 
('Dr. Adam Smith', 'Cardiologist'),
('Dr. Sarah Jones', 'Dermatologist'),
('Dr. Emily Clark', 'Neurologist');
```

9. Click **"Go"**

---

### ✅ STEP 5: Configure App (1 minute)

1. Go to **"Files"** tab
2. Navigate to: `/home/yourusername/Cure_Pulse/`
3. Click on `config.py`
4. Replace entire content with:

```python
import os

class Config:
    # REPLACE 'yourusername' with YOUR actual username!
    MYSQL_HOST = 'yourusername.mysql.pythonanywhere-services.com'
    MYSQL_USER = 'yourusername'
    MYSQL_PASSWORD = 'your_mysql_password_from_databases_tab'
    MYSQL_DB = 'yourusername$cure_pulse_db'
    MYSQL_CURSORCLASS = 'DictCursor'
    
    SECRET_KEY = 'your-secret-key-xyz123'
    UPLOAD_FOLDER = '/home/yourusername/Cure_Pulse/static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    
    TWILIO_ACCOUNT_SID = 'AC_YOUR_ACCOUNT_SID'
    TWILIO_AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
    TWILIO_PHONE_NUMBER = '+1234567890'
```

5. **Important:** Replace `yourusername` and `your_mysql_password` with your actual values
6. Click **"Save"**

---

### ✅ STEP 6: Setup Web App (2 minutes)

1. Go to **"Web"** tab
2. Click **"Add a new web app"**
3. Click **"Next"**
4. Choose **"Flask"**
5. Choose **"Python 3.10"**
6. Path: `/home/yourusername/Cure_Pulse/app.py`
7. Click **"Next"** until done

**Configure WSGI File:**

8. On "Web" tab, find **"Code"** section
9. Click on WSGI configuration file (blue link)
10. **Delete everything** in the file
11. Replace with:

```python
import sys
import os

# REPLACE with YOUR username
project_home = '/home/yourusername/Cure_Pulse'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

os.environ['PRODUCTION'] = 'true'

from app import app as application
```

12. Replace `yourusername`
13. Click **"Save"**

**Setup Static Files:**

14. Still on "Web" tab, find **"Static files"** section
15. Click **"Enter URL"**:
    - URL: `/static/`
    - Directory: `/home/yourusername/Cure_Pulse/static/`
16. Replace `yourusername`, click ✓

---

### ✅ STEP 7: Create Upload Folder (30 seconds)

1. Go to **"Consoles"** → **"Bash"**
2. Type:

```bash
mkdir -p /home/yourusername/Cure_Pulse/static/uploads
chmod 755 /home/yourusername/Cure_Pulse/static/uploads
```

(Replace `yourusername`)

---

### ✅ STEP 8: LAUNCH! (30 seconds)

1. Go to **"Web"** tab
2. Scroll to top
3. Click big green **"Reload yourusername.pythonanywhere.com"** button
4. Wait 15 seconds
5. Click your URL: **https://yourusername.pythonanywhere.com**

---

## 🎉 SUCCESS!

Your app is now LIVE at: **https://yourusername.pythonanywhere.com**

### Quick Test:

1. ✅ See the landing page with "Cure_Pulse"
2. ✅ Click "Get Started" → Registration form appears
3. ✅ Click "Admin Access" → Modal appears
4. ✅ Enter passkey `123456` → Admin dashboard loads

---

## 🚨 If Something Goes Wrong

### Can't See Your App?

**Check Error Log:**
1. Go to **"Web"** tab
2. Find **"Log files"** section (bottom)
3. Click **"Error log"**
4. Read the latest errors

**Common Fixes:**

**1. Import Error:**
```bash
# In Bash console:
cd Cure_Pulse
pip3 install --user flask flask-mysqldb
```

**2. Database Error:**
- Check username in config.py matches your actual username
- Database name must be: `yourusername$cure_pulse_db`
- Check password from Databases tab

**3. Can't Upload Files:**
```bash
chmod 755 /home/yourusername/Cure_Pulse/static/uploads
```

**4. Static Files Missing:**
- Check Static Files path in Web tab
- Verify folder exists in Files tab

---

## 📱 Share Your App!

Your live URL: `https://yourusername.pythonanywhere.com`

**Test Credentials:**
- Admin Passkey: `123456`

**Share on:**
- 📧 Email
- 💼 LinkedIn
- 📱 WhatsApp
- 🐦 Twitter
- 📄 Resume/Portfolio

---

## 🎓 What You Just Did

You successfully:
- ✅ Deployed a Python Flask application
- ✅ Set up MySQL database in the cloud
- ✅ Configured web server (WSGI)
- ✅ Made your app accessible worldwide
- ✅ All for FREE!

---

## 📈 Next Steps

**Immediate:**
1. Change admin passkey in `app.py`
2. Test all features
3. Share your URL

**This Week:**
1. Customize branding
2. Add your contact info
3. Take screenshots for portfolio

**This Month:**
1. Consider upgrading for custom domain ($5/month)
2. Add more features
3. Deploy other projects!

---

## 💡 Pro Tips

1. **Bookmark These Pages:**
   - Your app: https://yourusername.pythonanywhere.com
   - Dashboard: https://www.pythonanywhere.com/dashboard
   - Databases: https://www.pythonanywhere.com/databases

2. **Free Account Limits:**
   - 500MB storage
   - 1 web app
   - 100,000 requests/day
   - Perfect for portfolio projects!

3. **Keep Your Account Active:**
   - Login every 3 months
   - Or app may be disabled
   - Free accounts require occasional activity

4. **Database Backups:**
   - Go to Databases tab
   - Use phpMyAdmin → Export
   - Download monthly

---

## 🆘 Need Help?

**PythonAnywhere Help:**
- Forums: https://www.pythonanywhere.com/forums/
- Help: https://help.pythonanywhere.com/

**Common Questions:**
- Q: Can I use custom domain?
- A: Yes, with paid account ($5/month)

- Q: How long is free?
- A: Forever (with activity every 3 months)

- Q: Can I deploy multiple apps?
- A: 1 app on free, unlimited on paid

---

## ✨ Congratulations!

**You're now a full-stack developer with a live application!**

Your Cure_Pulse Health Management System is:
- ✅ Live on the internet
- ✅ Accessible from any device
- ✅ Running 24/7
- ✅ Free forever
- ✅ Ready to show employers

**Add to your resume:**
*"Deployed production Flask application with MySQL database on cloud infrastructure"*

---

**🎊 Well done! Now go show the world what you've built! 🎊**
