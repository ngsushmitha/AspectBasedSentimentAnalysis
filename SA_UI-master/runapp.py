from flask import Flask, render_template
import Feature_files
import Classification as C


app = Flask(__name__)


@app.route('/')


@app.route('/index.html')
def home():
    return render_template('index.html', r1=C.rate1, r2=C.rate2, r3=C.rate3, r4=C.rate4)


@app.route('/hotel1.html')
def hotel1():
    return render_template('hotel1.html', h1=C.hotel1_average, c1=C.content1)


@app.route('/hotel2.html')
def hotel2():
    return render_template('hotel2.html', h2=C.hotel2_average, c2=C.content2)


@app.route('/hotel3.html')
def hotel3():
    return render_template('hotel3.html', h3=C.hotel3_average, c3=C.content3)


@app.route('/hotel4.html')
def hotel4():
    return render_template('hotel4.html', h4=C.hotel4_average, c4=C.content4)


@app.route('/chart.html')
def chart():
    return render_template('chart.html', h3=C.hotel3_average, c3=C.content3)



@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html')

app.run()
