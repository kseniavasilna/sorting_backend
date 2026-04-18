from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/sort", methods=["POST"])
def sort_colors():
    data = request.json

    values = data.get("values", [])
    order_rule = data.get("order_rule", {})

    sorted_values =sort_values(values, order_rule)

    return jsonify({
        "sorted": sorted_values
    })

def sort_values(values, order_rule):
    buckets = {}
    for v in values:
        rank = int(order_rule[v["value"]])

        if rank not in buckets:
            buckets[rank] = []

        buckets[rank].append(v)

    result = []
    for i in sorted(buckets):
        result.extend(buckets[i])

    return result

if __name__ == "__main__":
    app.run()