from flask import Flask, request, render_template
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/processData', methods=['POST'])
def processData():
    direction = request.get_json(force=True)
    k.tap_key(direction)
    return render_template('index.html')
    
    
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
