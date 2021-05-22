# -*- coding: utf-8 -*-
from helpers import check_float
from helpers import create_response
from helpers import calculate_with_operator

def calculate(left, right, operator):
    """Calculate answer from the given input"""

    # Calculate
    status, message = calculate_with_operator(left, right, operator)

    # Create response
    response, status_code = create_response(
        data = message,
        checks = [status],
        message_ok = 'Calculation completed!',
        message_error = message
    )

    return response, status_code
