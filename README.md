# log-analyzer
 Python tool that detects brute-force login attempts in log files
It counts failed login attempts per IP address and flags any IP that crosses a set threshold.

## How to use
1. Download or clone this repo
2. Run: `python log_analyzer.py sample_logs/auth.log`

## What I learned
- Using regular expressions (regex) to parse log files
- Basic pattern recognition for security threats
- How brute-force attacks look in real server logs

## Future improvements
- Add time-window detection (only flag attempts within X minutes)
- Export results to CSV
- Add IP geolocation lookup
