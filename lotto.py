from flask import Flask, render_template, request
from randomNum import randomNum

#Flask를 이용한 사이트 구축.
#사이트에서 정수 받아오고 랜덤함수페이지를 거쳐 결과물 페이지에 출력하기
#한 페이지에 다 담을수 있지만 flask를 이용하여 다른페이지에 함수를 만들어 호출하고
#html을 통해 상속하여 연결하는 방법들을 숙련하는 목적이다.

app = Flask(__name__)

@app.route('/lotto', methods=['POST'])
def random_print() -> 'html':
    won = request.form['won']           #html에서 input된 won을 받아온다.
    title = '무작위 숫자 결과!'          #title에 str 담아서 return할때 the_title객체들에 다 뿌려준다.
    results = randomNum(int(won))       #won을 randomNum함수를 호출해서 results에 담아준다.
    return render_template('results.html',      #return될 페이지 연결. html안에서 호출될 값을 담아준다. 
                           the_title=title,
                           the_won = won,
                           the_results=results
                           )

@app.route('/')
@app.route('/entry')                    #연결이 되면 entry로 이동
def entry_page() -> 'html':
    return render_template('entry.html',    #return될 페이지 연결. the_title이라는 변수에담아호출될 값을 정의해주었다
                           the_title='로또 번호 생성기!')

if __name__ == '__main__':
    app.run(debug=True)