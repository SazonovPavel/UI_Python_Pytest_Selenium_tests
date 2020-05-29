# -*- coding: utf-8 -*-
import random


def get_new_rt_title():
    list_name = ["Good ", "Gorgeous ", "Perfect "]
    list_number = ["- 1", "- 2", "- 3"]
    rt = "Report Template "

    a = random.choice(list_name)
    b = random.choice(list_number)
    result = a + rt + b
    return result


def get_updated_rt_title(title):
    result = "UPDATED " + title
    return result
