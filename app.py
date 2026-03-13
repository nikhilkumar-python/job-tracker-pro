from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.String(50))
    status = db.Column(db.String(50))
    job_link = db.Column(db.String(200))
    notes = db.Column(db.Text)
    date_applied = db.Column(db.String(50))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)    


@app.route("/")
def home():

    if "user_id" not in session:
        return redirect("/login")

    search = request.args.get("search")

    if search:
        jobs = Job.query.filter(
        Job.company.contains(search),
        Job.user_id == session["user_id"]).all()
    else:
        jobs = Job.query.filter_by(user_id=session["user_id"]).all()

    total_jobs = len(jobs)

    interviews = len([job for job in jobs if job.status == "Interview"])
    rejected = len([job for job in jobs if job.status == "Rejected"])
    offers = len([job for job in jobs if job.status == "Offer"])

    return render_template(
        "dashboard.html",
        jobs=jobs,
        total_jobs=total_jobs,
        interviews=interviews,
        rejected=rejected,
        offers=offers
    )

@app.route("/add", methods=["GET", "POST"])
def add_job():

    if request.method == "POST":

        company = request.form["company"]
        role = request.form["role"]
        salary = request.form["salary"]
        status = request.form["status"]
        job_link = request.form["job_link"]
        notes = request.form["notes"]
        date_applied = request.form["date_applied"]

        new_job = Job(
    company=company,
    role=role,
    salary=salary,
    status=status,
    job_link=job_link,
    notes=notes,
    date_applied=date_applied,
    user_id=session["user_id"]
)

        db.session.add(new_job)
        db.session.commit()

        return redirect("/")

    return render_template("add_job.html")

@app.route("/delete/<int:id>")
def delete_job(id):

    job = Job.query.get(id)

    db.session.delete(job)
    db.session.commit()

    return redirect("/") 

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_job(id):

    job = Job.query.get(id)

    if request.method == "POST":

        job.company = request.form["company"]
        job.role = request.form["role"]
        job.salary = request.form["salary"]
        job.status = request.form["status"]
        job.job_link = request.form["job_link"]
        job.notes = request.form["notes"]
        job.date_applied = request.form["date_applied"]

        db.session.commit()

        return redirect("/")

    return render_template("edit_job.html", job=job)

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            return "Username already exists. Try another."

        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            return redirect("/")

        else:
            return "Invalid username or password"

    return render_template("login.html")

@app.route("/logout")
def logout():

    session.pop("user_id", None)

    return redirect("/login")          


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)