import time

from monitor.cpu_monitor import get_cpu_usage
from monitor.memory_monitor import get_memory_usage

from alerts.alert_manager import generate_alerts


def save_logs(message):

    with open("logs/system_logs.txt", "a") as file:

        file.write(message + "\n")


while True:

    cpu = get_cpu_usage()

    memory = get_memory_usage()

    alerts = generate_alerts(cpu, memory)

    output = f"""
==========================
SMART INFRA MONITOR
==========================

CPU Usage: {cpu}%
Memory Usage: {memory}%
"""

    print(output)

    save_logs(output)

    if alerts:

        print("ALERTS:")

        for alert in alerts:

            print(alert)

            save_logs(alert)

    time.sleep(5)