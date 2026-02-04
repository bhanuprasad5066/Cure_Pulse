CREATE DATABASE IF NOT EXISTS cure_pulse_db;
USE cure_pulse_db;

-- 1. Users Table (For Admin Access)
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) NOT NULL UNIQUE,
    role ENUM('admin', 'doctor') DEFAULT 'admin',
    passkey VARCHAR(255) NOT NULL -- Admin Passkey (e.g., 123456)
);

-- Insert default admin account
INSERT INTO users (name, email, role, passkey) VALUES 
('Admin', 'admin@curepulse.com', 'admin', '123456');

-- 2. Doctors Table
CREATE TABLE IF NOT EXISTS doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100),
    image_url VARCHAR(255)
);

-- 3. Patients Table
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
    document_path VARCHAR(255), -- Stores filename of uploaded ID
    privacy_consent BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Appointments Table
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

-- Seed Data (Initial Data)
INSERT INTO doctors (name, specialization) VALUES 
('Dr. Adam Smith', 'Cardiologist'),
('Dr. Sarah Jones', 'Dermatologist'),
('Dr. Emily Clark', 'Neurologist');
