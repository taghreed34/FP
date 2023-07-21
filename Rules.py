from collections import namedtuple
from typing import *



def IsTypeQualified(order: dict)-> bool:
    """
    IsTypeQualified function checks whether the order belongs to a specific list of types.

    :param: order: a dictionary represents an order with some attributes
    :return: a boolean value based on the given product type

    - Example:
    >> order = {"type": "dress", "size": "xs", "brand": "mango","price": 2000.0, "quantity": 2, "discount": 0}
    >>IsTypeQualified(order)
    True
    
    """

    #Input types assertion:
    assert (isinstance(order, dict)), "order must be a dictionary."

    return order["type"] in ["dress", "skirt"]

def GetTypeDiscount(order: dict)->float:
    """
    GetTypeDiscount function calculates discount for the given order.

    :param: order: a dictionary represents an order with some attributes
    :return: discount value

    - Example:
    >> order = {"type": "dress", "size": "xs", "brand": "mango","price": 2000.0, "quantity": 2, "discount": 0}
    >>GetTypeDiscount(order)
    200.0
    
    """
    #Input types assertion:
    assert (isinstance(order, dict)), "order must be a dictionary."

    #Discount value is 10% of one quantity price
    discount = order["price"] * 10 / 100
    return discount


def IsPriceQualified(order: dict)-> bool:
    """
    IsPriceQualified function checks whether the order price is higher than a specific value.

    :param: order: a dictionary represents an order with some attributes
    :return: a boolean value based on the given product price

    - Example:
    >> order = {"type": "dress", "size": "xs", "brand": "mango","price": 2000.0, "quantity": 2, "discount": 0}
    >>IsPriceQualified(order)
    True
    
    """
    #Input types assertion:
    assert (isinstance(order, dict)), "order must be a dictionary."

    return order["price"] >= 1600

def GetPriceDiscount(order: dict)->float:
    """
    GetPriceDiscount function calculates discount for the given order.

    :param: order: a dictionary represents an order with some attributes
    :return: discount value

    - Example:
    >> order = {"type": "dress", "size": "xs", "brand": "mango","price": 2000.0, "quantity": 2, "discount": 0}
    >>GetPriceDiscount(order)
    500.0
    
    """
    #Input types assertion:
    assert (isinstance(order, dict)), "order must be a dictionary."

    #Discount value is 25% of one quantity price
    discount = order["price"] * 25 / 100
    return discount


def IsBrandQualified(order: dict)-> bool:
    """
    IsBrandQualified function checks whether the order belongs to a specific list of brands.

    :param: order: a dictionary represents an order with some attributes
    :return: a boolean value based on the given product brand

    - Example:
    >> order = {"type": "dress", "size": "xs", "brand": "mango","price": 2000.0, "quantity": 2, "discount": 0}
    >>IsBrandQualified(order)
    True
    
    """

    #Input types assertion:
    assert (isinstance(order, dict)), "order must be a dictionary."

    return order["brand"] in ["mango", "lipsy", "zara"]

def GetBrandDiscount(order: dict)->float:
    """
    GetBrandDiscount function calculates discount for the given order.

    :param: order: a dictionary represents an order with some attributes
    :return: discount value

    - Example:
    >> order = {"type": "dress", "size": "xs", "brand": "mango","price": 2000.0, "quantity": 2, "discount": 0}
    >>GetBrandDiscount(order)
    300.0
    
    """
    #Input types assertion:
    assert (isinstance(order, dict)), "order must be a dictionary."

    #Discount value is 15% of one quantity price
    discount = order["price"] * 15 / 100
    return discount


def IsSizeQualified(order: dict)-> bool:
    """
    IsSizeQualified function checks whether the order belongs to a specific list of sizes.

    :param: order: a dictionary represents an order with some attributes
    :return: a boolean value based on the given product size

    - Example:
    >> order = {"type": "dress", "size": "L", "brand": "mango","price": 2000.0, "quantity": 2, "discount": 0}
    >>IsSizeQualified(order)
    False
    
    """
    #Input types assertion:
    assert (isinstance(order, dict)), "order must be a dictionary."

    return order["size"] in ["xs", "2xl"]

def GetSizeDiscount(order: dict)->float:
    """
    GetSizeDiscount function calculates discount for the given order.

    :param: order: a dictionary represents an order with some attributes
    :return: discount value

    - Example:
    >> order = {"type": "dress", "size": "xs", "brand": "mango","price": 2000.0, "quantity": 2, "discount": 0}
    >>GetSizeDiscount(order)
    700.0
    
    """

    #Input types assertion:
    assert (isinstance(order, dict)), "order must be a dictionary."
   
    #Discount value is 35% of one quantity price
    discount = order["price"] * 35 / 100
    return discount


def IsQuantityQualified(order: dict)-> bool:
    """
    IsQuantityQualified function checks whether the product quantity in the given order is greater than a specific value

    :param: order: a dictionary represents an order with some attributes
    :return: a boolean value based on product quantity in the given order

    - Example:
    >> order = {"type": "dress", "size": "xs", "brand": "mango","price": 2000.0, "quantity": 1, "discount": 0}
    >>IsQuantityQualified(order)
    False
    
    """

    #Input types assertion:
    assert (isinstance(order, dict)), "order must be a dictionary."

    return order["quantity"] > 1

def GetQuantityDiscount(order: dict)->float:
    """
    GetTypeDiscount function calculates discount for the given order.

    :param: order: a dictionary represents an order with some attributes
    :return: discount value

    - Example:
    >> order = {"type": "dress", "size": "xs", "brand": "mango","price": 2000.0, "quantity": 2, "discount": 0}
    >>GetTypeDiscount(order)
    360.0
    
    """
    #Input types assertion:
    assert (isinstance(order, dict)), "order must be a dictionary."
    
    #Discount value is 18% of one quantity price
    discount = order["price"] * 18 / 100
    return discount


def get_rules()->List[namedtuple]:

    """
    get_rules function returns a list of discount qualifying conditions and discount rules pairs.

    :return: a list of named tuples, each of which holds a qualifying condition function and the corresponding discount
    calculation function
    - Example:
    >> order = {"type": "dress", "size": "xs", "brand": "mango","price": 2000.0, "quantity": 2, "discount": 0}
    >>get_rules()
    [
        DiscountPair(IsTypeQualified, GetTypeDiscount), 
        DiscountPair(IsPriceQualified, GetPriceDiscount),
        DiscountPair(IsBrandQualified, GetBrandDiscount), 
        DiscountPair(IsSizeQualified, GetSizeDiscount),
        DiscountPair(IsQuantityQualified, GetQuantityDiscount)
    ]

    """
    
    #Creating a namedtuple that has a name "DiscountPair", a first item with name "QualfyingCondition",
    #and a second item with name "DiscountRule":
    DiscountPair = namedtuple("DiscountPair", "QualifyingCondition DiscountRule")

    conditions_rules_pairs = [
                              DiscountPair(IsTypeQualified, GetTypeDiscount), 
                              DiscountPair(IsPriceQualified, GetPriceDiscount),
                              DiscountPair(IsBrandQualified, GetBrandDiscount), 
                              DiscountPair(IsSizeQualified, GetSizeDiscount),
                              DiscountPair(IsQuantityQualified, GetQuantityDiscount)
                              ]
    
    return conditions_rules_pairs
