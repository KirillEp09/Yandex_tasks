from flask import Flask, render_template

app = Flask(__name__)

answer = {'Surname': 'Дуров', 'Name': 'Павел', 'Education': 'Филологическое', 'Profession': 'Штурман марсохода',
          'Sex': 'male', 'Motivation': 'Серьезная', 'Ready': 'True'}

@app.route('/')
@app.route('/index')
def main_str():
    title = "Колонизация Марса"
    return render_template('base3.html', title=title)

@app.route('/answer')
def answ():
    return render_template('base6.html', answer=answer)

@app.route('/auto_answer')
def auto_answ():
    return render_template('base4.html', answer=answer)


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
