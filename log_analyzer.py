import re
from collections import defaultdict

FAILED_LOGIN_PATTERN = r'Failed password for .* from (\d+\.\d+\.\d+\.\d+)'
THRESHOLD = 5

def analyze_log(file_path):
    ip_attempts = defaultdict(int)

    with open(file_path, 'r') as f:
        for line in f:
            match = re.search(FAILED_LOGIN_PATTERN, line)
            if match:
                ip = match.group(1)
                ip_attempts[ip] += 1

    print("=== Log Analysis Report ===\n")
    suspicious_found = False

    for ip, count in ip_attempts.items():
        status = "⚠️  SUSPICIOUS" if count >= THRESHOLD else "OK"
        if count >= THRESHOLD:
            suspicious_found = True
        print(f"IP: {ip:15} | Failed attempts: {count:3} | {status}")

    if not suspicious_found:
        print("\nNo suspicious activity detected.")
    else:
        print(f"\n⚠️  {sum(1 for c in ip_attempts.values() if c >= THRESHOLD)} IP(s) exceeded the threshold of {THRESHOLD} failed attempts.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py <path_to_log_file>")
    else:
        analyze_log(sys.argv[1])

  Add log analyzer script
