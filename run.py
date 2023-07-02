import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('japanese_sushi')

order = SHEET.worksheet("sales")
data_one = order.get_all_values()


def get_enter_input():                         # Ask if user want to put in todays sales.
    """
    Ask if user want to put in todays sales.
    """
    print("Welcome to Japanese Sushi terminal!\nDo you want to continue?\n")
    input_firs_question = (input("Enter (y/n): \n")).upper()
    # print(f"\nYou pressed: {input_firs_question}\n")
    if input_firs_question == "Y":
        print("\nJapanese Sushi Terminal Menu:\nWhat do you want to register?\n1. Today's sales\n2. Today's tips")
        spread_all_tips()

    elif input_firs_question == "N":
        print("\nWelcome back next time!\n")

    else:
        print("Invalid input, try again!\n")
        get_enter_input()



def spread_all_tips():
    input_first_numbers = (input("Press number and Enter:\n"))
    if input_first_numbers == "1":
        main_sales()

    elif input_first_numbers == "2":
        main_tip()

    else:
        get_enter_input()


def get_all_sales_data():
    """
    User make input of how much the sold after 1pm.
    Cred. CI - Love sandwiches(Modified by me).
    """
    while True:                                         # Makes a loop if user get the wrong input

        print("\nPlease enter todays lunch data.")      # Text for the user.
        print("In the order: Omakase, Moriawase, Salmon, Vegetarian, Poké Bowl")
        print("Separate the 5 numbers by commas.")
        print("Example: 38,30,25,20,24\n")

        data_str = input("Enter todays sales here: \n")     # The user get a input line to write in.
        print(f"You provided this: {data_str}")           # The user can see the input.

        sales_data = data_str.split(",")                  # Take the input from a string to a list.

        if check_validation_data(sales_data):              # Pass data to the next function.
            print("Data is valid")
            break

    return sales_data


def input_of_tips():

    while True:

        data_str = input("Total ampunt of tip today: \n")
        print(f"You provided this: {data_str}")

        tip_data = data_str

        if check_validation_tip_data(tip_data):
            print("Tip is counted!")
            break

    return tip_data


def check_validation_data(values):
    """
    The input of the sales data has to be correct.
    If it's not correct, run a while loop till the
    correct input is made. Explane what typ of input come
    and put out to the terminal what its needed.
    Cred. CI - Love sandwiches(Modified by me).
    """
    try:
        [int(value.strip()) for value in values]        # Provide the value to be a integer and remove white spaces.
        if len(values) != 5:                            # Provide an error if user don't add 5 values.
            raise ValueError(
                f"Expected 5 values, you provided {len(values)}.\n"
            )
    except ValueError as e:
        print(f"Invalid data: {e}Please try again.\n")
        return False

    return True


def check_validation_tip_data(tips):
    """
    Checks if the input is a valid float number.
    If it's not valid, runs a while loop until the correct input is made.
    """
    while True:
        try:
            tips = float(tips)
            print("Its float")
            break 
        except ValueError:
            print(f"Invalid data: {tips} Please try again.\n")   # Provide an error if user don't add add a float number.
            tips = input("Enter a number: \n")

    return True


def update_sales_worksheet(data):                       # Function to add data to worksheet
    """
    Update  the sales worksheet, adds a new row in the worksheet
    with the list of data the user have provided.
    Cred. CI - Love sandwiches(Modified by me).
    """
    print("Updating the sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Our sales is updated successfully.\n")


def update_sureplus_worksheet(data):                # Function to add surplus data to worksheet
    """
    Update  the surplus worksheet, adds a new row in the worksheet
    with the list of data the calculation have provided.
    Cred. CI - Love sandwiches(Modfied by me).
    """
    print("Updating the surlplus worksheet...\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("Your surplus is updated successfully.\n")


def update_premanuf_worksheet(data):                # Function to add premanuf data to worksheet
    """
    Update  the premanuf worksheet, adds a new row in the worksheet
    with the list of data the calculation have provided.
    Cred. CI - Love sandwiches(Modified by me).
    """
    print("Updating the premanuf worksheet...\n")
    premanuf_worksheet = SHEET.worksheet("premanuf")
    premanuf_worksheet.append_row(data)
    print("Your premanuf is updated successfully.\n")


# def update_tips_worksheet(data):                # Function to add premanuf data to worksheet
#     """
#     Update  the premanuf worksheet, adds a new row in the worksheet
#     with the list of data the calculation have provided.
#     Cred. CI - Love sandwiches(Modified by me).
#     """
#     print("Updating the tips worksheet...\n")
#     premanuf_worksheet = SHEET.worksheet("tips")
#     premanuf_worksheet.append_row(data)
#     print("Your premanuf is updated successfully.\n")


def calculateing_surplus_data(sales_row):
    """
    Definition of sureplus:
    - If positive, it indicate that they had to throw away sushi.
    - If negative, it's indicate that costumer had to wait
    while they made more sushi.

    This function calculate how much that have been wasted or made this day.
    Cred. CI - Love sandwiches(Modified by me).
    """
    print("Calculating the sureplus data...\n")

    premanuf = SHEET.worksheet("premanuf").get_all_values()  # Get the value of premanuf in the worksheet.
    premanuf_row_last = premanuf[-1]                         # Get the last value of the list in premanuf.

    surplus_data = []
    for premanuf, sales in zip(premanuf_row_last, sales_row):   # To handle the both list at the same time
        surplus = int(premanuf) - sales                         # Calculate surplus, premanuf comes first as a str, now its a int.
        surplus_data.append(surplus)

    return surplus_data


def split_tips_between(tips):
    """
    Split the tips between 6 coworkers that works at the resturant.
    """
    print("Spliting tips between workers...\n")
    split_tips = []
    for t in range(6):
        split_tip = tips / 6.0
        split_tips.append(split_tip)
        tips -= split_tip
        print("Split tips")
        print(split_tips)
    return split_tips




def get_last_3_sales():
    """
    This collect the last 3 columns of data from the sales worksheet
    for eash sushi-type. Cred. CI - Love sandwiches(Modified by me).
    """
    sales = SHEET.worksheet("sales")                # Get data from the worksheet
    columns = []                                    # Empty variable
    for ind in range(1, 6):                          # Loop throug numbers 1-5
        column = sales.col_values(ind)
        columns.append(column[-3:])                 # -3, To get the latest input from the workcheet

    return columns                                  # Sett the value to the function


def calculate_premanuf_data(data):                  # Calculat the premanufactury value
    """
    Finds the average premanufacturing of 3 and
    the value for each item.
    Then adding aditional 5%. Cred. CI - Love sandwiches(Modified by me).
    """
    print("Calculating premanuf data...\n")

    new_premauf_data = []
    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        premanuf_num = round(average * 1.05)
        new_premauf_data.append(premanuf_num)

    return new_premauf_data


def get_premanuf_values(data):                  # Get visual for user what to make next day
    """
    Print to user the calculated premanuf numbers for each sushi. Cred. CI - Love sandwiches(Modified by me).
    """
    headings = SHEET.worksheet('premanuf').row_values(1)    # Get headings for the sushi type
    print("Make the following sushi for the next day:\n")

    new_data = {}
    for heading, premanuf_num in zip(headings, data):
        new_data[heading] = premanuf_num

    return new_data


def get_data_deleted():                         # Ask if user whant to delet the input with a yes or a no.
    """
    Ask if its true, else will delete the data that was just inputed.
    """
    result_del = (input("\nDo you want to delete your input? Enter (y/n): \n")).upper()
    if result_del == "Y":
        print(f"\nYou pressed: {result_del}\n")
        check_validation_delete()
        print("\nData has been deleted\n")
        print("\nYou will now go back and enter the correct sales for today...")
        main_sales()

    elif result_del == "N":
        print("\nWelcome back next salesday!!!\n")

    else:
        print("Did not press (Y/N), try again.")
        get_data_deleted()


def check_validation_delete():                      # When function calls it delete the last row in the selected sheets.
    surplus_worksheet = SHEET.worksheet("surplus")
    rows_sur = surplus_worksheet.row_count
    surplus_worksheet.delete_rows(rows_sur)
    premanuf_worksheet = SHEET.worksheet("premanuf")
    rows_pre = premanuf_worksheet.row_count
    premanuf_worksheet.delete_rows(rows_pre)
    sales_worksheet = SHEET.worksheet("sales")
    rows_sal = sales_worksheet.row_count
    sales_worksheet.delete_rows(rows_sal)


def main_sales():
    data = get_all_sales_data()
    sales_data = [int(num) for num in data]                  # Make the list values to numbers instead of strings value"
    update_sales_worksheet(sales_data)                       # Pass data to the function upsate_sales_worksheet.
    new_surplus_data = calculateing_surplus_data(sales_data)  # Sett the values to the variable
    update_sureplus_worksheet(new_surplus_data)              # Pass datat to the function
    sales_columns = get_last_3_sales()
    premanuf_data = calculate_premanuf_data(sales_columns)      # Calculate the averege of the latest 3 sales.
    update_premanuf_worksheet(premanuf_data)
    premanuf_values = get_premanuf_values(premanuf_data)    # Update premanuf data to worksheet
    print(premanuf_values)
    get_data_deleted()                                         # Delet the latest row of data in worksheet.


def main_tip():
    input_of_tips()
    check_validation_tip_data(tip_data)
    tips = spread_all_tips()
    divided_tips = split_tips_between(tips)
    # print(divided_tips)
    # update_tips_worksheet(divided_tips)


def main_terminal():
    get_enter_input()


def main():
    """
    Run all program functions.
    """
    main_terminal()


main()
