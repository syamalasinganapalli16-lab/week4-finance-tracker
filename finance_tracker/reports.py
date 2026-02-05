def category_report(expenses):
    result = {}

    for e in expenses:
        result[e["category"]] = result.get(e["category"], 0) + e["amount"]

    for k, v in result.items():
        print(k, ":", v)
