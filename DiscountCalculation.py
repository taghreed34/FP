from types import FunctionType
from typing import *
from collections import namedtuple
from pipe import select, where, take, sort
from numpy import average
from copy import deepcopy
from Rules import get_rules


def claculate_order_discount(order: dict, rules: List[namedtuple])-> dict:

    selected_discounts = list(rules | where(lambda x: x.QualifyingCondition(order)) |
                               select(lambda y: y.DiscountRule(order)) |sort(reverse=True) | take(3))
    
    final_discount = average(selected_discounts)

    new_order = deepcopy(order)
    
    new_order.update({"discount": final_discount})

    return new_order

def calculate_all_orders_discount(orders: List[dict], get_rules_func: FunctionType)-> List[dict]:

    rules = get_rules_func

    return list(map(lambda order: claculate_order_discount(order, rules), orders))