"""

 - This is a program created by Noah Sizemore

"""

"""
    Format for the Google Doc:

    Table should be formated as follows: 

    ---------------
    | x unicode y |
    | x unicode y |
    | x unicode y |
    | x unicode y |
    | x unicode y |
    | x unicode y |
    | x unicode y |
    | x unicode y |
    ---------------


"""

# import BeautifulSoup and requests to access data from the Google Doc
import requests
from bs4 import BeautifulSoup


# This method takes the url, makes it accessible, then returns the output of the decoded message
def decode_google_message(url):

    # getting the url from the web
    response = requests.get(url)
    response.raise_for_status() # Raise an exception for bad status codes

    # parsing the data to html
    soup_response = BeautifulSoup(response.text, "html.parser")

    # finding the table only in the Google Doc table
    doc_table = soup_response.find("table")

    # initial creation of the list used to return the result
    parsed_data = []

    # if the doc contains a table...
    if doc_table:
        # "tr" means it will iterate through every row
        table_rows = doc_table.find_all("tr")

        # loops through every row EXCEPT the first which contains the titles, find all the columns "td"
        for row in table_rows[1:]:
            table_columns = row.find_all("td")

            # ensuring that the rows have enough columns and cleaning the data
            if len(table_columns) >= 3:
                x_value = table_columns[0].get_text().strip()
                final_uni = table_columns[1].get_text().strip()
                y_value = table_columns[2].get_text().strip()

                # checking to see if the digits are digits
                if x_value.isdigit() and y_value.isdigit():
                    final_x = int(x_value)
                    final_y = int(y_value)

                    parsed_data.append([final_x, final_uni, final_y])


    # setting up the grid for the final print statement using the data from parse_data where 0 is "x" and 2 is "y"
    max_x_grid = max([item[0] for item in parsed_data], default = 0)
    max_y_grid = max([item[2] for item in parsed_data], default=0)

    # creating the grid needing the max x and y values to be + 1 their current dimension
    grid = [[" " for _ in range(max_x_grid + 1)] for _ in range(max_y_grid + 1)]

    # placing each value in their respective place for the grid
    for item in parsed_data:
        x_coordinate = item[0]
        uni_char = item[1]
        y_coordinate = item[2]

        # the format for a grid is grid[y][x]
        grid[y_coordinate][x_coordinate] = uni_char

    # print the final result by looping through every place that a character needs to be
    for place in grid:
        print("".join(place))



# main method
def main():
    user_url = str(input("What is the URL of the document: "))
    decoded_message = decode_google_message(user_url)
    print(f"\n\n{decoded_message}")

# run main
if __name__ == "__main__":
    main()

























