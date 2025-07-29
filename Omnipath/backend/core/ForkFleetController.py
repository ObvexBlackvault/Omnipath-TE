
import subprocess
import time

forks = ["ForkAlpha.py", "ForkBeta.py"]

def launch_fork(filename):
    try:
        subprocess.Popen(["python3", filename])
        print(f"Launched {filename}")
    except Exception as e:
        print(f"Error launching {filename}: {e}")

if __name__ == "__main__":
    for fork in forks:
        launch_fork(fork)
        time.sleep(1)
