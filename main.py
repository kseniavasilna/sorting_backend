from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)                       #создано Flack приложение
CORS(app)                                   #для возможности запросов из разных доменов

@app.route("/sort", methods=["POST"])  #создан endpoint /sort который принимает только POST с данными и параметрами сортировки
def sort_colors():
    data = request.json

    values = data.get("values", [])         #считывание из json входной последовательности
    order_rule = data.get("order_rule", {}) #считывание из json Правила порядка

    sorted_values =sort_values(values, order_rule) #вызов функции сортировки

    return jsonify({                        #выходной json с отсортированной последовательностью
        "sorted": sorted_values
    })

def sort_values(values, order_rule):        #функция, на вход получает входную последовательность и правило сортировки
    buckets = {}
    for v in values:
        rank = int(order_rule[v["value"]])  #получение ранга каждой буквы

        if rank not in buckets:             #если ранг еще не записывался, то записать
            buckets[rank] = []

        buckets[rank].append(v)             #группировка в соотвествующий ранг массива с буквой (К или З или С)

    result = []
    for i in sorted(buckets):               #сортировка сгруппированных массивов букв в соотвествиии с правилом
        result.extend(buckets[i])

    return result

if __name__ == "__main__": # старт сервера на дефолтном адресе http://127.0.0.1:5000
    app.run()