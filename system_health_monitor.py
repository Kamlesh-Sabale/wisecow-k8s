import psutil
import time

# Thresholds
CPU_THRESHOLD = 80  # percent
MEMORY_THRESHOLD = 80  # percent
DISK_THRESHOLD = 80  # percent


def check_system_health():
    alerts = []
    # CPU usage
    cpu = psutil.cpu_percent(interval=1)
    if cpu > CPU_THRESHOLD:
        alerts.append(f"High CPU usage: {cpu}%")

    # Memory usage
    memory = psutil.virtual_memory().percent
    if memory > MEMORY_THRESHOLD:
        alerts.append(f"High Memory usage: {memory}%")

    # Disk usage (root)
    disk = psutil.disk_usage('/').percent
    if disk > DISK_THRESHOLD:
        alerts.append(f"High Disk usage: {disk}%")

    # Running processes
    processes = len(psutil.pids())
    # You can set a process threshold if needed

    if alerts:
        print("ALERTS:")
        for alert in alerts:
            print(alert)
    else:
        print("System health is OK.")

if __name__ == "__main__":
    check_system_health()
