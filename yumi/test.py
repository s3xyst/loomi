from gigachat.context import authorization_cvar
from langchain_gigachat.chat_models.gigachat import GigaChat
from pyexpat.errors import messages

from lumidata.data import  get_token, get_auth

auth = get_auth()
#giga_token = get_token()
giga = GigaChat(
    credential = auth,
    model= 'GigaChat',
    verify_ssl_certs = False,
)

giga.invoke("Привет, расскажи про капибар.")