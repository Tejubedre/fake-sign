from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a simple model
class Sign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(255), nullable=False)
    is_fake = db.Column(db.Boolean, default=False)

# Placeholder function for fake sign detection (replace with actual detection logic)
def detect_fake_sign(image_path):
    # Replace this with your actual detection logic using a pre-trained model
    # This function should return True if the sign is fake, False otherwise
    # For simplicity, we'll just return False in this example
    return False

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Assuming you have an HTML form with a file input named 'image'
        uploaded_file = request.files["image"]
        
        if uploaded_file.filename != "":
            # Save the uploaded file
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            uploaded_file.save(image_path)
            
            # Perform fake sign detection
            is_fake = detect_fake_sign(image_path)
            
            # Save the result to the database
            new_sign = Sign(image_path=image_path, is_fake=is_fake)
            db.session.add(new_sign)
            db.session.commit()

            loading_time = round(time.time() - start_time, 2)
            return render_template("result.html", is_fake=is_fake, image_path=image_path)

    # Render the main page
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

# Run the application
if __name__ == "__main__":
    db.create_all()  # Create the database tables
    app.run(host="0.0.0.0", port=5000, debug=True)

