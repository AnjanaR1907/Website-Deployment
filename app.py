from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        skills = request.form.get("skills")
        experience = request.form.get("experience")
        education = request.form.get("education")
        return render_template("resume.html", name=name, email=email, phone=phone, 
                               skills=skills, experience=experience, education=education)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
