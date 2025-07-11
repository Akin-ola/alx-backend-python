import time
import functools

def retry_on_failure(retries=3, delay=2, exceptions=(Exception, )):
    def retry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts=0
            while attempts < retries:
                try:
                    return func(args, kwargs)
                except exceptions as e:
                    attempts +=1
                    print(f"[WARNING] {e} — Retrying {attempts}/{retries}...")
                    time.sleep(delay)
                print("[ERROR] Operation failed after retries.")
            return None
        return wrapper
    return retry
    