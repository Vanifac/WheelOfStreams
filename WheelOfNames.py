import http.client
import json

# https://wheelofnames.stoplight.io/docs/wheelofnames/ck5d76uhtsg3s-update-a-wheel

conn = http.client.HTTPSConnection("wheelofnames.com")


def get_shared_wheels(api_key: str):
    headers = {
        "x-api-key": api_key,
        "Accept": "application/json"
    }

    conn.request("GET", "/api/v1/wheels/shared", headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))

    return data


def get_private_wheels(api_key: str):
    headers = {
        'x-api-key': api_key,
        'Accept': "application/json"}

    conn.request("GET", "/api/v1/wheels/private", headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))

    return data


def send_shared_wheel(api_key: str, path: str, wheel: dict):
    payload = json.dumps(wheel)
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json"}
    conn.request("PUT", f"/api/v1/wheels/{path}", payload, headers)

    res = conn.getresponse()
    data: dict = json.loads(res.read().decode("utf-8"))

    if 'error' in data.keys():
        return data['error']
    else:
        return "Successful Upload!"


def send_private_wheel(api_key: str, wheel: dict):
    payload = json.dumps(wheel)
    headers = {
        'x-api-key': api_key,
        'Content-Type': "application/json",
        'Accept': "application/json, application/xml"}
    conn.request("PUT", "/api/v1/wheels/private", payload, headers)

    res = conn.getresponse()
    data: dict = json.loads(res.read().decode("utf-8"))

    if 'error' in data.keys():
        return data['error']
    else:
        return "Successful Upload!"
