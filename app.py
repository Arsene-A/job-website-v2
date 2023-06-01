from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Scientist',
  'location': 'Cotonou, Benin',
  'salary': 'CFA. 1,000,000'
}, {
  'id': 2,
  'title': 'Data Analyst',
  'location': 'Parakou, Benin',
  'salary': 'CFA. 800,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Kandi, Benin',
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Lokossa, Benin',
  'salary': 'CFA. 800,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Arsonval')


@app.route("/api/jobs")
def list_job():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
