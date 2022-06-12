import datetime
from dateutil.relativedelta import relativedelta

from django import template


register = template.Library()

# カスタムフィルタを登録
@register.filter
def month_delta(input_date):
    start_date = input_date
    current_date = datetime.date.today()
    result = (
        relativedelta(current_date, start_date).years * 12
        + relativedelta(current_date, start_date).months
    )
    return result
