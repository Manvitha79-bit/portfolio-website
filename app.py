from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
                   (name, email, message))
    conn.commit()
    conn.close()

    return jsonify({"message": "Message sent successfully!"})

# View all contacts (for mentor/demo)
@app.route('/contacts')
def contacts():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    data = cursor.fetchall()
    conn.close()
    return {"data": data}

if __name__ == '__main__':
    init_db()
    app.run(debug=True)