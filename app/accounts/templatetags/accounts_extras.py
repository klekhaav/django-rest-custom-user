from django import template
import datetime

register = template.Library()


@register.filter(name='get_age')
def get_age(value):
    age_year_ctrl = int(datetime.date.today().year) - 13
    age_month_ctrl = datetime.date.today().month
    age_day_ctrl = datetime.date.today().day
    if value.year <= age_year_ctrl:
        if value.month >= age_month_ctrl:
            if value.day >= age_day_ctrl:
                return "allowed"
    else:
        return "blocked"


@register.filter(name='bizz_fuzz')
def bizz_fuzz(value):
    st = ""
    if value % 3 == 0:
        st += "Bizz"
    if value % 5 == 0:
        st += "Fuzz"
    if value % 3 != 0 and value % 5 != 0:
        st = value
    return "%s" % st