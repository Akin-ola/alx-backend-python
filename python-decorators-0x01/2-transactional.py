import mysql.connector


def transactional(func):
    def wrapper(*args, **kwargs):
        connection = kwargs.get('connection')
        cursor = connection.cursor()

        try:
            result= func(cursor, args, kwargs)
            connection.commit()
            return result
        
        except mysql.connector.Error as e:
            connection.rollback()
            print(f"[ERROR] Transaction failed: {e}")
            return None
        finally:
            cursor.close()
    return wrapper
