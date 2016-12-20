from flask import jsonify
from functools import wraps
from thw.helpers.api import HttpException


def pack(func):
    """
    Translate and pack the output of a function in a default JSON output format

    :param func: function
    :type func: Function
    """

    @wraps(func)
    def validate(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return jsonify({'status': result[1], 'result': result[0], 'valid': True})
        except (HttpException, RuntimeError) as ex:
            return jsonify({'status': 401, 'result': ex.message})

    return validate

