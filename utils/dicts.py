def get_val(collection, key, default="git"):
    if collection:
        return collection.get(key)
    else:
        return default
