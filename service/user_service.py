
import abc

from entity.user import User
from utility.FileProcessor import CsvProcessor as csv_processor
import service.data_processing as dp
from matplotlib import pyplot as plt
from collections import Counter


class UserService(abc.ABC):

    def __init__(self):
        self._users = []


class UserServiceImpl (UserService):
    def __init__(self, file_path: str):
        super().__init__()
        users_dataframe = csv_processor.read(file_path)
        for data in users_dataframe.values:
            self._users.append(User(data))

    def get_difference_in_years(self):
        return [dp.DateOperations.calculate_year_difference(user.date_of_birth) for user in self._users]

    def get_sex(self):
        return [user.sex for user in self._users]

    def get_job_title(self):
        return [user.job_title for user in self._users]

    def create_difference_in_years_histogram(self, has_to_be_downloaded=False):
        difference_in_years = self.get_difference_in_years()
        plt.hist(difference_in_years, bins=range(min(difference_in_years), max(difference_in_years)), edgecolor='black')
        if has_to_be_downloaded:
            plt.savefig('./files/difference-in-years-histogram.png')

        plt.title('Histogram')
        plt.xlabel('Age')
        plt.ylabel('Frequency')

        plt.show()

    def create_sex_pie_chart(self, has_to_be_downloaded=False):
        sex = self.get_sex()
        sex_counter = Counter(sex)

        plt.pie([sex_counter[key] for key in sex_counter], labels=[key for key in sex_counter], startangle=90,
                colors=['blue', 'pink'])
        if has_to_be_downloaded:
            plt.savefig('./files/sex-pie-chart.png')

        plt.title('Pie Chart')
        plt.show()

    def create_job_bar_chart(self, has_to_be_downloaded=False):
        job_title = self.get_job_title()
        job_title_counter = Counter(job_title)

        plt.figure(figsize=(11, 16))
        plt.bar([key for key in job_title_counter], [job_title_counter[key] for key in job_title_counter],
                color='green')

        if has_to_be_downloaded:
            plt.savefig('./files/job-bar-chart.png')
        plt.title('Bar Chart')
        plt.xlabel('Job')
        plt.ylabel('Frequency')
        plt.xticks(fontsize=6)  # You can adjust the font size here
        plt.yticks(fontsize=10)
        plt.xticks(rotation=-90)

        plt.show()

    def create_complicated_diagram(self, has_to_be_downloaded=False):
        job_title = self.get_job_title()
        job_title_counter = Counter(job_title)
        difference_in_years = self.get_difference_in_years()

        # Create a figure with two subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 16))

        # First subplot (bar chart)
        ax1.bar([key for key in job_title_counter], [job_title_counter[key] for key in job_title_counter],
                color='green')
        ax1.set_title('Job Frequency')
        ax1.set_xlabel('Job')
        ax1.set_ylabel('Frequency')
        ax1.tick_params(axis='x', labelrotation=-90)
        ax1.tick_params(axis='x', labelsize=6)
        ax1.tick_params(axis='y', labelsize=10)

        # Second subplot (histogram)
        ax2.hist(difference_in_years, bins=range(min(difference_in_years), max(difference_in_years)), edgecolor='black')
        ax2.set_title('Difference in Years Histogram')
        ax2.set_xlabel('Age')
        ax2.set_ylabel('Frequency')

        # Adjust layout to prevent overlapping
        plt.tight_layout()

        # Save figures if needed
        if has_to_be_downloaded:
            plt.savefig('./files/combined_chart.png')

        # Display the plot
        plt.show()