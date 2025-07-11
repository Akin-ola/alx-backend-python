import functools

query_cached = {}

def query_cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Use function name and args as a cache key (can be improved further)
        key = (func.__name__, args, frozenset(kwargs.items()))

        if key in query_cached:
            print("Fetching from cache...")
            return query_cached[key]

        # If not in cache, run the function
        result = func(*args, **kwargs)
        query_cached[key] = result
        return result
    return wrapper