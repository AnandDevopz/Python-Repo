import psutil

def monitor_and_kill_processes():
    for process in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            process_info = process.info
            pid = process_info['pid']
            cpu_percent = process_info['cpu_percent']
            memory_percent = process_info['memory_percent']

            # Define the CPU and memory thresholds for termination
            cpu_threshold = 95
            memory_threshold = 95

            if cpu_percent > cpu_threshold or memory_percent > memory_threshold:
                print(f"Process {pid} ({process_info['name']}) exceeded thresholds: CPU {cpu_percent}%, Memory {memory_percent}%")
                
                # Terminate the process
                process = psutil.Process(pid)
                process.terminate()
                print(f"Process {pid} terminated.")

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    monitor_and_kill_processes()
