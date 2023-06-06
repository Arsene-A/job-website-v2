from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  JOBS = load_jobs_from_db()
  return render_template('home.html', jobs=JOBS, company_name='Arsonval')


@app.route("/api/jobs")
def list_job():
  JOBS = load_jobs_from_db()
  return jsonify(JOBS)


@app.route("/job/<id>")
def show_job(id):
  JOB = load_job_from_db(id)

  if not JOB:
    return "Not Found", 404

  return render_template('jobpage.html', job=JOB)
  #return jsonify(JOB)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  JOB = load_job_from_db(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html',
                         application=data,
                         job=JOB)
  #return jsonify(data)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
