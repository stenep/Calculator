# -*- coding: utf-8 -*-
import json

def check_float(num):
    """
    Return True if the given number can be evaluated as float else return False
    """
    try:
        float(num)
        return True
    except ValueError:
        return False

def create_response(data, checks, message_ok, message_error):
    """
    Creates a HTML JSON response.

    Args:
        data (str):
            data to return
        checks (list):
            a list of checks that must evaluate to True
        message_ok (str):
            message to return if all checks are OK
        message_error (str):
            message to return if all checks are not OK

    Return:
        JSON formatted response and status code
    """
    if all(checks):
        status_code = 200
        message = message_ok
    else:
        status_code = 500
        message = message_error
        data = None

    response = {'data': data,
                'message': message}

    return json.dumps(response), status_code

def calculate_with_operator(left, right, operator):
    """
    Calculates an answer for a math expression on the form
    'left operator right'.

    Args:
        left/right (str):
            a string containing a valid number
        operator (str):
            a string describing the operator to use:
                add (addition)
                sub (subtraction)
                mult (multiplication)
                div (division)

    Return:
        Answer to the input given
    """

    # Check input numbers
    if not all([check_float(num) for num in [left, right]]):
        # Error
        error = 'You must provide valid numbers!'
        return False, error

    # Convert to float
    left, right = [float(num) for num in [left, right]]

    # Perform calculation
    if operator == 'mult':
        ans = left * right
    elif operator == 'div':
        try:
            ans = left / right
        except ZeroDivisionError as e:
            error = 'Cannot divide by zero!'
            return False, error
    elif operator == 'add':
        ans = left + right
    elif operator == 'sub':
        ans = left - right
    else:
        error = 'Unknown operator!'
        return False, error

    # Return answer
    return True, ans
