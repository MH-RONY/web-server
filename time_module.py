import datetime

def string_time():

    time_formate = {
        "weekday": "%a",
        "day": "%d",
        "month": "%b",
        "year": "%Y",
        "hour": "%I",
        "minute": "%M",
        "second": "%S",
        "ap": "%p"
    }

    time_obj = {
        "timezone": "GMT",
        "utc": "+06"
    }

    time_present = datetime.datetime.now()

    for key, value in time_formate.items():
        time_obj[key] = time_present.strftime(value)

    time_str = "{}, {} {} {} {}:{}:{} {} {}({})".format(time_obj["weekday"], time_obj["day"], time_obj["month"], time_obj["year"], time_obj["hour"], time_obj["minute"], time_obj["second"], time_obj["ap"], time_obj["timezone"], time_obj["utc"])

    return time_str


if __name__ == "__main__":
    print(f"Time: {string_time()}")
