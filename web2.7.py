from flask import Flask, render_template

app = Flask(__name__)
title = 'Колонизация Марса'


@app.route('/male/<age>')
def func1(age):
    if int(age) < 21:
        a = 'img/mars_child.jpg'
    elif int(age) >= 21:
        a = 'img/mars_adult.jpg'
    return render_template('base7.html', title=title, x=1, lin=a, age=int(age))


@app.route('/female/<age>')
def func2(age):
    if int(age) < 21:
        a = 'img/mars_child.jpg'
    elif int(age) >= 21:
        a = 'img/mars_adult.jpg'
    return render_template('base7.html', title=title, x=0, lin=a, age=int(age))


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
