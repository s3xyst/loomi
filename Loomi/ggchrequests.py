from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import HumanMessage
from lumidata.data import  get_token, get_auth
import re
import json



giga = GigaChat(
    model="GigaChat-Pro",
    credentials= get_auth(),
    verify_ssl_certs = False,
    profanity_check = True,
)

def ggch_request(text):

    resp = giga.invoke(
        [

            HumanMessage(
                content= text
    ),
    (
        "assistant",
        "Твоя задача подобрать путешествие На территории Краснодарского края НА ОСНОВЕ ПРЕДПОЧТЕНИЙ, КОТОРЫЕ УКАЗЫВАЕТ ПОЛЬЗОВАТЕЛЬ, к выбору города подходи максимально осознанно, пользователь сам намекает на город когда указывает свои предпочтения. Отправляй в сообщении ТОЛЬКО  json-код в следующем формате. place:РАСПОЛОЖЕНИЕ ОТЕЛЯ зто значение всегда отправляй на русском языке. price: ЦЕНА ЗА НОЧЬ. name: НАЗВАНИЕ ОТЕЛЯ, количество звёзд у отеля(от 1 до 5). description: краткое описание путешествия. ticket: ГОРОД ОТПРАВЛЕНИЯ - ГОРОД ПРИБЫТИЯ, ЦЕНА, ДАТА(дата в диапазоне: 15.04.2025- 01.07.2025). Это всё должен быть ОДИН СЛОВАРЬ БЕЗ ВЛОЖЕННЫХ СЛОВАРЕЙ. ЕСЛИ в запросе есть выражения на английском языке, то значения словаря вписывай на английском. "

    )
    ]
    )
    return(resp.content)


def extract_json_from_text(text):
    # Ищем текст между ***
    print(text)
    pattern = r'{(.*?)}'
    matches = re.findall(pattern, text, re.DOTALL)

    if not matches:
        return None

    # Берем первый найденный JSON (между первыми ***)
    json_str = "{"+matches[0].strip()+"}"

    try:
        # Парсим JSON в словарь Python
        json_data = json.loads(json_str)
        return json_data
    except json.JSONDecodeError as e:
        print(f"Ошибка при разборе JSON: {e}")
        return None

def finreq(text):
    return extract_json_from_text(ggch_request(text))

#print(finreq('HEllo, im from Paris, i want to travel in Krasnodar'))


#print(finreq('ПРивет, я из Парижа, хочу в Краснодар'))
