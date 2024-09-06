from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[
  {
    "ID":1,
    "Postion":"Data Analyst",
    "Location":"Bengaluru,India",
    "Salary":"Rs 10,00,000"
  },
  {
    "ID":2,
    "Postion":"Data Scientist",
    "Location":"Delhi,India",
    "Salary":"Rs 15,00,000"
  },
  {
    "ID":3,
    "Postion":"Front end Engineer",
    "Location":"Bengaluru,India",
    "Salary":"Rs 10,00,000"
  },
  {
    "ID":1,
    "Postion":"Backend Engineer",
    "Location":"San Fransico,USA",
    "Salary":"$ 10,00,000"
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name='LearnIT')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)