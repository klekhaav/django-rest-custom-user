from rest_framework import permissions
from models import UserExtension
import datetime


class UserAccessPermission(permissions.BasePermission):
    message = 'Sorry you need to be 13 year old.'

    def has_permission(self, request, view):
        age_year_ctrl = int(datetime.date.today().year) - 13
        age_month_ctrl = datetime.date.today().month
        age_day_ctrl = datetime.date.today().day
        older = UserExtension.objects.filter(
            birthday__year__lte=age_year_ctrl,
            birthday__month__gte=age_month_ctrl,
            birthday__day__gte=age_day_ctrl
        )
        return older
