#!/usr/bin/python3


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    best_student = list(a_dictionary.keys())[0]
    best = a_dictionary[best_student]
    for k, v in a_dictionary.items():
        if v > best:
            best = v
            best_student = k
    return best_student
