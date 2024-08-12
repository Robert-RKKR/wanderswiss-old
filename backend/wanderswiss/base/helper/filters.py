def dict_to_filter_params(d, prefix=''):
    """
    Translate a dictionary of attributes to a nested set of parameters
    suitable for QuerySet filtering.
    
    Args:
        d (dict): The dictionary of attributes.
        prefix (str): The prefix to prepend to each parameter key (default: '').
        
    Returns:
        dict: The nested set of parameters suitable for QuerySet filtering.
    """

    params = {}
    for key, val in d.items():
        k = prefix + key
        if isinstance(val, dict):
            params.update(dict_to_filter_params(val, k + '__'))
        else:
            params[k] = val
    return params
