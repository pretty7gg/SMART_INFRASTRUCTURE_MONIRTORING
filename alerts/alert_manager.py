def generate_alerts(cpu, memory):
    alerts = []
    if cpu > 80:
        alerts.append("HIGH CPU USAGE")
    if memory > 80:
        alerts.append("HIGH MEMORY USAGE")
    return alerts