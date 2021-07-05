from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    from urllib.request import urlopen

    # import json
    import json
    # store the URL in url as
    # parameter for urlopen
    url = "https://cms.mlcs.xyz/api/view/teaching_staff/all/"
    url1 = "https://cms.mlcs.xyz/api/view/program_sessions/all/"
    url2 = "https://cms.mlcs.xyz/api/view/students_of/bscs-2016/all/"
    # store the response of URL
    response = urlopen(url)
    response1 = urlopen(url1)
    response2 = urlopen(url2)

    # storing the JSON response
    # from url in data
    data_json = json.loads(response.read())
    data_json1 = json.loads(response1.read())
    data_json2 = json.loads(response2.read())
    # print the json response
    bs_batch = []
    bs_batch1 = []
    bs_batch2 = []
    for teacher in data_json:
        f=str(teacher).find('teacher_designation')
        g=f-4
        bs_batch.append(str(teacher)[35:g])
    for session in data_json1:
        i=str(session).find('Session_Title')
        pi=str(session).find('Session_Year')
        pii=pi-4
        ii=i+15
        bs_batch1.append(str(session)[ii:pii])
    for student in data_json2:
        q=str(student).find('student_name')
        w=str(student).find('student_father')
        w=w-4
        q=q+15
        bs_batch2.append(str(student)[q:w])
    print (bs_batch+bs_batch1)
    return render_template("index.html", bs_batch=bs_batch, bs_batch1=bs_batch1, bs_batch2=bs_batch2)

@app.route("/session",  methods=['POST'])
def intro():
    teacher  = request.form.get("program")
    return "You selected as a Supervisor "  + str(teacher)


 
if __name__ == "__main__":
    app.run(debug=True)
