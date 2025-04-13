from flask import Flask, request, jsonify
from  ggchrequests import  finreq
from flask_cors import CORS


app = Flask(__name__)
#CORS(app, resources={r"/process_text": {"origins": ["http://localhost:5500"]}})
CORS(app)



@app.route('/process_text', methods=['POST'])
def process_text():
    # Получаем текст из запроса
    data = request.get_json()
    text = data.get('text', '')
    app.logger.debug(f"Received text: {text}")

    # Обрабатываем текст (например, превращаем в словарь)
    result = finreq(text)

    # Возвращаем JSON
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=5500)  # Запуск сервера на порту 5000