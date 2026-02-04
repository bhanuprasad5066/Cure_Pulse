# DEPLOYMENT CHECKLIST - Cure_Pulse

## Pre-Deployment Checklist

### System Requirements
- [ ] XAMPP installed
- [ ] Python 3.7+ installed
- [ ] pip package manager available
- [ ] Web browser (Chrome, Firefox, Edge, etc.)

### Files Verification
- [ ] All files present in Cure_Pulse folder
- [ ] schema.sql contains database structure
- [ ] config.py has correct settings
- [ ] requirements.txt is available
- [ ] templates/ folder has 5 HTML files
- [ ] static/ folder has css and js subfolders

## Database Setup

### Step 1: Start Services
- [ ] Open XAMPP Control Panel
- [ ] Start Apache (port 80)
- [ ] Start MySQL (port 3306)
- [ ] Both services show green "Running" status

### Step 2: Create Database
- [ ] Open http://localhost/phpmyadmin
- [ ] Click "New" in left sidebar
- [ ] Database name: `cure_pulse_db`
- [ ] Collation: utf8_general_ci (default)
- [ ] Click "Create"

### Step 3: Import Schema
- [ ] Select `cure_pulse_db` from left sidebar
- [ ] Click "SQL" tab at top
- [ ] Open `schema.sql` in text editor
- [ ] Copy entire content
- [ ] Paste in SQL query box
- [ ] Click "Go" button
- [ ] Verify: See "4 tables" and "3 rows inserted" message

### Step 4: Verify Tables
- [ ] Click "Structure" tab
- [ ] Confirm 4 tables exist:
  - [ ] users
  - [ ] doctors
  - [ ] patients
  - [ ] appointments
- [ ] Click "doctors" table → Browse
- [ ] Verify 3 doctors listed

## Python Environment Setup

### Install Dependencies
```bash
# Navigate to project folder
cd path/to/Cure_Pulse

# Install packages
pip install -r requirements.txt
```

- [ ] Flask installed successfully
- [ ] flask-mysqldb installed
- [ ] twilio installed
- [ ] werkzeug installed
- [ ] No error messages during installation

### Configuration Check
Edit `config.py` and verify:
- [ ] MYSQL_HOST = 'localhost'
- [ ] MYSQL_USER = 'root'
- [ ] MYSQL_PASSWORD = '' (or your password)
- [ ] MYSQL_DB = 'cure_pulse_db'
- [ ] SECRET_KEY is set
- [ ] UPLOAD_FOLDER path is correct

## Application Launch

### Start Application
```bash
python app.py
```

Expected output:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

- [ ] No error messages
- [ ] Server running on port 5000
- [ ] Debug mode enabled

### Access Application
- [ ] Open browser
- [ ] Navigate to: http://127.0.0.1:5000
- [ ] Landing page loads successfully
- [ ] "Cure_Pulse" logo visible
- [ ] Both buttons ("Get Started" and "Admin Access") visible

## Functionality Testing

### Test Patient Registration
- [ ] Click "Get Started (Patient)"
- [ ] Register page loads
- [ ] All form fields visible
- [ ] Fill in sample data:
  - Name: Test Patient
  - Email: test@example.com
  - Phone: +1234567890
  - DOB: 1990-01-01
  - Other fields (optional)
- [ ] Upload a sample file (any image)
- [ ] Check privacy consent
- [ ] Click "Submit & Continue"
- [ ] Success message appears
- [ ] Redirects to booking page

### Test Appointment Booking
- [ ] Booking page loads
- [ ] Doctor dropdown shows 3 doctors
- [ ] Select a doctor
- [ ] Choose future date/time
- [ ] Enter reason: "Regular checkup"
- [ ] Click "Confirm Booking"
- [ ] Success message appears
- [ ] Redirects to landing page

### Test Admin Access
- [ ] Click "Admin Access" button
- [ ] Modal appears with passkey input
- [ ] Enter passkey: 123456
- [ ] Click "Verify"
- [ ] Dashboard loads
- [ ] Statistics cards show correct counts
- [ ] Appointments table displays
- [ ] Test appointment visible with "pending" status

### Test Admin Actions
- [ ] Click "Approve" on pending appointment
- [ ] Page refreshes
- [ ] Status changes to "scheduled"
- [ ] Green badge displays
- [ ] Statistics update (pending -1, scheduled +1)

### Test Logout
- [ ] Click "Logout" link
- [ ] Redirects to landing page
- [ ] Cannot access /admin without passkey

## Database Verification

### Check phpMyAdmin
- [ ] Open http://localhost/phpmyadmin
- [ ] Select `cure_pulse_db`
- [ ] Click "patients" table → Browse
- [ ] Verify test patient record exists
- [ ] Click "appointments" table → Browse
- [ ] Verify test appointment exists
- [ ] Check status field updates correctly

## File Upload Verification
- [ ] Navigate to `Cure_Pulse/static/uploads/`
- [ ] Verify uploaded file exists
- [ ] File name is sanitized (no spaces/special chars)

## Security Checks (Development)
- [ ] Admin passkey works: 123456
- [ ] Wrong passkey shows error message
- [ ] Cannot access /admin without authentication
- [ ] Session expires after browser close
- [ ] File uploads restricted to 16MB

## Performance Checks
- [ ] Pages load within 2 seconds
- [ ] No console errors in browser (F12)
- [ ] Forms submit smoothly
- [ ] Database queries execute quickly
- [ ] No server errors in terminal

## Common Issues Resolution

### Issue: Cannot connect to MySQL
**Solution:**
- [ ] Check XAMPP MySQL is running
- [ ] Verify port 3306 is not blocked
- [ ] Check config.py credentials

### Issue: Module not found
**Solution:**
- [ ] Run: pip install -r requirements.txt
- [ ] Check Python version: python --version
- [ ] Try: python3 instead of python

### Issue: Template not found
**Solution:**
- [ ] Verify templates/ folder exists
- [ ] Check all 5 HTML files are present
- [ ] Ensure correct file names (lowercase)

### Issue: File upload fails
**Solution:**
- [ ] Create static/uploads/ folder manually
- [ ] Check folder permissions
- [ ] Verify MAX_CONTENT_LENGTH in config

### Issue: Styles not loading
**Solution:**
- [ ] Check static/css/style.css exists
- [ ] Verify Tailwind CDN link in base.html
- [ ] Clear browser cache (Ctrl+F5)

## Production Deployment (Future)

### Security Enhancements
- [ ] Change SECRET_KEY to random string
- [ ] Use environment variables
- [ ] Hash admin passkey
- [ ] Enable HTTPS
- [ ] Add CSRF protection
- [ ] Implement rate limiting

### Database
- [ ] Use production MySQL server
- [ ] Enable SSL connections
- [ ] Regular backups scheduled
- [ ] Optimize indexes

### Application
- [ ] Set DEBUG = False
- [ ] Use production WSGI server (Gunicorn)
- [ ] Configure logging
- [ ] Add error monitoring (Sentry)
- [ ] Enable gzip compression

### Storage
- [ ] Move uploads to cloud storage (AWS S3, Azure Blob)
- [ ] Implement file type validation
- [ ] Add virus scanning
- [ ] Set up CDN for static files

## Final Verification

- [ ] All features working correctly
- [ ] No errors in terminal
- [ ] No errors in browser console
- [ ] Database properly populated
- [ ] File uploads working
- [ ] Admin dashboard functional
- [ ] Ready for demonstration/development

## Success Criteria

✅ XAMPP services running
✅ Database created and seeded
✅ All Python packages installed
✅ Application running on http://127.0.0.1:5000
✅ Patient registration working
✅ Appointment booking working
✅ Admin login working
✅ Admin actions (approve/cancel) working
✅ File uploads functional
✅ No critical errors

---

**Congratulations! Cure_Pulse is ready to use! 🎉**

For ongoing development, refer to README.md for detailed documentation.
