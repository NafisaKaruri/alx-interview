#!/usr/bin/python3
"""
Log Parsing Script
"""

import sys
import re


def output(log: dict) -> None:
    """
    Helper function to display stats
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code] > 0:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    regex = re.compile(
        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
        r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] '
        r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
    )

    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {str(code): 0 for code in [
            200, 301, 400, 401, 403, 404, 405, 500]}
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.match(line)
            if match:
                code = match.group(2)
                file_size_str = match.group(3)

                try:
                    file_size = int(file_size_str)
                    log["file_size"] += file_size
                except ValueError:
                    continue  # Skip lines with invalid file size

                if code in log["code_frequency"]:
                    log["code_frequency"][code] += 1

                if line_count % 10 == 0:
                    output(log)

    except KeyboardInterrupt:
        output(log)
    finally:
        output(log)
