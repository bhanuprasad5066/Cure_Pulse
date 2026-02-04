# TODO: Enhance Admin Login Security

## Tasks
- [x] Update schema.sql: Add email column to users table and seed limited admin users with email and passkey
- [x] Update templates/login.html: Add email input field to admin modal
- [x] Update app.py: Modify admin_dashboard route to verify email and passkey against database
- [ ] Test the updated login functionality

## Dependent Files
- schema.sql
- templates/login.html
- app.py

## Followup Steps
- Run the updated schema.sql in phpMyAdmin to apply changes
- Restart the Flask app if running
- Test admin login with seeded credentials
