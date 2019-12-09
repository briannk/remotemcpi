from flask import Flask, request, render_template
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/processMove', methods=['POST'])
def processMove():
    
    key = request.get_json(force=True)
    if(key['isRelease'] == "true"):
        k.release_key(key['value'])
    else:
        k.press_key(key['value'])
    
    return render_template('index.html')

@app.route('/processCamera', methods=['POST'])
def processCamera():
    
    pos = request.get_json(force=True)
    print(pos['x'])
    
    return render_template('index.html')

    
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
