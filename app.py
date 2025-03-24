from flask import Flask, render_template, request

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<head><title>Resume Builder</title></head>
<body>
    <h2>Enter Your Details</h2>
    <form method="POST">
        <input type="text" name="name" placeholder="Full Name" required><br>
        <input type="email" name="email" placeholder="Email" required><br>
        <textarea name="skills" placeholder="Skills (comma-separated)" required></textarea><br>
        <button type="submit">Generate Resume</button>
    </form>
</body>
</html>
"""

HTML_RESUME = """
<!DOCTYPE html>
<html>
<head><title>Your Resume</title></head>
<body>
    <h2>Your Resume</h2>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Skills:</strong> {skills}</p>
    <a href="/">Go Back</a>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        skills = request.form.get("skills")
        return HTML_RESUME.format(name=name, email=email, skills=skills)
    return HTML_FORM

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
