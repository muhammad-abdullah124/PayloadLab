import requests

def send_to_burp(payload, endpoint, param_name="q"):
    try:
        r = requests.get(endpoint, params={param_name: payload}, verify=False, timeout=5)
        return {
            "url": r.url,
            "status_code": r.status_code,
            "length": len(r.text),
            "payload": payload
        }
    except Exception as e:
        return {"error": str(e), "payload": payload}