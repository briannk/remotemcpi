from flask import Flask, request, render_template
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
# handles all touch inputs
@app.route('/processMove', methods=['POST'])
def processMove():
    
    key = request.get_json(force=True)
    
    # handles mouse clicks
#    if((key['value'] == "left")or(key['value'] == "right")):
#        if(key['value'] == "left"):
#            if(key['isRelease'] == "true"):
#                m.release(1920/2, 1080/2,1)
#                print(m.position())
#            else:
#                m.press(1920,1080/2,1)
#        else:
#            if(key['isRelease'] == "true"):
#                m.release(0,0,3)
#            else:
#                m.press(0,0,3)
                
    # handles inventory
    if((key['value'] == 'e')or(key['value'] == "escape")):
        if(key['value'] == 'e'):
            k.tap_key(key['value'])
        else:
            k.tap_key('Escape')
    # handles movement
    else:
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
