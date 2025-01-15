from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory poll data
polls = {
    1: {"question": "Is the weather good today?", "yes": 0, "no": 0}
}

@app.route('/')
def homepage():
    poll = polls[1]  # Display the first poll as "Poll of the Day"
    return render_template('home.html', poll=poll)

@app.route('/vote/<string:choice>')
def vote(choice):
    poll = polls[1]  # Poll of the day
    if choice == 'yes':
        poll['yes'] += 1
    elif choice == 'no':
        poll['no'] += 1
    return redirect('/results')

@app.route('/results')
def results():
    poll = polls[1]  # Poll of the day
    return render_template('results.html', poll=poll)

if __name__ == '__main__':
    app.run(debug=True)
