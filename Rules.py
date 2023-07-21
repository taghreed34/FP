from collections import namedtuple
from typing import *



def IsTypeQualified(order: dict)-> bool:
    return order["type"] in ["dress", "skirt"]

def GetTypeDiscount(order: dict)->float:
    discount = order["price"] * 10 / 100
    return discount


def IsPriceQualified(order: dict)-> bool:
    return order["price"] >= 1600

def GetPriceDiscount(order: dict)->float:
    discount = order["price"] * 25 / 100
    return discount


def IsBrandQualified(order: dict)-> bool:
    return order["brand"] in ["mango", "lipsy", "zara"]

def GetBrandDiscount(order: dict)->float:
    discount = order["price"] * 15 / 100
    return discount


def IsSizeQualified(order: dict)-> bool:
    return order["size"] in ["xs", "2xl"]

def GetSizeDiscount(order: dict)->float:
    discount = order["price"] * 35 / 100
    return discount


def IsQuantityQualified(order: dict)-> bool:
    return order["quantity"] > 1

def GetQuantityDiscount(order: dict)->float:
    discount = order["price"] * 18 / 100
    return discount


def get_rules()->List[namedtuple]:

    DiscountPair = namedtuple("Discount Pair", "QualifyingCondition DiscountRule")

    conditions_rules_pairs = [
                              DiscountPair(IsTypeQualified, GetTypeDiscount), 
                              DiscountPair(IsPriceQualified, GetPriceDiscount),
                              DiscountPair(IsBrandQualified, GetBrandDiscount), 
                              DiscountPair(IsSizeQualified, GetSizeDiscount)
                              ]
    
    return conditions_rules_pairs
