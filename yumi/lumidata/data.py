import  uuid
import  requests

def get_auth():
    return('MzRjYzQ5YzQtNDg0Yy00NGY4LWI0NGEtNGRlZmExYjBlOGE3OjE4NzYzMTkxLTQzNzktNDAyZC05ZTAxLWRjNzY5OTM1YmZhOQ==')

def get_token(auth = get_auth(), scope = 'GIGACHAT_API_PERS'):
    rq_uid = str(uuid.uuid4())
    url =  "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': rq_uid,
        'Authorization': f'Basic {auth}'
    }

    payload = {
        'scope': scope
    }
    response = requests.request("POST", url, headers=headers, data=payload, verify= False)

    return(response.json()['access_token'])



