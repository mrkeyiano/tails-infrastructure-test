from flask import Flask, request
import sqlite3
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Tails.com!'

@app.route('/wag/', methods=['POST'])
def wag():

    #command input needs to be filtered
    command = (request.form['command'],)

    #correct variable name dATABASE, naming convention needs to be seamless across code
    database = sqlite3.connect('wag_or_not.sqlite')
    c = database.cursor()
    #prevent SQLite injection by using parameterized queries
    c.execute("SELECT wag FROM wag_or_not WHERE command=?", command)

    try:
        has_it_had_a_wag_or_dit_it_not = c.fetchone()[0]

        if has_it_had_a_wag_or_dit_it_not == 1:
              return '{"wag": true}'
        else:
            return '{"wag": false}'

    except TypeError:
        return '{"error": "Invalid command"}'
