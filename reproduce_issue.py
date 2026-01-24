import sys
import os
import traceback

log_file = open('debug_output.txt', 'w')

def log(msg):
    log_file.write(msg + '\n')
    log_file.flush()
    print(msg)

log("Starting debug script")
log(f"Python executable: {sys.executable}")

# Add backend to path
backend_path = os.path.join(os.getcwd(), 'complaint_manager', 'backend')
sys.path.append(backend_path)
log(f"Added to path: {backend_path}")

try:
    log("Attempting to import app.main")
    from app import main
    log("Successfully imported app.main")
except Exception as e:
    log(f"Failed to import app.main: {e}")
    traceback.print_exc(file=log_file)

try:
    log("Attempting to import app.models")
    from app import models
    log("Successfully imported app.models")
except Exception as e:
    log(f"Failed to import app.models: {e}")
    traceback.print_exc(file=log_file)

log("Finished debug script")
log_file.close()
