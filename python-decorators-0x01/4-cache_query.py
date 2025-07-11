import functools

query_cached = {}

def cache_query(func):
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


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")