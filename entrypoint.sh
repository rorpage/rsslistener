#!/bin/sh
set -e

echo "*/15 * * * * python /listener.py" | crontab - && crond -f -L -
