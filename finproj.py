from flask import Flask
from flask import url_for, render_template, request, redirect

app = Flask(__name__)

corpus = []

def listedprint(massive):
    for item in massive:
        print(item)

@app.route('/')
def index():
    urls = {'главная (эта страница)': url_for('index'),
            'форма загрузки материалов': url_for('uploading'),
            'форма просмотра материалов': url_for('downloading')}
    return render_template('index.html', urls=urls)

@app.route('/uploading')
def uploading():
    return render_template('uploading.html')

@app.route('/downloading')
def downloading():
    if request.args:
        name = request.args['name']
        age = request.args['age']
        gender = request.args['gender']
        answer = request.args['uploadment']
        with open("gld.csv", 'a', encoding="utf-8") as f:
            line = name + ", " + age + ", " + gender + ", " + answer + "\n"
            f.write(line)
        with open("gld.csv", encoding="utf-8") as ff:
            corpus = ff.readlines()
        listedprint(corpus)
        return render_template('downloading.html', name=name, age=age, gender=gender,
                               uploadment=answer, corpus=corpus)
    return redirect(url_for('uploading'))

if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)