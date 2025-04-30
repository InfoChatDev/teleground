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
    return render_template('index.html')
  
@app.route('/chat_anymous/',methods=['GET','POST'])
def chat():
    if request.method == 'GET':
        return render_template("chat.html",chat_list=chat_list)
    else:
        content = request.form.get("content")
        print(content)
        chat_list.append(content)
        exit_run()
        return redirect('/chat_anymous/')
      
if __name__ == '__main__':
    with open("saved.json","r")as f:
        chat_list = json.loads(f.read())
    app.run('0.0.0.0',8000,True)