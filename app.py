from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    mobile = request.form['mobile']
    age = request.form['age']
    city = request.form['city']
    marital_status = request.form['marital_status']

    # Save data to database
    save_to_database(name, mobile, age, city, marital_status)

    return redirect(url_for('show_data'))

def save_to_database(name, mobile, age, city, marital_status):
    conn = sqlite3.connect('userdata.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            mobile TEXT,
            age INTEGER,
            city TEXT,
            marital_status TEXT
        )
    ''')
    c.execute('INSERT INTO users (name, mobile, age, city, marital_status) VALUES (?, ?, ?, ?, ?)', (name, mobile, age, city, marital_status))
    conn.commit()
    conn.close()

@app.route('/data')
def show_data():
    conn = sqlite3.connect('userdata.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    conn.close()
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
