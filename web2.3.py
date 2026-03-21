from flask import Flask, render_template

app = Flask(__name__)

professions = [
    "инженер-исследователь",
    "пилот космического корабля",
    "строитель",
    "экзобиолог",
    "врач-иммунолог",
    "геолог",
    "специалист по жизнеобеспечению",
    "физик-ядерщик",
    "робототехник",
    "психолог",
    "метеоролог"
]

@app.route('/list_prof/<list>')
def ind(list):
    return render_template('base2.html', list=list, professions=professions)

if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')