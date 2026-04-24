from flask import Flask,render_template,jsonify
app=Flask(__name__)
JOBS=[
    {
        'id':1,
        'title':"DATA ANALYST",
        'location':"Bengaluru India",
        'salary':'Rs 1,00,000' 
    },
    {
        'id':2,
        'title':"FRONTEND ENGINEER",
        'location':"Delhi India",
        'salary':'Rs 15,00,000'
    },
    {
        
        'id':3,
        'title':"BACKEND ENGINNER",
        'location':"San Francisco USA",
        'salary':'Rs $105,000'
    },
    {
        'id':4,
        'title':"DEVOPS",
        'location':"Chicago USA",
        'salary':'Rs $105,000'
    }
]
@app.route("/")
def hello_world():
    return render_template("home.html",jobs=JOBS)

@app.route("/api/jobs")
def list_items():
    return jsonify(JOBS)
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
