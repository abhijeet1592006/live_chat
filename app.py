.from flask import Flask,request,redirect,session,url_for,render_template

from flask_socketio import SocketIO,join_room,emit

app=Flask(__name__)

app.secret_key="hie"

socketio=SocketIO(app)

@app.route("/",methods=["POST","GET"])

def main():
    if request.method=="POST":

        session['username']=(request.form["username"])
        username=session['username']

        return render_template("chat.html",username=username)

    return render_template("index.html")
@app.route("/chat",methods=["POST","GET"])
def chat():
    if(session.get('username')!=None):
        if request.method=="POST":
            username=session['username']
            
        return render_template("chat.html",username=username)


    else:
        print(session.get("username"))
        return redirect(url_for("main"))
    
@socketio.on("status")
def joinhandel(d):
    print(d['data'])
    user_name=session['username']
    d1={"user_name":user_name}
    socketio.emit("restatus",d1)


@socketio.on("send")
def message(u):
    print(u['u'])
    user_name=session['username']+":- "
    
    u1={'u':u['u'],"name":user_name}
    socketio.emit("recive",u1)
if __name__=="__main__":
    socketio.run(app,host='0.0.0.0')

