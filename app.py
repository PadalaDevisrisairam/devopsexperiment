from flask import Flask, render_template

# Initialize Flask App
app = Flask(__name__)
# Route to Render Registration Form
@app.route("/")
def registration_form():
    return render_template("registration.html")  # Serve the form
# Run Flask App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
  