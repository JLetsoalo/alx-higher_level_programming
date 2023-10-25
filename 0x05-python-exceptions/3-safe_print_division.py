#!/usr/bin/python3
#safely printing division results

def safe_print_division(a, b):
    try:
        div = a / b
    """skips division by zero"""
    except (ZeroDivisionError, TypeError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
