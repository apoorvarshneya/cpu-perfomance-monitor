import psutil
import time
import threading

def real_time_ghz_monitor(interval=1):
    try:
        while True:
            freq = psutil.cpu_freq()
            current_ghz = freq.current / 1000  # Convert MHz to GHz
            print(f"Current CPU Frequency: {current_ghz:.2f} GHz")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Frequency monitoring stopped.")

def display_usage(interval=1, performance=50):
    try:
        while True:
            # Get the current CPU and Memory usage
            cpu_usage = psutil.cpu_percent()
            mem_usage = psutil.virtual_memory().percent

            # Calculate the percentage for CPU and Memory
            cpu_percent = cpu_usage / 100.0
            cpu_bar = int(cpu_percent * performance)
            mem_percent = mem_usage / 100.0
            mem_bar = int(mem_percent * performance)

            # Build the bar strings
            cpu_display = "🚀" * cpu_bar + "-" * (performance - cpu_bar)
            mem_display = "🚀" * mem_bar + "-" * (performance - mem_bar)

            # Print the formatted output for CPU and memory usage
            print(f"CPU PERFORMANCE: |{cpu_display}| {cpu_usage:.2f}%")
            print(f"MEM PERFORMANCE: |{mem_display}| {mem_usage:.2f}%")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Usage monitoring stopped.")

if __name__ == "__main__":
    # Create threads for both monitoring functions
    ghz_thread = threading.Thread(target=real_time_ghz_monitor)
    usage_thread = threading.Thread(target=display_usage)

    # Start the threads
    ghz_thread.start()
    usage_thread.start()

    # Wait for both threads to complete
    ghz_thread.join()
    usage_thread.join()