import requests, httpx, uuid


dialog_history={}

def add_to_history(user_id: int, role:str, content:str):
    if user_id not in dialog_history:
        dialog_history[user_id]=[]

    dialog_history[user_id].append({'role':role, 'content':content})

def get_context(user_id:int):
    return dialog_history.get(user_id,[])

def summarize(text):
    words=text.split()
    if len(words) <=35:
        return words
    return " ".join(words[:35])+ "..."

def get_token():
    r = requests.post(
    "https://ngw.devices.sberbank.ru:9443/api/v2/oauth",
    headers={
        "RqUID": str(uuid.uuid4()),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "Authorization": f"Basic {'MDE5YWQzYTMtNTAzMi03MTAwLWI0NWUtZjdlYWFkZWYxZWYwOjdhZWI5ZWI2LTA0NDMtNGZmYy1iY2VhLWE0YjEyNWIxZGE5NA=='}",
    },
    data={"scope": "GIGACHAT_API_PERS"},
    verify=False,
    timeout=60,
)
    r.raise_for_status()
    token = r.json()["access_token"]
    return token

http_client = httpx.Client(verify=False, timeout=60)