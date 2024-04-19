import psutil
import time

def monitor_cpu_usage(interval=5):
    while True:
        cpu_percent = psutil.cpu_percent(interval=interval)
        
        print("CPU Usage:", cpu_percent, "%")
        
        time.sleep(interval)

monitor_cpu_usage()
