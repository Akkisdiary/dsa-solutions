import datetime

DATE_FORMAT = "%d/%m/%Y"


def calculate_subscription(expiry_date, months_to_buy, monthly_cost):
    start_date = datetime.datetime.strptime(expiry_date, DATE_FORMAT)

    end_day = start_date.day
    end_month = start_date.month + (months_to_buy % 12) - 1
    end_year = start_date.year + (months_to_buy // 12)
    end_date = datetime.datetime(day=start_date.day, month=end_month, year=end_year)

    billing_month = (end_date.month % 12) + 1
    billing_year = end_date.year + ((end_date.month + 1) // 12)
    billing_day = 15 if months_to_buy == 1 else 1
    if billing_month > end_month:
        billing_day = 1
    billing_date = datetime.datetime(
        day=billing_day, month=billing_month, year=billing_year
    )

    daily_cost = monthly_cost / 30

    full_months = months_to_buy - 1
    days_over_full_months = (billing_date - end_date).days

    subscription_date = billing_date.strftime(DATE_FORMAT)
    subscription_cost = (full_months * monthly_cost) + (
        days_over_full_months * daily_cost
    )

    return subscription_date, subscription_cost


print(calculate_subscription("1/01/2022", 1, 1000))
