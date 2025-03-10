import debugpy 
import os 
import time 
from flask import Flask 

REMOTE_DEBUG = False   

if REMOTE_DEBUG: 
    try: 
        debugpy.listen(("0.0.0.0", 2323))  # Ensure this matches launch.json 
        print("Debugpy listening on port 2323.", flush=True) 
    except Exception as e: 
        print(f"Debugpy failed to start: {e}", flush=True) 
print("Starting process1 PID:", os.getpid(), "PPID:", os.getppid(), flush=True) 

app = Flask(__name__) 

@app.route("/") 
def home(): 
    print("New Request1 PID:", os.getpid(), "PPID:", os.getppid(), flush=True) 
    formatted_time = time.strftime("%H:%M:%S", time.localtime()) 
    return "Hello from service 1" + formatted_time 

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False) 
