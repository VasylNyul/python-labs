import service.data_processing as dp


class User:

    def __init__(self, data):
        """
        Initialize UserData object with the given data.
        Parameters:
        - data (list): A list containing values for each attribute in the specified order.
        """
        self.index = data[0]
        self.user_id = data[1]
        self.first_name = data[2]
        self.last_name = data[3]
        self.sex = data[4]
        self.email = data[5]
        self.phone = data[6]
        self.date_of_birth = dp.DateOperations.parse_dateformat(data[7], "%Y-%m-%d").date()
        self.job_title = data[8]

    def __str__(self):
        return f"{self.index} {self.user_id} {self.first_name} {self.last_name} {self.sex} {self.email} {self.phone} {self.date_of_birth} {self.job_title}"