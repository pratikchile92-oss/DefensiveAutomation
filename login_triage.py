def classify_login(failed_attempts, success_after_failures=False):
    if failed_attempts is None:
        return "Manual Review"

    if failed_attempts < 0:
        return "Invalid Data"

    if failed_attempts > 5:
        return "High Risk"

    if failed_attempts >= 3 and success_after_failures:
        return "High Risk"

    if failed_attempts >= 3:
        return "Medium Risk"

    return "Low Risk"


# Sample login alerts
alerts = [
    {"user": "Amit", "failed": 1, "success": False},
    {"user": "Rahul", "failed": 4, "success": False},
    {"user": "Neha", "failed": 8, "success": False},
    {"user": "Priya", "failed": 4, "success": True},
    {"user": "Unknown", "failed": None, "success": False}
]

print("SUSPICIOUS LOGIN ALERT TRIAGE")
print("-" * 35)

for alert in alerts:
    result = classify_login(alert["failed"], alert["success"])
    print(f'User: {alert["user"]} | Failed Attempts: {alert["failed"]} | Result: {result}')