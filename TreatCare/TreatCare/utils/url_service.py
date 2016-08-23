from urllib.parse import urlparse, urlunparse, urlencode, parse_qs

def remove_param(url, param):
    """ Remove param from query of URL
        Args:
            url: URL as string
            param: param name to remove from URL
        Retrun:
            A new URL without query param
    """
    url_obj= urlparse(url)
    query = parse_qs(url_obj.query)
    query.pop(param, None)
    url_obj= url_obj._replace(query=urlencode(query, True))
    return urlunparse(url_obj)

def remove_params(url, params_list):
    """ Remove a list of params from query of URL
        Args:
            url: URL as string
            params_list: list with params names to remove from URL
        Retrun:
            A new URL without query params
    """

    for param in params_list:
        url = remove_param(url, param)
    return url

def append_params(url, params_dict):
    """ Append params to a query of URL
        Args:
            url: URL as string
            params_dict: dictionary with the given params to append to the URL
        Retrun:
            A new URL with appended query params
    """
    url_obj = urlparse(url)
    query = parse_qs(url_obj.query)
    query.update(params_dict)
    url_obj= url_obj._replace(query=urlencode(query, True))
    return urlunparse(url_obj)
