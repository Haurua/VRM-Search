from django import template
import datetime

register = template.Library()


@register.filter()
def format_date(date: str) -> str:
    """Rearrange the date format to an easier to read format, depending on original format.

    :parameter:
            date (str): Date in string format, either DD-MM-YYYY or MM-YYYY.
    :returns:
            (str): string date in a better looking format.
    """
    if len(date) > 8:
        return datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%d %B, %Y')
    return datetime.datetime.strptime(date, '%Y-%m').strftime('%B %Y')


@register.filter()
def insert_comma(num: int) -> str:
    """Insert commas as 1000 separator.

    :parameter:
            num (int): Integer to be converted and have commas inserted.
    :returns:
            (str): String with appropriate commas.
    """
    return f"{num:,}"
