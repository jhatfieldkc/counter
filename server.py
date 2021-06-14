from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'lolz'


@app.route('/')
def index():
    if not 'counter1' in session:
        session['counter1'] = 0
    session['counter1'] += 1
    return render_template("index.html", counter=session['counter1'])


@app.route('/increment_counter', methods=['POST'])
def increment():
    print(request.form)
    print('in increment()')
    session['counter1'] += 1

    print('redirecting to /')
    return redirect('/')

@app.route('/destroy_session', methods=['GET', 'POST'])
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
