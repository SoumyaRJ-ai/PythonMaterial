from datetime import datetime

import pytz


def lambda_handler(event, context):
    timezones = pytz.all_timezones
    current_time = datetime.now()
    results = {}
    for tz in timezones:
        timezone = pytz.timezone(tz)
        results[tz] = current_time.astimezone(timezone).strftime("%Y-%m-%d %H:%M:%S")
    return {"statusCode": 200, "body": results}


"""
pip install --platform manylinux2014_x86_64 --target=. --implementation cp --python 3.9 --only-binary=:all: --upgrade pytz


  "errorMessage": "Unable to import module 'lambda_function': No module named 'lambda_function'",

    Go to the configuration, and change the lambda hanlder path

"""
