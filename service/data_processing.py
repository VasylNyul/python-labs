from datetime import datetime

from dateutil.relativedelta import relativedelta


class DateOperations:
    @staticmethod
    def parse_dateformat(date: str, date_format: str) -> datetime:
        return datetime.strptime(date, date_format)

    @staticmethod
    def calculate_year_difference(dt: datetime):
        return relativedelta(datetime.now(), dt).years