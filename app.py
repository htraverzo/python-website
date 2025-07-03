from flask import Flask, render_template, jsonify

app = Flask(__name__)

COURSE = [{
    'id': 1,
    'title': 'Data Structures',
    'description': 'Learn about data structures',
    'price': '3000',
}, {
    'id': 2,
    'title': 'Data Analitycs',
    'description': 'Learn about data analytics',
}, {
    id: 3,
    'title': 'Data Sciences',
    'description': 'Learn about data Sciences',
    'price': '3000',
}]


@app.route("/")
def project_python():
    return render_template('home.html', courses=COURSE)


@app.route("/api/courses")
def list_courses():
    return jsonify(COURSE)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
