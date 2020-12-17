#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        new_dic = {}
        new_dic = sorted(a_dictionary.values())
        return new_dic[-1]
