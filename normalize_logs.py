# This script normalizes logs

import re

# Define the log format
log_format = r'^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d{3} \[(?P<thread>[^\]]+)\] (?P<level>\w+) (?P<class>[^:]+):(?P<line>\d+) - (?P<message>.*)$'

# Define the normalized log format
normalized_log_format = '{timestamp} [{level}] {class}:{line} - {message}'

# Read the log file
with open('logfile.txt', 'r') as f:
    logs = f.readlines()

# Normalize each log
for log in logs:
    match = re.match(log_format, log)
    if match:
        normalized_log = normalized_log_format.format(
            timestamp=match.group('timestamp'),
            level=match.group('level'),
            class=match.group('class'),
            line=match.group('line'),
            message=match.group('message').strip()
        )
        print(normalized_log)
