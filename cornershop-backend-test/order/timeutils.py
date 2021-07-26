import datetime


def is_time_limit():
    """
    we need to validate the limit hour to make a order
    declared limit_time_string in environments variables
    :return:
    """
    limit_time_string = "11:00:00"

    limit_time_datetime = datetime.datetime.strptime(limit_time_string, "%H:%M:%S")

    current_datetime = datetime.datetime.today()
    today_time_limit = current_datetime.replace(hour=limit_time_datetime.time().hour,
                                                minute=limit_time_datetime.time().minute,
                                                second=limit_time_datetime.time().second,
                                                microsecond=0)

    return current_datetime < today_time_limit
