# QUICK SETUP GUIDE - Cure_Pulse

Follow these steps to get Cure_Pulse running in minutes!

## Step 1: Start XAMPP
- Open XAMPP Control Panel
- Start **Apache** module
- Start **MySQL** module

## Step 2: Create Database
1. Open browser → `http://localhost/phpmyadmin`
2. Click "New" to create database
3. Name it: `cure_pulse_db`
4. Click "Create"
5. Click on `cure_pulse_db` → Select "SQL" tab
6. Open `schema.sql` file in a text editor
7. Copy ALL content and paste in SQL tab
8. Click "Go" to execute

## Step 3: Install Python Libraries
Open Command Prompt/Terminal in Cure_Pulse folder:
```
pip install -r requirements.txt
```

## Step 4: Run the Application
In the same terminal:
```
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

## Step 5: Access the Application
Open your browser and go to:
```
http://127.0.0.1:5000
```

## Default Login
- **Admin Passkey**: 123456

## Test the System

### As a Patient:
1. Click "Get Started (Patient)"
2. Fill the registration form
3. Upload a sample ID document
4. Book an appointment

### As Admin:
1. Click "Admin Access"
2. Enter passkey: 123456
3. View and manage appointments

## Common Issues

**Problem**: Can't connect to MySQL
**Solution**: Make sure MySQL is running in XAMPP

**Problem**: Module not found error
**Solution**: Run `pip install -r requirements.txt`

**Problem**: Page not found
**Solution**: Ensure all template files are in templates/ folder

**Problem**: File upload fails
**Solution**: Check that static/uploads/ folder exists

## Need Help?
Check README.md for detailed documentation
