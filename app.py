from flask import Flask, render_template, jsonify, request
import requests
from pymongo import MongoClient
from datetime import date, datetime, timedelta

# client = MongoClient('mongodb://test:test@52.78.138.113',27017)  # mongoDB는 27017 포트로 돌아갑니다.
client = MongoClient('localhost', 27017)

db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/project', methods=['POST'])
def post_project():
    title_receive = request.form['title_give']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    task1_name = request.form['task1_name']
    task2_name = request.form['task2_name']
    task3_name = request.form['task3_name']
    task4_name = request.form['task4_name']
    task5_name = request.form['task5_name']
    task1_progress = request.form['task1_progress']
    task2_progress = request.form['task2_progress']
    task3_progress = request.form['task3_progress']
    task4_progress = request.form['task4_progress']
    task5_progress = request.form['task5_progress']

    doc = {
        'title': title_receive,
        'start_day': start_date,
        'end_day': end_date,
        'task1_name': task1_name,
        'task1_progress': task1_progress,
        'task2_name': task2_name,
        'task2_progress': task2_progress,
        'task3_name': task3_name,
        'task3_progress': task3_progress,
        'task4_name': task4_name,
        'task4_progress': task4_progress,
        'task5_name': task5_name,
        'task5_progress': task5_progress
        # 'average' : average

        # progress = [task1_progress, task2_progress, task3_progress, task4_progress, task5_progress]
        # for score in progress:
        #     total += score
        # average = progress / len(progress)
    }

    db.myprojects.insert_one(doc)

    print(title_receive)

    return jsonify({'result': 'success', 'msg': '저장 완료!'})


@app.route('/projects', methods=['GET'])
def view_projects():
    # 여길 채워나가세요!

    projects = list(db.myprojects.find({}, {"_id": False}))

    # dday 연산 후 프론트에 doc insert for문 삽입 (todolist)

    proj_result = []

    for data in projects:
        end_day = data['end_day']
        dday = datetime.strptime(end_day, '%Y-%m-%d').date()
        # print(dday)

        now = datetime.now().date()

        left_day = ((dday - now).days)

        data['left_day'] = left_day

        proj_result.append(data)

    proj_result.sort(key=lambda x: x.get('left_day')) #대박! 성공했다!
    # proj_result.sorted(key=left_day)


    # dday_doc = {
    #     'left_day': left_day,
    # }
    #
    # db.myprojects.insert_one(dday_doc)

    return_val = {'result': 'success', 'projectList': proj_result}

    print(proj_result)

# @app.route('/projects/edit', methods=['GET'])
# def edit_projects():

    return jsonify(return_val)



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
