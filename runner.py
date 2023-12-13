from service.user_service import UserService, UserServiceImpl


def main():
    data_file = "./files/users.csv"
    service = UserServiceImpl(data_file)

    while (True):
        print(f"1. Display difference in years histogram\n"
              f"2. Display sex pie chart\n"
              f"3. Display job bar chart\n"
              f"4. Display complicated diagram\n"
              f"0. Exit\n")

        match (input("Enter your choice: ")):
            case "1":
                has_to_be_downloaded = True if input(
                    "Do you want to download the histogram? Enter 'y' or anything else not to download") == "y" else False
                service.create_difference_in_years_histogram(has_to_be_downloaded)
            case "2":
                has_to_be_downloaded = True if input(
                    "Do you want to download the pie chart? Enter 'y' or anything else not to download") == "y" else False
                service.create_sex_pie_chart(has_to_be_downloaded)
            case "3":
                has_to_be_downloaded = True if input(
                    "Do you want to download the bar chart? Enter 'y' or anything else not to download") == "y" else False
                service.create_job_bar_chart(has_to_be_downloaded)
            case "4":
                has_to_be_downloaded = True if input(
                    "Do you want to download the complicated chart? Enter 'y' or anything else not to download") == "y" else False
                service.create_complicated_diagram(has_to_be_downloaded)
            case "0":
                exit(0)
            case _:
                print("Invalid choice. Enter again!")


if __name__ == '__main__':
    main()