from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[
  {
    "ID":1,
    "Postion":"Data Analyst",
    "Location":"Bengaluru,India",
    "Salary":"Rs 10,00,000",
    "Responsibility":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
    "Requirements": "Python,SQL,ML,DL,NLP,FLASK,REST API,AZURE"
  },
  {
    "ID":2,
    "Postion":"Data Scientist",
    "Location":"Delhi,India",
    "Salary":"Rs 15,00,000",
    "Requirements": "Python,SQL,ML,DL,NLP,FLASK,REST API,AZURE",
    "Responsibility":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
  },
  {
    "ID":3,
    "Postion":"Front end Engineer",
    "Location":"Bengaluru,India",
    "Salary":"Rs 10,00,000",
    "Requirements": "Python,SQL,ML,DL,NLP,FLASK,REST API,AZURE",
    "Responsibility":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
  },
  {
    "ID":4,
    "Postion":"Backend Engineer",
    "Location":"San Fransico,USA",
    "Salary":"$ 10,00,000",
    "Requirements": "Python,SQL,ML,DL,NLP,FLASK,REST API,AZURE",
    "Responsibility":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name='LearnIT')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

@app.route("/job/<int:id>")
def job_page(id):
  job = next((job for job in JOBS if job["ID"]==id),None)
  # job = JOBS.get(id)
  if job is None:
      return "Job is not Found",404
  return render_template('jobpage.html',job=job,company_name='LearnIT')

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)