# 🚀 Quick Setup Checklist

Follow these steps in order to get Cure_Pulse running:

## ✅ Pre-Installation

- [ ] XAMPP installed and running (Apache + MySQL)
- [ ] Python 3.7+ installed
- [ ] Terminal/Command Prompt access

## ✅ Database Setup

- [ ] Open phpMyAdmin at http://localhost/phpmyadmin
- [ ] Click "SQL" tab
- [ ] Copy contents of `schema.sql`
- [ ] Paste and click "Go"
- [ ] Verify `cure_pulse_db` database was created
- [ ] Check that 3 doctors were added to `doctors` table

## ✅ Python Setup

- [ ] Open terminal in `Cure_Pulse` folder
- [ ] Run: `pip install -r requirements.txt`
- [ ] Wait for all packages to install successfully

## ✅ Configuration

- [ ] Open `config.py`
- [ ] Update `MYSQL_PASSWORD` if you set one in XAMPP (otherwise leave empty)
- [ ] (Optional) Add Twilio credentials for SMS

## ✅ First Run

- [ ] Run: `python app.py`
- [ ] Look for message: "Running on http://127.0.0.1:5000"
- [ ] Open browser to http://127.0.0.1:5000
- [ ] See the Cure_Pulse landing page

## ✅ Test the Application

### Patient Flow:
- [ ] Click "Get Started (Patient)"
- [ ] Fill registration form
- [ ] Upload a test document (any image/PDF)
- [ ] Submit registration
- [ ] See booking page
- [ ] Select a doctor
- [ ] Choose date/time
- [ ] Submit appointment

### Admin Flow:
- [ ] Return to home page
- [ ] Click "Admin Access"
- [ ] Enter passkey: `123456`
- [ ] See admin dashboard
- [ ] View the appointment you just created
- [ ] Click "Approve" to schedule it
- [ ] See status change to "scheduled"

## 🎉 Success!

If all checkboxes are ticked, your Cure_Pulse system is fully operational!

## 🔧 Common Issues

**MySQL Connection Error:**
- Ensure MySQL is running in XAMPP Control Panel
- Check password in config.py matches XAMPP MySQL password

**Module Not Found:**
- Run: `pip install <module-name>`
- Or reinstall all: `pip install -r requirements.txt`

**Port 5000 Busy:**
- Change port in app.py: `app.run(debug=True, port=5001)`
- Access at http://127.0.0.1:5001

**Can't Upload Files:**
- Check `static/uploads/` folder exists
- Verify file is under 16MB

## 📞 Need Help?

1. Read the full README.md
2. Check error messages in terminal
3. Verify database tables in phpMyAdmin
4. Review browser console for JavaScript errors
