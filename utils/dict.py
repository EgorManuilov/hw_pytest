def get_val(collection, key, default='git'):
    """ Функция возвращает значение из словаря по переданному ключу,
        если ключ существует.
        В ином случае возвращается значение default.
    """

    if len(collection) == 0:
        return default
    else:
        for k in collection:
            if k == key:
                return collection[key]
            return default