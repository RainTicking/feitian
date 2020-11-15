from flask import Flask 


@app.route("/index")
#线程局部变量 request  
def index():
    request.form.get("name")



