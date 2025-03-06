import debugpy 

import os 

import time 

from flask import Flask 

 
 

REMOTE_DEBUG = False   

 
 

if REMOTE_DEBUG: 

    try: 

        debugpy.listen(("0.0.0.0", 2525))  # Ensure this matches launch.json 

        print("Debugpy listening on port 2525.", flush=True) 

    except Exception as e: 

        print(f"Debugpy failed to start: {e}", flush=True) 

 
 

print("Starting process2 PID:", os.getpid(), "PPID:", os.getppid(), flush=True) 

 
 

app = Flask(__name__) 

 
 

@app.route("/") 

def home(): 

    print("New Request2 PID:", os.getpid(), "PPID:", os.getppid(), flush=True) 

    formatted_time = time.strftime("%H:%M:%S", time.localtime()) 

    return "Hello from Service 2! " + formatted_time 

 
 

if __name__ == "__main__": 

    if REMOTE_DEBUG: 

        print("Waiting for debugger to attach...", flush=True) 

        debugpy.wait_for_client()  

        print("Debugger attached!", flush=True) 

 
 

    app.run(host="0.0.0.0", port=5001, debug=True, use_reloader=False) 

 
 