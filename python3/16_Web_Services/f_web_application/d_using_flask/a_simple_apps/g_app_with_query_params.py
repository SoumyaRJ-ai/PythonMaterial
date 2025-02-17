#!/usr/bin/python
"""
Purpose: Create a Flask App
    with /echo endpoint which should accept only 'message' as parameter

"""
from flask import Flask, make_response, request

app = Flask(__name__)

banner = {"active": False}


@app.route("/echo")
def echo():
    arguments = request.args.to_dict()
    message = arguments.pop("message", "")
    if (not message) or len(arguments) != 0:
        response = make_response("")
        response.status_code = 406
    elif request.method != "GET":
        response = make_response("")
        response.status_code = 200
    else:
        response = make_response(message)
        response.status_code = 200
    if banner["active"]:
        response.headers["banner"] = True
    return response


@app.route("/set_banner", methods=["POST"])
def admin():
    print(f"{banner =}")
    response = make_response("")
    if request.method != "POST":
        response.status_code = 405
    else:
        request_headers = dict(request.headers)
        print(f"{request_headers =}")
        if request_headers.get("Admin-Auth", "") != "1234":
            response.status_code = 403
        else:
            response.status_code = 200
            body_params = request.get_json(force=True)
            if "banner" in body_params:
                banner["active"] = True
                # response.headers['banner'] = True
    return response


if __name__ == "__main__":
    app.run(debug=False)

# curl http://127.0.0.1:5000/echo
# curl http://127.0.0.1:5000/echo?message=Hello%20World
# curl http://127.0.0.1:5000/echo?message=Hello%20World&extra_param=value


# curl -X POST -H "Content-Type: application/json" -H "Admin-Auth: 1234" -d '{"banner": true}' http://127.0.0.1:5000/set_banner
# curl -X POST -H "Content-Type: application/json" -d '{"banner": true}' http://127.0.0.1:5000/set_banner
# curl -X POST -H "Content-Type: application/json" -d '{"banner_text": "Welcome to our website!"}' http://127.0.0.1:5000/set_banner
