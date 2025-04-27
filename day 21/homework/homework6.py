from datetime import datetime

def format_date(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d').strftime('%d/%m/%Y')
