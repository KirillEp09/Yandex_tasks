from flask import Flask, render_template

app = Flask(__name__)

distribution = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']


@app.route('/distribution')
def distrib():
    title = 'Колонизация Марса'
    return render_template('base5.html', distr=distribution, title=title)


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')