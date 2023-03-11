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
    print("Do you want to enter toadays sushi sales?\n")
    result_del = (input("Enter (y/n): \n")).upper()
    if result_del == "Y":
        print(f"\nYou pressed: {result_del}\n")
        print("\nYou will enter now!\n")
        main()
        
    elif result_del == "N":
        print("\nWelcome back next time!\n")
        
    else:
        main()


def get_all_sales_data():
    """
    User make input of how much the sold after 1pm.
    """
    while True:                                         # Makes a loop if user get the wrong input

        print("\nWelcome, please enter todays lunch data.")      # Text for the user.
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


def check_validation_data(values):
    """
    The input of the sales data has to be correct.
    If it's not correct, run a while loop till the 
    correct input is made. Explane what typ of input come
    and put out to the terminal what its needed.
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


def update_sales_worksheet(data):                       # Function to add data to worksheet
    """
    Update  the sales worksheet, adds a new row in the worksheet 
    with the list of data the user have provided.
    """
    print("Updating the sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Our sales is updated successfully.\n")


def update_sureplus_worksheet(data):                # Function to add surplus data to worksheet
    """
    Update  the surplus worksheet, adds a new row in the worksheet 
    with the list of data the calculation have provided.
    """
    print("Updating the surlplus worksheet...\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("Your surplus is updated successfully.\n")


def update_premanuf_worksheet(data):                # Function to add premanuf data to worksheet
    """
    Update  the premanuf worksheet, adds a new row in the worksheet 
    with the list of data the calculation have provided.
    """
    print("Updating the premanuf worksheet...\n")
    premanuf_worksheet = SHEET.worksheet("premanuf")
    premanuf_worksheet.append_row(data)
    print("Your premanuf is updated successfully.\n")


def calculateing_surplus_data(sales_row): 
    """
    Definition of sureplus:
    - If positive, it indicate that they had to throw away sushi.
    - If negative, it's indicate that costumer had to wait 
    while they made more sushi.

    This function calculate how much that have been wasted or made this day.
    """
    print("Calculating the sureplus data...\n")
    premanuf = SHEET.worksheet("premanuf").get_all_values() # Get the value of premanuf in the worksheet.
    premanuf_row_last = premanuf[-1]                        # Get the last value of the list in premanuf.
    
    surplus_data = []
    for premanuf, sales in zip(premanuf_row_last, sales_row):   # To handle the both list at the same time
        surplus = int(premanuf) - sales                         # Calculate surplus, premanuf comes first as a str, now its a int.
        surplus_data.append(surplus)

    return surplus_data

def get_last_3_sales():
    """
    This collect the last 3 columns of data from the sales worksheet
    for eash sushi-type.
    """
    sales = SHEET.worksheet("sales")                # Get data from the worksheet
    columns = []                                    # Empty variable
    for ind in range(1,6):                          # Loop throug numbers 1-5
        column = sales.col_values(ind)              
        columns.append(column[-3:])                 # -3, To get the latest input from the workcheet
    
    return columns                                  # Sett the value to the function
        
def calculate_premanuf_data(data):                  # Calculat the premanufactury value
    """
    Finds the average premanufacturing of 3 and 
    the value for each item. 
    Then adding aditional 5%
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
    Print to user the calculated premanuf numbers for each sushi.
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
    print("Do you want to delete your input?")
    result_del = (input("Enter (y/n): \n")).upper()
    if result_del == "Y":
        print(f"\nYou pressed: {result_del}\n")
        check_validation_delete()
        print("\nData has been deleted\n")
        print("\nYou will now go back and enter the correct sales for today...")
        main()

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


def main():
    data = get_all_sales_data()
    sales_data = [int(num) for num in data]                 # Make the list values to numbers instead of strings value"
    update_sales_worksheet(sales_data)                      # Pass data to the function upsate_sales_worksheet.
    new_surplus_data = calculateing_surplus_data(sales_data) # Sett the values to the variable
    update_sureplus_worksheet(new_surplus_data)             # Pass datat to the function
    sales_columns = get_last_3_sales()
    premanuf_data = calculate_premanuf_data(sales_columns)
    update_premanuf_worksheet(premanuf_data)
    premanuf_values = get_premanuf_values(premanuf_data)
    print(premanuf_values)
    get_data_deleted()
    
get_enter_input()