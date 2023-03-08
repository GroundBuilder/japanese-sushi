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

def get_all_sales_data():
    """
    User make input of how much the sold after 1pm.
    """
    while True:                                         # Makes a loop if user get the wrong input

        print("\nWelcome, please enter todays lunch data.")      # Text for the user.
        print("In the order: Omakase, Moriawase, Salmon, Vegetarian, Poké Bowl") 
        print("Separate the 5 numbers by commas.")
        print("Example: 38,30,25,20,24\n")

        data_str = input("Enter todays sales here: ")     # The user get a input line to write in.
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


data = get_all_sales_data()
sales_data = [int(num) for num in data]
print(sales_data)