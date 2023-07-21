from types import FunctionType
from typing import *
from collections import namedtuple
from pipe import select, where, take, sort
from numpy import average
from copy import deepcopy
from Rules import get_rules


def claculate_order_discount(order: dict, rules: List[namedtuple])-> dict:
    """
    claculate_order_discoun function calculates discount for the given order.

    :param: order: a dictionary represents an order with some attributes
    :param: rules: a list of qualifying conditions and the corresponding discount rules
    :return: a new dictionary order after updating the discount value

    - Example:
    >> order = {"type": "dress", "size": "xs", "brand": "mango","price": 2000.0, "quantity": 2, "discount": 0}
    >>claculate_order_discount(order, rules)
    {"type": "dress", "size": "xs", "brand": "mango","price": 2000.0, "quantity": 2, "discount": 286.6666666666667}
    
    """

    #Input types assertion:
    assert (isinstance(order, dict)), "order must be a dictionary."
    assert (isinstance(rules, List)), "rules must be a list of namedtuples."

    #Getting the lowest three discounts:
    selected_discounts = list(rules | where(lambda x: x.QualifyingCondition(order)) |
                               select(lambda y: y.DiscountRule(order)) |sort | take(3))
    
    print(selected_discounts)
    #Averaging the selected discounts:
    final_discount = average(selected_discounts)

    #Creating a copy of the given order:
    new_order = deepcopy(order)
    
    #Updating the discount value:
    new_order.update({"discount": final_discount})

    return new_order

def calculate_all_orders_discount(orders: List[dict], get_rules_func: FunctionType)-> List[dict]:
    """
    calculate_all_orders_discount function calculates discounts for a given list of orders.

    :param: order: a list of dictionaries, each of which represents an order with some attributes
    :param: get_rules_func: a function returns a list of qualifying conditions and the corresponding discount rules
    :return: a list of new orders after updating discount values

    - Example:
    >> order = {"type": "dress", "size": "xs", "brand": "mango","price": 2000.0, "quantity": 2, "discount": 0}
    >>  orders = [
              {"type": "dress", "size": "xs", "brand": "mango","price": 2000.0, "quantity": 2, "discount": 0}, 
              {"type": "skirt", "size": "m", "brand": "h&m","price": 1700, "quantity": 1, "discount": 0}, 
              {"type": "top", "size": "s", "brand": "zara","price": 1300, "quantity": 1, "discount": 0}
              ]
    >>calculate_all_orders_discount(orders, get_rules())
    [{'type': 'dress', 'size': 'xs', 'brand': 'mango', 'price': 2000.0, 'quantity': 2, 'discount': 286.6666666666667}, 
    {'type': 'skirt', 'size': 'm', 'brand': 'h&m', 'price': 1700, 'quantity': 1, 'discount': 297.5}, 
    {'type': 'top', 'size': 's', 'brand': 'zara', 'price': 1300, 'quantity': 1, 'discount': 195.0}]
    
    """
    #Input types assertion:
    assert (isinstance(orders, List)), "order must be a list of dictionaries."
    assert (isinstance(get_rules_func, FunctionType)), "get_rules_func must be a function."


    rules = get_rules_func()

    return list(map(lambda order: claculate_order_discount(order, rules), orders))