from flask import Flask, render_template,request

# Initialize Flask App
app = Flask(__name__)
# Route to Render Registration Form
@app.route("/")
def registration_form():
    return render_template("registration.html")  # Serve the form

@app.route("/submit", methods=["POST"])
def submit_form():
    # Extract form data
    name = request.form.get("name")
    password = request.form.get("password")
    confirmpassword = request.form.get("confirmpassword")
 
    
    if(password != confirmpassword):
        return "no"
    return "Success"

# Run Flask App
#this is the change make in github second time

if(__name__ == "__main__"):
  app.run(host="0.0.0.0", port=9000, debug=True)
  
