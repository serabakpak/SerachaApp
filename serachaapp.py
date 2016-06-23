from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
import filter_words

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'seracha_wedding'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/rsvp', methods=['POST'])
def filter():
	if request.method == 'POST':
		_name = request.form['name']
		_email = request.form['email']
		_attendance = request.form['attendance']
		_message = request.form['message']
		_plusonename = request.form['plusonename']

		print "bad_word_dict:", filter_words.bad_word_dict
		_filtered_message = filter_words.replace_bad_words(request.form['message'],filter_words.bad_word_dict )

		# Connect to MySQL
		conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO rsvps (name, email, attendance, plus_one_name, message) VALUES (%s, %s, %s, %s, %s)", (_name, _email, _attendance, _plusonename, _filtered_message))
        
        # The fetchall method fetches all (or all remaining) rows of a query result set and returns a list of tuples. If no more rows are available, it returns an empty list.
        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            return redirect(url_for('guestbook'))
        else:
            return redirect(url_for('main'))

@app.route('/guestbook')
def guestbook():
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("SELECT message, name from rsvps ORDER BY id DESC;")
	data = cursor.fetchall()
	print data
	# Get a list of rsvps from the database and then render them inside of the rsvps template
	return render_template('guestbook.html', guests=data)

if __name__ == '__main__':
	app.run()