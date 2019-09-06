

def order_price_calculation(fabric_complexity_factor, product_base_price, complication_element_base_price,
                            complication_element_complexity, order_processing_category,
                            allowance_discount_coefficients):

    complication_element_price = 0
    order_allowance_discount = 0

    for i in range(len(complication_element_base_price)):
        complication_element_price += complication_element_base_price[i] * complication_element_complexity[i]

    starting_price = (product_base_price + complication_element_price) * fabric_complexity_factor

    if order_processing_category == 1:
        starting_price = 1.2 * starting_price   # +20% for first processing category

    for coefficient in allowance_discount_coefficients:
        order_allowance_discount += coefficient * starting_price

    order_price = starting_price + order_allowance_discount

    return "%.2f" % order_price
