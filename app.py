from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
from twilio.rest import Client
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

# --- Helper Functions ---
def send_sms(to_number, body_text):
    """Sends SMS via Twilio if configured"""
    try:
        if app.config['TWILIO_ACCOUNT_SID'] != 'AC_YOUR_ACCOUNT_SID':
            client = Client(app.config['TWILIO_ACCOUNT_SID'], app.config['TWILIO_AUTH_TOKEN'])
            client.messages.create(
                body=body_text,
                from_=app.config['TWILIO_PHONE_NUMBER'],
                to=to_number
            )
            return True
    except Exception as e:
        print(f"SMS Error: {e}")
    return False

# --- Routes ---

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 1. Handle File Upload
        file = request.files.get('document')
        filename = None
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # 2. Extract Data
        d = request.form
        cursor = mysql.connection.cursor()
        
        try:
            query = """
                INSERT INTO patients (full_name, email, phone, dob, gender, address, 
                primary_physician, insurance_provider, insurance_policy_number, 
                allergies, current_medications, family_medical_history, 
                identification_type, identification_number, document_path, privacy_consent)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                d['full_name'], d['email'], d['phone'], d['dob'], d['gender'],
                d['address'], d['primary_physician'], d['insurance_provider'],
                d['insurance_policy_number'], d['allergies'], d['current_medications'],
                d['family_medical_history'], d['identification_type'], 
                d['identification_number'], filename, 1 if 'privacy_consent' in d else 0
            ))
            mysql.connection.commit()
            
            # Auto-login the patient to session
            session['patient_id'] = cursor.lastrowid
            flash('Registration successful! Please book your first appointment.', 'success')
            return redirect(url_for('book_appointment'))
            
        except Exception as e:
            mysql.connection.rollback()
            flash(f'Error: {str(e)}', 'error')
        finally:
            cursor.close()
            
    return render_template('register.html')

@app.route('/book', methods=['GET', 'POST'])
def book_appointment():
    cursor = mysql.connection.cursor()
    
    if request.method == 'POST':
        patient_id = session.get('patient_id')
        if not patient_id:
            flash('Session expired. Please register or login.', 'error')
            return redirect(url_for('register'))

        doctor_id = request.form['doctor']
        date = request.form['date']
        reason = request.form['reason']

        cursor.execute("INSERT INTO appointments (patient_id, doctor_id, appointment_date, reason) VALUES (%s, %s, %s, %s)",
                       (patient_id, doctor_id, date, reason))
        mysql.connection.commit()
        
        # SMS Notification Logic
        cursor.execute("SELECT phone FROM patients WHERE patient_id=%s", (patient_id,))
        patient = cursor.fetchone()
        send_sms(patient['phone'], f"CurePulse: Appointment requested for {date}. We will confirm shortly.")
        
        flash('Appointment booked! Check your SMS for confirmation.', 'success')
        return redirect(url_for('index'))

    # Load Doctors for Dropdown
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    cursor.close()
    return render_template('booking.html', doctors=doctors)

@app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
    # Email and Passkey Verification
    if request.method == 'POST':
        email = request.form.get('email')
        passkey = request.form.get('passkey')
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s AND passkey=%s AND role='admin'", (email, passkey))
        user = cursor.fetchone()
        cursor.close()
        if user:
            session['admin_logged_in'] = True
        else:
            flash('Invalid Admin Email or Passkey', 'error')
            return redirect(url_for('index'))

    if not session.get('admin_logged_in'):
        return redirect(url_for('index'))

    cursor = mysql.connection.cursor()
    
    # 1. Fetch Stats
    cursor.execute("SELECT COUNT(*) as count FROM appointments WHERE status='scheduled'")
    scheduled = cursor.fetchone()['count']
    cursor.execute("SELECT COUNT(*) as count FROM appointments WHERE status='pending'")
    pending = cursor.fetchone()['count']
    cursor.execute("SELECT COUNT(*) as count FROM appointments WHERE status='cancelled'")
    cancelled = cursor.fetchone()['count']

    # 2. Fetch Appointments Table
    cursor.execute("""
        SELECT a.*, p.full_name as patient_name, d.name as doctor_name 
        FROM appointments a
        JOIN patients p ON a.patient_id = p.patient_id
        JOIN doctors d ON a.doctor_id = d.doctor_id
        ORDER BY a.appointment_date DESC
    """)
    appointments = cursor.fetchall()
    cursor.close()
    
    return render_template('admin.html', 
                           stats={'scheduled': scheduled, 'pending': pending, 'cancelled': cancelled},
                           appointments=appointments)

@app.route('/admin/action', methods=['POST'])
def admin_action():
    """API Endpoint for canceling/scheduling appointments via JS"""
    if not session.get('admin_logged_in'):
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.json
    appt_id = data.get('id')
    action = data.get('action')  # 'schedule' or 'cancel'
    
    cursor = mysql.connection.cursor()
    status = 'scheduled' if action == 'schedule' else 'cancelled'
    
    cursor.execute("UPDATE appointments SET status=%s WHERE appointment_id=%s", (status, appt_id))
    mysql.connection.commit()
    cursor.close()
    
    return jsonify({'success': True})

if __name__ == '__main__':
    # Ensure upload folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
