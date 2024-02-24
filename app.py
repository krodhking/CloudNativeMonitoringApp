import psutil;
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_per = psutil.virtual_memory().percent
    Message = None
    if(cpu_percent > 80 or mem_per > 80):
        Message = "high memory or cpu utilization, please scale up"
    
    return render_template("index.html", cpu_metric=cpu_percent, mem_metric=mem_per, message=Message)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, host = '0.0.0.0')