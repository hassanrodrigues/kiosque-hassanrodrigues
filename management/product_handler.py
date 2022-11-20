from menu import products


def get_product_by_id(id):
    try:
        if not isinstance(id, int):
            raise TypeError("product id must be an int")
        return next((product for product in products if product['_id'] == id), {})
    except TypeError as error:
        raise error


def get_products_by_type(type):
    try:
        if not isinstance(type, str):
            raise TypeError("product type must be a str")
            
        return [product for product in products if product['type'] == type]
    except TypeError as error:
        raise error


def menu_report():
    count = len(products)
    #print('price total',sum([product['price'] for product in products]))
    price_average = sum([product['price'] for product in products])/count
    most_type_common = max(set([product['type'] for product in products]), key=[product['type'] for product in products].count)
    return f"Products Count: {count} - Average Price: ${round(price_average,2)} - Most Common Type: {most_type_common}"


def add_product(product_list, **new_product):
    #print(len(product_list) + 1)
    new_product['_id'] = len(product_list) + 1
    product_list.append(new_product)
    return new_product


def add_product_extra():
    ...
