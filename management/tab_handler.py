from menu import products

def calculate_tab(tab):
    total = 0
    for item in tab:
        for product in products:
            if item['_id'] == product['_id']:
                total += item['amount'] * product['price']
    return {"subtotal": f'${round(total, 2)}'}
