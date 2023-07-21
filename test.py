from DiscountCalculation import calculate_all_orders_discount
from Rules import get_rules



if __name__ == '__main__':

    orders = [
              {"type": "dress", "size": "xs", "brand": "mango","price": 2000.0, "quantity": 2, "discount": 0}, 
              {"type": "skirt", "size": "m", "brand": "h&m","price": 1700, "quantity": 1, "discount": 0}, 
              {"type": "top", "size": "s", "brand": "zara","price": 1300, "quantity": 1, "discount": 0}
              ]
    
    orders_after_discount = calculate_all_orders_discount(orders, get_rules)

    print("Orders after calculating discount: ", orders_after_discount)
    


