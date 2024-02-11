@@ -5,7 +5,7 @@
This file creates your application.
"""

from flask import Flask, render_template, url_for

app = Flask(__name__)

@@ -17,7 +17,7 @@

@app.route('/')
def home():
    return f"<p>My Home page </p> <a href='{url_for('about')}'> About </a>"


@app.route('/about')
    return render_template('about.html')
