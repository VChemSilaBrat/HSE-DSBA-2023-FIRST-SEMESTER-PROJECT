#!/bin/bash
# flask settings
export FLASK_APP=/root/HSE-DSBA-2023-FIRST-SEMESTER-PROJECT/app.py
export FLASK_DEBUG=0

flask run --host=0.0.0.0 --port=2000
