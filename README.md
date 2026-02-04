# Cure_Pulse - Health Management System

A modern, feature-rich healthcare management system built with Flask, MySQL, and Tailwind CSS featuring a beautiful glassmorphism UI.

## 🌟 Features

- **Patient Registration**: Comprehensive patient onboarding with medical history, insurance details, and document upload
- **Appointment Booking**: Easy-to-use appointment scheduling system with doctor selection
- **Admin Dashboard**: Powerful admin interface to manage appointments (approve, schedule, cancel)
- **SMS Notifications**: Optional Twilio integration for appointment confirmations
- **Glassmorphism UI**: Modern, beautiful dark theme with glassmorphism effects
- **Secure File Upload**: Support for patient identification documents
- **Session Management**: Secure patient and admin sessions

## 📁 Project Structure

```
Cure_Pulse/
│
├── static/
│   ├── css/
│   │   └── style.css          # Custom Glassmorphism effects
│   ├── js/
│   │   └── main.js            # Frontend logic (Modal, API calls)
│   └── uploads/               # Patient ID documents storage
│
├── templates/
│   ├── base.html              # Master layout with Tailwind CDN
│   ├── login.html             # Landing page with Admin Passkey Modal
│   ├── register.html          # Patient registration form
│   ├── booking.html           # Appointment scheduling page
│   └── admin.html             # Admin Dashboard
│
├── config.py                  # Database & API Configuration
├── app.py                     # Main Backend Application
├── schema.sql                 # Database Setup Script
└── requirements.txt           # Python Libraries
```

## 🚀 Quick Start Guide

### Prerequisites

1. **XAMPP** (Apache + MySQL)
   - Download from: https://www.apachefriends.org/
   - Install and start Apache and MySQL services

2. **Python 3.7+**
   - Download from: https://www.python.org/

3. **pip** (Python package manager)
   - Usually comes with Python installation

### Installation Steps

#### Step 1: Database Setup

1. Open XAMPP Control Panel and start **Apache** and **MySQL**
2. Navigate to `http://localhost/phpmyadmin` in your browser
3. Click on **SQL** tab
4. Open the `schema.sql` file from the project folder
5. Copy and paste the entire SQL code into phpMyAdmin
6. Click **Go** to execute

This will create:
- Database: `cure_pulse_db`
- Tables: `users`, `doctors`, `patients`, `appointments`
- Sample doctors data

#### Step 2: Python Environment Setup

Open terminal/command prompt in the `Cure_Pulse` folder and run:

```bash
# Install required Python packages
pip install -r requirements.txt
```

If you encounter issues, install packages individually:
```bash
pip install Flask
pip install flask-mysqldb
pip install twilio
pip install werkzeug
```

#### Step 3: Configuration

Open `config.py` and update if needed:

- **MySQL Password**: If you set a password for MySQL in XAMPP, update `MYSQL_PASSWORD`
- **Secret Key**: Change `SECRET_KEY` for production use
- **Twilio** (Optional): Add your Twilio credentials for SMS notifications

```python
MYSQL_PASSWORD = ''  # Leave empty for default XAMPP, or add your password
SECRET_KEY = 'your-secret-key-here'  # Change for production
```

#### Step 4: Run the Application

```bash
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

#### Step 5: Access the Application

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## 🔐 Default Credentials

**Admin Access:**
- Passkey: `123456`

## 📱 Using the Application

### For Patients:

1. **Registration**
   - Click "Get Started (Patient)" on the landing page
   - Fill in personal details
   - Provide medical information
   - Upload identification document
   - Accept privacy consent
   - Submit to create account

2. **Book Appointment**
   - After registration, you'll be redirected to booking page
   - Select a doctor from the dropdown
   - Choose your preferred date and time
   - Enter reason for visit
   - Submit booking request

3. **Confirmation**
   - You'll receive a flash message confirming your booking
   - If Twilio is configured, you'll get an SMS notification

### For Administrators:

1. **Login**
   - Click "Admin Access" on the landing page
   - Enter passkey: `123456`
   - Click "Verify"

2. **Dashboard Overview**
   - View statistics: Scheduled, Pending, and Cancelled appointments
   - See all appointments in a table format

3. **Manage Appointments**
   - **Approve**: Click "Approve" to schedule a pending appointment
   - **Cancel**: Click "Cancel" to cancel any appointment
   - Status updates happen in real-time

## 🎨 UI Features

- **Dark Theme**: Easy on the eyes with a modern dark color scheme
- **Glassmorphism**: Frosted glass effects for cards and modals
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Smooth Animations**: Hover effects and transitions
- **Custom Scrollbar**: Styled to match the dark theme

## 🔧 Troubleshooting

### Database Connection Issues

If you see "Can't connect to MySQL server":
1. Make sure MySQL is running in XAMPP
2. Check `config.py` for correct credentials
3. Verify database `cure_pulse_db` exists in phpMyAdmin

### File Upload Issues

If file uploads fail:
1. Check that `static/uploads/` folder exists
2. Ensure folder has write permissions
3. Verify file size is under 16MB

### Port Already in Use

If port 5000 is busy:
```python
# In app.py, change the last line to:
app.run(debug=True, port=5001)
```

### Missing Modules

If you get "ModuleNotFoundError":
```bash
pip install <module-name> --break-system-packages
```

## 📊 Database Schema

### Patients Table
Stores patient information including personal details, medical history, and insurance.

### Doctors Table
Contains doctor profiles with specializations.

### Appointments Table
Manages appointment bookings with status tracking (pending, scheduled, cancelled).

### Users Table
Reserved for admin authentication (future enhancement).

## 🔮 Future Enhancements

- [ ] Patient login and profile management
- [ ] Doctor availability calendar
- [ ] Email notifications
- [ ] Medical records management
- [ ] Prescription tracking
- [ ] Payment integration
- [ ] Video consultation
- [ ] Analytics and reporting

## 🛡️ Security Notes

**For Production Deployment:**

1. Change `SECRET_KEY` in `config.py`
2. Use environment variables for sensitive data
3. Implement proper password hashing for admin
4. Enable HTTPS
5. Add CSRF protection
6. Implement rate limiting
7. Use a production WSGI server (Gunicorn, uWSGI)
8. Set `debug=False` in app.py

## 📝 License

This project is for educational purposes. Feel free to use and modify as needed.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## 📞 Support

For issues and questions:
- Check the troubleshooting section above
- Review the code comments in `app.py`
- Verify database setup in phpMyAdmin

---

**Built with ❤️ using Flask, MySQL, and Tailwind CSS**
