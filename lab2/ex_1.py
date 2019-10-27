#!/usr/bin/env python3
# coding=utf-8
from librip.gens import field
from librip.gens import gen_random

goods = [
    {'title': "Ковер", 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

for good in field(goods, 'title'):
    print good

random = gen_random(1, 5, 4)
print random

