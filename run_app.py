import subprocess
import sys
import time
import webbrowser

# Inicia o Streamlit em background
proc = subprocess.Popen([
    sys.executable, "-m", "streamlit", "run", "app.py", "--server.headless=false"
])


proc.wait()