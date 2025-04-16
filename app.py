from flask import Flask, render_template, render_template_string
import sqlite3

app = Flask(__name__, template_folder='templates')

# Path to your SQLite database
DB_PATH = r"C:\Python sem1\sem 1\dab111_sales_project\database\sales.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <body>
            <h1>Sales Data Project</h1>
            <p>Welcome! You can view:</p>
            <ul>
                <li><a href="/data">View Sales Data Table</a></li>
                <li><a href="/about">About</a></li>
            </ul>
        </body>
        </html>
    ''')

@app.route('/data')
def data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sales")  # Change table name if needed
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    conn.close()

    return render_template('data.html', rows=rows, columns=columns)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)
