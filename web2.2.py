from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    prof = "nothing"
    return render_template('base.html', title='Заготовка', prof=prof)

@app.route('/training/<prof>')
def train_specialist(prof):
    return  render_template('base.html', title='Заготовка', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')    