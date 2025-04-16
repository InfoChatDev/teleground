from flask import *
app = Flask(__name__)
chat_list = ["114514","asf","asdf","asdf"]
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
        return redirect("/chat/")
app.run('0.0.0.0',8000,True)