from flask import Flask
from flask import render_template
from flask import request
from pypdf import PdfReader
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
   present_skills = []
   missing_skills = []
   score = 0
   if request.method == "POST":
      name = request.form["name"]
      email = request.form["email"]
      target = request.form["target"].strip().title()
      if target == "Python Developer":
          skills = ["Python Syntax", "Variables and data types", "Operators", "Conditional Statements","Loops", "Functions", "Lambda Functions", "String Manipulation", "File Handling", "Modules & Packages", "Python Coding Standards (PEP 8)"]
      elif target == "Data Analyst":
          skills = ["Python", "SQL", "Excel", "Pandas", "Statistics", "Problem Solving and Analytical thinking", "Communication Skills"]
      elif target == "Frontend Developer":
          skills = ["HTML", "CSS", "JavaScript", "Git and GitHUB", "React"]
      elif target == "Backend Developer":
          skills = ["Python", "Flask", "Django", "APIs"]
      else:
          return "Role is not matched,Sorry"
      resume = request.files["resume"]
      resume.save("uploads/" + resume.filename)
      reader = PdfReader("uploads/" + resume.filename)

      resume_text = ""
      for page in reader.pages:
          resume_text += page.extract_text()
      
      for skill in skills:
          if skill in resume_text:
             present_skills.append(skill)
          else:
             missing_skills.append(skill)
      score = round(len(present_skills)/len(skills)*100)
   return render_template("index.html", present_skills = present_skills, missing_skills = missing_skills, score=score)
if __name__ == "__main__":
   app.run(debug=True)
    


 