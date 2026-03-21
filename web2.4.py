from flask import Flask, render_template

app = Flask(__name__)

answer = {'surname': 'Дуров', 'name': 'Павел', 'education': 'Филологическое', 'profession': 'Штурман марсохода',
          'sex': 'male', 'motivation': 'Серьезная', 'ready': 'True'}

@app.route('/')
@app.route('/index')
def main_str():
    title = "Колонизация Марса"
    return render_template('base3.html', title=title)


@app.route('/auto_answer')
def hello():
    return render_template('base4.html', answer=answer)


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
