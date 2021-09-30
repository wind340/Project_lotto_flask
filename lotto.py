from flask import Flask, render_template, request
from randomNum import randomNum

app = Flask(__name__)

@app.route('/lotto', methods=['POST'])
def random_print() -> 'html':
    won = request.form['won']
    title = '무작위 숫자 결과!'
    results = randomNum(int(won))
    return render_template('results.html',
                           the_title=title,
                           the_won = won,
                           the_results=results
                           )

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='로또 번호 생성기!')

if __name__ == '__main__':
    app.run(debug=True)