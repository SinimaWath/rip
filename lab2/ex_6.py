#!/usr/bin/env python3
# coding=utf-8
import json
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = 'data_light.json'
with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(unique(list(field(arg, 'job-name')), ignore_case=True))

@print_result
def f2(arg):
    return list(filter(lambda x: 'программист' in x, arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    sals = list(gen_random(100000, 200000, len(arg)))
    return list(map(lambda x: x[1] + ' с зарплатой ' + str(sals[x[0]]), enumerate(arg)))


with timer():
    f4(f3(f2(f1(data))))
