import subprocess
import sys
import time
import webbrowser
import os

def run_streamlit():
    # Start Streamlit app
    streamlit_process = subprocess.Popen(
        ['streamlit', 'run', 'app.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=os.environ.copy()
    )

    # Wait for Streamlit to start
    time.sleep(5)  # Adjust if necessary

    # Open the web browser
    webbrowser.open('http://localhost:8501')

    # Wait for the Streamlit process to finish
    streamlit_process.communicate()

if __name__ == "__main__":
    run_streamlit()
