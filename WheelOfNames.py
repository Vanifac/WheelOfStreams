import http.client
import json

# https://wheelofnames.stoplight.io/docs/wheelofnames/ck5d76uhtsg3s-update-a-wheel

conn = http.client.HTTPSConnection("wheelofnames.com")


def get_wheels(api_key: str):
    headers = {
        'x-api-key': api_key,
        'Accept': "application/json"}

    conn.request("GET", "/api/v1/wheels/private", headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))

    return data


def send_wheel(api_key: str, wheel: dict):
    payload = json.dumps(wheel)
    headers = {
        'x-api-key': api_key,
        'Content-Type': "application/json",
        'Accept': "application/json, application/xml"}

    conn.request("PUT", "/api/v1/wheels/private", payload, headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")

    if data[0] == "{":
        return "Successful Upload!"
    else:
        return data
