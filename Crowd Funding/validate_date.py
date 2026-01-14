from datetime import datetime

def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True 
    except ValueError:
        return False