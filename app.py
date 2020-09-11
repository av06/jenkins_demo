"""Flask App that Runs Bubble Sort"""
from flask import Flask, render_template, request
from bubblesort import bubble_sort
app = Flask(__name__)

""" The route() function of the Flask class is a decorator. """
@app.route('/',methods=['post', 'get'])
def index():
    """Renders HTML file and takes ',' seperated list of numbers as input."""
    message = ''
    if request.method == 'POST':
        inputs = request.form.get('n').split(",")
        int_input = list(map(int,inputs))
        result = ",".join(list(map(str,bubble_sort(int_input))))
        message = result
    return render_template('index.html',message=message)

if __name__=='__main__':
    app.run(host='0.0.0.0', port='5000')
