from flask import *
import atexit
import json

app = Flask(__name__)

chat_list = []

def exit_run():
    content = json.dumps(chat_list)
    with open("saved.json","w")as f:
        f.write(content)
        
@app.route('/')
def index():
    return "Welcome to Teleground"
  
@app.route('/chat/',methods=['GET','POST'])
def chat():
    if request.method == 'GET':
        return render_template("chat.html",chat_list=chat_list)
    else:
        content = request.form.get("content")
        print(content)
        chat_list.append(content)
        exit_run()
        return redirect('/chat/')
      
if __name__ == '__main__':
    try:
        with open("saved.json","r")as f:
            chat_list = json.loads(f.read())
    except:
        chat_list = []
    app.run('0.0.0.0',8000,False)
