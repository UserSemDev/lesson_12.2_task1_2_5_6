def get_val(collection, key, default="git"):
    """Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default.
    :param collection: исходный словарь
    :param key: ключ словаря
    :param default: дефолтное значение"""
    if collection:
        return collection.get(key)
    else:
        return default
