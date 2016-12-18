from flask import jsonify
from functools import wraps


def pack(func):
    """
    Translate and pack the output of a function in a default JSON output format

    :param func: function
    :type func: Function
    """

    @wraps(func)
    def validate(*args, **kwargs):
        result = func(*args, **kwargs)
        return jsonify({'status': result[1], 'result': result[0]})

    return validate
