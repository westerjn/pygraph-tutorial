app = Flask(__name__)

@app.route('/')
def chart():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)