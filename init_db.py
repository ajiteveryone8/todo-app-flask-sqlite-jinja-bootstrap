from app import app, db

import os
print(os.getcwd())

with app.app_context():
    db.create_all()
    print("Database and tables created successfully!")
