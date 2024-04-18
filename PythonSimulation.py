# TODO:
    # Other: Could allow the user to copy and paste data or use TXT files instead of using only CSV format.

######################################################################################################
# Section 0.0: IMPORTS            
######################################################################################################

# Menu Imports
import webbrowser
import os

# Simulation Imports
import mysql.connector
import csv
import random
import shutil

######################################################################################################
# Section 1.0: MAIN MENU
# - User can select which menu item to follow.
# - Calls a function within the Menu object based on the choice.
# - Validates user inputs when received and loops until valid.
######################################################################################################

def main():
    menu = Menu()
    while True:
        os.system('cls') # Clear screen
        print("#################### MENU ####################")
        print("|            1. Run Simulation               |")
        print("|            2. Visit Website                |")
        print("|            3. View Github                  |")
        print("|            4. Calculate Year Range         |")
        print("|            5. Quit Application             |")
        print("##############################################")
        choice = input("Please select where you would like to navigate to: ")
        match choice:
            
            # 1. Run Simulation
            case "1":
                menu.choiceOne()
                input("Press Enter to continue...")

            # 2. Visit Website (Will be implemented only after completion)
            case "2":
                menu.choiceTwo()
                input("Press Enter to continue...")

            # 3. Visit Github (Will be implemented after completion)
            case "3":
                menu.choiceThree()
                input("Press Enter to continue...")
            
            # 4. Calculate Year Range
            case "4":
                menu.choiceFour()
                input("Press Enter to continue...")

            # 4. Quit Program
            case "5":
                menu.choiceFive()
            
            # Invalid Selection
            case _:
                input("That was not a valid selection. Press press [Enter] to try again...")
        
        os.system('cls') # Clear screen

######################################################################################################
# Section 2.1: MENU FUNCTIONS
# - Called from Section 1.0.
# - Consists of four functions:
#   = One: Run simulation.
#   = Two: Go to supplemental website.
#   = Three: Go to project Github.
#   = Four: Quit program.
######################################################################################################

# Menu choices object with each function defining a separate action.
# NOTE: Consider condensing this into the main selection.
class Menu:
    def __init__(self):
        pass
    
    # Gender simulation function.
    def choiceOne(self):
        os.system('cls') # Clear screen
        print("|---------------------------------------- Run Simulation ----------------------------------------|")

        # Establish connection to database.
        try:
            mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="password",
                passwd="password",
                port=3306
            )
        except Exception as e:
            print("An error occurred:", e)

        # Call gender simulation object.
        gendersimulation = GenderSimulation(mydb)

        ######################################################################################################
        # Section 2.2: SELECT SINGLE OR RANGE YEAR
        # - Prompts the user to enter if they want to run for one year or multiple.
        # - Calls one of two functions from the GenderSimulation object:
        #   = Single: Calls singleYear function. (Ex. 2002)
        #   = Range: Calls multipleYear function. (Ex. 2002 to 2005)
        # + NOTE: As a more in-depth explanation of why there are two options, both options are used for
        #           different needs. If we wanted to use a dataset that surveys only people born in 1995, then
        #           it would be faster and more accurate to use single, as it would not need to compare it to
        #           multiple years and would carry the exact ranges from that year.
        #         However, if we wanted to run a dataset from 2024 that surveys 21 to 25 year olds, then we
        #           would want to take (2024 - 25) and (2024 - 21) for a range of 1999 to 2003, as this would
        #           allow us to account for any shifts in gender trends and create a sort of 'average' between
        #           all of the years represented in the data.
        ######################################################################################################

        # Prompt the user to select if they want to run a single year or multiple years and call the corresponding function.
        while True:
            print("Would you like to filter your data for a single year (Ex. Only people born in 1997) or would you like to select a range of years (Ex. People born from 1997 to 2002)?")
            selection = input("Please type either 'single' or 'range': ").lower() # Will convert any uppercases in case the user capitalizes any letters.
            if selection == "single":
                gendersimulation.singleYear()
                break
            elif selection == "range":
                gendersimulation.multipleYear()
                break
            else:
                print("Invalid input. Please enter either 'single' or 'range'.")

    # Website function. (May be cut for final development.)
    def choiceTwo(self):
        webbrowser.open("https://www.w3schools.com/python/python_iterators.asp")
        print("This selection will take the user to the website portion of the project, if finished.")
    
    # Github function.
    def choiceThree(self):
        webbrowser.open("https://python-forum.io/")
        print("This selection will take the user to the project github.")

    # Github function.
    def choiceFour(self):

        print("This section will help you calculate your starting and ending years for a ranged simulation. Please input all ages as the ages presented in the year your data was taken.")
        
        # Prompt the user to enter an age between 2 and 122. Loop if invalid.
        while True:
            try:
                minimum = int(input("Enter the minimum age of your data sample: "))
                if ((minimum < 0) or (minimum > 122)):
                    print("Our data sample currently only covers ages within the ranges of 0 to 122. Please enter a year within that range.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an age between 0 and 122.")

        # Prompt the user to enter an age between 0 and 122. Loop if invalid.
        while True:
            try:
                maximum = int(input("Enter the maximum age of your data sample: "))
                if ((maximum < 0) or (maximum > 122) or (minimum > maximum)):
                    print("Our data sample currently only covers ages within the ranges of 0 to 122. Please enter a year within that range that is higher than the minimum.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an age between 0 and 122 that is higher than the minimum.")

        # Prompt the user to enter a year between 1880 and 2022. Loop if they do not enter a valid value.
        while True:
            try:
                year = int(input("Finally, please enter the year that your data was collected: "))
                if ((year < 1880) or (year > 2022)):
                    print("Our data sample currently only covers years within the ranges of 1880 to 2022. Please enter a year within that range.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a year between 1880 and 2022.")

        minYear = year - maximum
        maxYear = year - minimum

        if (minYear < 1880):
            print("It looks like your minimum age is too low to be accurately simulated by our dataset. The minimum year for your range would be below 1880, which is the lowest year this system can simulate.")
        else:
            print("For your age range, you will want to set the minimum year as", minYear, "and the maximum as", maxYear, ".")

    # Exit function.
    def choiceFive(self):
        exit(1)

# Gender simulation object with each function defining the formatting section for single year, multiple years, and the ending portion that uses the formatted data
# from both.
# NOTE: Might be able to further condense some of this into formattedSimulation and choiceOne of the menu object.
class GenderSimulation:
    def __init__(self, mydb):
        self.mydatabase = mydb

    ######################################################################################################
    # Section 3.1: SINGLE YEAR
    # - Prompt user to select file name and year.
    # - Use the year to do an SQL query for that year and each name in the file.
    # - Call formattedSimulation with the results.
    ######################################################################################################

    # Function for when there's only a single year.
        # Ex.) ('2002')
    def singleYear(self):

        ######################################################################################################
        # Section 3.2: LOCATE & COPY FILE
        # - Prompts the user to enter their file name.
        #   + NOTE: It is best practice to load the file containing the data into the folder containing this program.
        # - Validates that the user's file exists and loops if not found.
        # - Creates a copy of user's file to ensure the original data is not modified.
        ######################################################################################################

        os.system('cls') # Clear screen
        print("|---------------------------------------- Single Year ----------------------------------------|")

        # Prompt the user to enter a file name and display error if invalid.
        while True:
            fileName = input("Please enter the file name: ")
            if os.path.isfile(fileName):
                source_file = fileName
                destination_file = "dataWithGenderCategory.csv"

                try:
                    shutil.copyfile(source_file, destination_file)
                    #print(f"CSV file '{source_file}' copied successfully to '{destination_file}'.")
                except FileNotFoundError:
                    print("File not found. Please check the path and try again.")
                break
            else:
                print("File not found. Please enter a valid file name.")

        # Create cursor object.
        myCursor = self.mydatabase.cursor()

        ######################################################################################################
        # Section 3.3: SELECT YEAR
        # - Prompts the user to enter the year to compare the names to.
        # - Validates user input (must be between 1880 and 2022) and loops if invalid.
        # + NOTE: The reason the range is 1880 to 2022 is that the SSA Baby Names dataset that is used for
        #         processing the names at each give year only exists within that range.
        ######################################################################################################

        # Prompt the user to enter a year between 1880 and 2022. Loop if they do not enter a valid value.
        while True:
            try:
                year = int(input("Enter the year (e.g., 2000): "))
                if year < 1880 or year > 2022:
                    print("Our data sample currently only covers years between 1880 and 2022. Please provide a year within that range.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a year between 1880 and 2022.")

        # Select the database.
        myCursor.execute("USE yearsandnames;")

        # Declare variables.
        foundNames = []
        notFoundNames = 0
        columnNumber = 0

        #print()
        #print("Extracting from data...")

        # Open and read the CSV file.
        with open(fileName, newline='') as csvfile:
            csvReader = csv.reader(csvfile)
            count = 0

            # Read the first row to determine the number of columns
            first_row = next(csvReader)
            num_columns = len(first_row)

            ######################################################################################################
            # Section 3.4.1: COMPARE FILE TO BABY NAME DATABASE (SINGLE COLUMN)
            # - Split each row by any spaces (' '). This extracts only first names.
            # - Run SQL Query at the given year with the first name.
            # - Checks if a result is found.
            #   = Result is found: Append it to a new array.
            #   = Result is not found: Append the name with "N/A" as row[1] and row[2] for later processing.
            ######################################################################################################

            # If file is only a single column...
            if num_columns == 1:
                os.system('cls') # Clear screen
                print("This may take a few minutes. Please wait...")
                for row in csvReader:
                    data = row[columnNumber]
                    count = count + 1

                    # Split any full names by checking for spaces (' '). Only save the first name.
                    if ' ' in data:
                        name = data.split(" ", 1)[0]
                    else:
                        name = row[0]

                    # Perform SQL query.
                    sqlQuery = f"SELECT * FROM year{year} WHERE name = %s;"
                    myCursor.execute(sqlQuery, (name.capitalize(),))
                    results = myCursor.fetchall()

                    # If the query returns a result, append it to foundNames.
                    if results:
                        for dbRow in results:
                            #print(dbRow)
                            foundNames.append(dbRow)

                    # Append name and "N/A" to foundNames when the SQL query returns nothing.
                    else:
                        dbRow = (name, "N/A", "N/A")
                        #print(dbRow)
                        foundNames.append(dbRow)
                        notFoundNames += 1  # Counts any names that were not found.

            ######################################################################################################
            # Section 3.4.2: COMPARE FILE TO BABY NAME DATABASE (MULTIPLE COLUMNS)
            # - Prompt user to enter the number associated with their column. (A = 1, B = 2, Etc...)
            # - Check if input is valid, loop if not.
            # - Split each row by any spaces (' '). This extracts only first names.
            # - Run SQL Query at the given year with the first name.
            # - Checks if a result is found.
            #   = Result is found: Append it to a new array.
            #   = Result is not found: Append the name with "N/A" as row[1] and row[2] for later processing.
            ######################################################################################################

            # If file is multiple columns...
            else:
                #print("It looks like your data contains multiple columns.")

                # Prompt the user to enter which column their first names category is located in. Loop if incorrect input.
                while True:
                    try:
                        columnNumber = int(input("Please enter the column number associated with your data (i.e., the first column is column '1', the second column is column '2', etc.): "))

                        # Checks if the entered column number is within the populated columns.
                        if columnNumber < num_columns:
                            os.system('cls') # Clear screen
                            print("This may take a few minutes. Please wait...")

                            # Loop through each row and process data based on the specified column number.
                            for row in csvReader:
                                data = row[columnNumber - 1]
                                count = count + 1

                                # Multiple columns contains a space (indicating a full name).
                                if ' ' in data:
                                    name = data.split(" ", 1)[0]

                                # Multiple columns does not contain a space (indicating just a first name).
                                else:
                                    name = data

                                # Perform SQL query.
                                sqlQuery = f"SELECT * FROM year{year} WHERE name = %s;"
                                myCursor.execute(sqlQuery, (name.capitalize(),))
                                results = myCursor.fetchall()

                                # If the query returns a result, append it to foundNames.
                                if results:
                                    for dbRow in results:
                                        #print(dbRow)
                                        foundNames.append(dbRow)

                                # Append name and "N/A" to foundNames when the SQL query returns nothing.
                                else:
                                    dbRow = (name, "N/A", "N/A")
                                    #print(dbRow)
                                    foundNames.append(dbRow)
                                    notFoundNames += 1  # Counts any names that were not found.
                            break
                        else:
                            print("Invalid column number. Please enter a valid number.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

            confidenceScore = 100 - ((notFoundNames / count) * 100)

        # Declare variable.
        ranges = []

        # If the number of found names was zero, inform the user of the error and quit.
        if len(foundNames) == 0:
            print("The data that you have provided is either empty or were not found within any of the years specified.")
            print("If you believe this is an error, please check to ensure that your dataset is populated and that you are using the correct column if your data contains multiple columns.")
            quit()

        #print()
        #print("Found Names redone...")
        #for i in foundNames:
            #print(i)

        #print()
        #print("New rows...")

        combinedList = foundNames

        #for i in ranges:
            #print(i)

        #print()
        #print("After:")
        #for row in ranges:
            #print(row)

        new_row = ['DeleteMe', 1, 2]
        ranges.insert(0, new_row)

        fromMultiple = False

        # With everything formatted, call the remaining code function. This will run all other parts such as generating a random number, displaying results, and
        # creating a CSV to view the finalized results.
        self.formattedSimulation(ranges, columnNumber, confidenceScore, combinedList, fromMultiple)

        # Close cursor and connection.
        myCursor.close()
        self.mydatabase.close()

    ######################################################################################################
    # Section 4.1: MULTIPLE YEARS
    # - Prompt user to select file name and year range.
    # - Use the year range to do an SQL query for each year and each name in the file.
    # - Combine the names across years for a total list of occurrences from all the years.
    # - Call formattedSimulation with the results.
    ######################################################################################################

    # Function for when there is a year range.
        # Ex.) ('2002', '2003', '2004', '2005', '2006')
    def multipleYear(self):

        ######################################################################################################
        # Section 4.2: LOCATE & COPY FILE
        # - Prompts the user to enter their file name.
        #   + NOTE: It is best practice to load the file containing the data into the folder containing this program.
        # - Validates that the user's file exists and loops if not found.
        # - Creates a copy of user's file to ensure the original data is not modified.
        ######################################################################################################

        os.system('cls') # Clear screen
        print("|---------------------------------------- Multiple Years ----------------------------------------|")

        # Prompt the user to enter a file name and display error if invalid.
        while True:
            fileName = input("Please enter the file name: ")
            if os.path.isfile(fileName):
                source_file = fileName
                destination_file = "dataWithGenderCategory.csv"

                try:
                    shutil.copyfile(source_file, destination_file)
                    #print(f"CSV file '{source_file}' copied successfully to '{destination_file}'.")
                except FileNotFoundError:
                    print("File not found. Please check the path and try again.")
                break
            else:
                print("File not found. Please enter a valid file name.")

        # Create cursor object.
        mycursor = self.mydatabase.cursor()

        # Generate variables.
        yearRange = []
        yearRangeNext = 0
        yearIncrement = 0

        ######################################################################################################
        # Section 4.3: SELECT YEAR
        # - Prompts the user to enter the years to compare the names to.
        # - Validates user input (must be between 1880 and 2022, second must be bigger than first) and loops if invalid.
        # - Creates a list of years starting from the first and ending at the second.
        # + NOTE: The reason the range is 1880 to 2022 is that the SSA Baby Names dataset that is used for
        #         processing the names at each give year only exists within that range.
        ######################################################################################################

        # Prompt the user to input the desired year ranges.
        while yearRangeNext != 2:
            try:
                # Prompt the user to enter the minimum to the range.
                if yearRangeNext == 0:
                    year = int(input("Enter the first year (e.g., 1880 - 2022): "))

                    # Display error and loop if the user enters a year outside of 1880 to 2022.
                    if year < 1880 or year > 2022:
                        print("Our data sample currently only covers years between 1880 and 2022. Please provide a year within that range.")
                        continue

                    # Go to the maximum year selection if the minimum year is valid.
                    else:
                        yearRange.append(year)
                        yearRangeNext += 1
                        yearIncrement = year

                # Prompt the user to enter the maximum to the range.
                elif yearRangeNext == 1:
                    year2 = int(input(f"Enter a year higher than {yearRange[0]} and within 1880 - 2022: "))

                    # Display error and loop if the user enters a year lower than the first or higher than 2022.
                    if year2 <= yearRange[0] or year2 > 2022:
                        print("The second year must be higher than the first and within the range of 1880 to 2022.")
                        continue
                    
                    # Escape the year range selection with the generated range if the second year is valid.
                    else:
                        yearRange.append(year2)
                        yearRangeNext = yearRangeNext + 1

            # Displays error if user enters incorrect value.
            except ValueError:
                print("Invalid input. Please enter a valid year between 1880 and 2022.")

        #print("Year range selected:", yearRange) # Used for debugging. Displays year range.

        # Declare variables.
        totalYearRange = []
        foundNames = []
        notFoundNames = 0

        # Create a list of years from the starting year to the ending year.
        # Ex.) ('2002', '2006') becomes ('2002', '2003', '2004', '2005', '2006')
        while (yearIncrement != (yearRange[1] + 1)):
            totalYearRange.append(yearIncrement)
            yearIncrement = yearIncrement + 1
        #print(totalYearRange)

        # Select the database.
        # NOTE: Could move this to the function that calls multipleYear.
        mycursor.execute("USE yearsandnames;")

        #print()
        #print("Extracting from database...")

        # Declare variables.
        columnNumber = 0
        foundNames = []

        ######################################################################################################
            # Section 4.4.1: COMPARE FILE TO BABY NAME DATABASE (SINGLE COLUMN)
            # - Go year by year, running the processes below.
            #   = Split each row by any spaces (' '). This extracts only first names.
            #   = Run SQL Query at the given year with the first name.
            #   = Checks if a result is found.
            #       + Result is found: Append it to a new array.
            #       + Result is not found: Append the name with "N/A" as row[1] and row[2] for later processing.
            ######################################################################################################

        # Create a list of arrays so that each year is stored in a separate array within the list.
        # Ex.) ('year2002', 'year2003', 'year2004', 'year2005', 'year2006').
        for i in totalYearRange:
            yearData = []

            # Display which year is currently being run.
            # NOTE: If I implement the functionality that displays a progress bar, this is where it will likely be placed.
            #print()
            print(f"Running year {i}...")
            #print()

            # Open and read the CSV file.
            with open(fileName, newline='') as csvfile:
                # Create a CSV reader object
                csvreader = csv.reader(csvfile)
                newCount = 0

                # If file is only a single column...
                if len(next(csvreader)) == 1:
                    csvfile.seek(0)  # Reset the file pointer. Resource: https://www.geeksforgeeks.org/python-seek-function/

                    # Split any full names by checking for spaces (' '). Only save the first name.
                    for row in csvreader:
                        newCount = newCount + 1
                        data = row[columnNumber]
                        if ' ' in data:
                            name = data.split(" ", 1)[0]
                        else:
                            name = row[0]

                        name = name.capitalize()

                        # Perform SQL query.
                        sqlQuery = f"SELECT * FROM year{i} WHERE name = %s;"
                        mycursor.execute(sqlQuery, (name,))
                        results = mycursor.fetchall()

                        # If the query returns a result, append it to the yearData for the corresponding year.
                        if results:
                            for dbRow in results:
                                #print(dbRow)
                                yearData.append(list(dbRow))  # Convert tuple to list and append to yearData
                        else:
                            # Append name and "N/A" to foundNames when the SQL query returns nothing.
                            dbRow = [name, "N/A", "N/A"]
                            #print(dbRow)
                            yearData.append(dbRow)
                            notFoundNames += 1  # Counts any names that were not found.

            ######################################################################################################
            # Section 4.4.2: COMPARE FILE TO BABY NAME DATABASE (MULTIPLE COLUMNS)
            # - Prompt user to enter the number associated with their column. (A = 1, B = 2, Etc...)
            # - Check if input is valid, loop if not.
            # - Split each row by any spaces (' '). This extracts only first names.
            # - Run SQL Query at the given year with the first name.
            # - Checks if a result is found.
            #   = Result is found: Append it to a new array.
            #   = Result is not found: Append the name with "N/A" as row[1] and row[2] for later processing.
            ######################################################################################################

                # If CSV is multiple columns...
                else:
                    #print("It looks like your data contains multiple columns.")

                    # Prompt the user to enter which column their first names category is located in. Loop if incorrect input.
                    while True:
                        try:
                            if columnNumber == 0:
                                columnNumber = int(input("Please enter the column number associated with your data (i.e., the first column is column '1', the second column is column '2', etc.): "))

                            csvfile.seek(0)  # Reset the file pointer
                            for row in csvreader:
                                newCount = newCount + 1
                                if columnNumber <= len(row):
                                    data = row[columnNumber - 1]

                                    # Multiple columns contain a space (indicating a full name)
                                    if ' ' in data:
                                        name = data.split(" ", 1)[0]

                                    # Multiple columns do not contain a space (indicating just a first name)
                                    elif ' ' not in data:
                                        name = data

                                    name = name.capitalize()

                                    # Perform SQL query.
                                    sqlQuery = f"SELECT * FROM year{i} WHERE name = %s;"
                                    mycursor.execute(sqlQuery, (name,))
                                    results = mycursor.fetchall()

                                    # If the query returns a result, append it to the yearData for the corresponding year.
                                    if results:
                                        for dbRow in results:
                                            #print(dbRow)
                                            yearData.append(list(dbRow))  # Convert tuple to list and append to yearData
                                    else:
                                        # Append name and "N/A" to foundNames when the SQL query returns nothing.
                                        dbRow = [name, "N/A", "N/A"]
                                        #print(dbRow)
                                        yearData.append(dbRow)
                                        notFoundNames += 1  # Counts any names that were not found.
                            break

                        # Error for if the user enters a column number that does not align with the total number of columns in their file.
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")

            # Append yearData to foundNames.
            foundNames.append(yearData)

            #print("foundNames:", foundNames) # Used for debugging and displaying which names were found and their corresponding values.

            #print()
            #print("Result...")
            #print(finalResult)
            #print()

        ######################################################################################################
        # Section 4.5: CREATE COMBINED LIST
        # - Set all 'N/As' to 0 which will receive a 50/50 gender marker later on.
        # - For each row in the first year of foundNames, check the other years for matches and add their totals.
        # + NOTE: It is not necessary to check any year after the first year, as they all contain the same names.
        ######################################################################################################

        # Convert "N/A" to 0 in foundNames. This has to be done due to the code trying to skip zero values.
        for yearData in foundNames:
            for row in yearData:
                for i in range(len(row)):
                    if row[2] == "N/A":
                        row[1] = 0
                        row[2] = 0

        combinedList = []

        for row in foundNames[0]:
            name, gender, value = row
            total_value = value
            for other_arr in foundNames[1:]:
                for other_row in other_arr:
                    if other_row[0] == row[0] and other_row[1] == row[1]:
                        total_value += other_row[2]
            combinedList.append([row[0], row[1], total_value])

        # Display the combined values.
        #print()
        #print("Combined Values: ")
        #print(combinedList)

        # Display the number in foundNames.
        #print()
        #print("FoundNames length: ")
        #print(len(foundNames[0]))

        confidenceScore = 100 - (((notFoundNames / len(foundNames)) / newCount) * 100)

        ranges = []

        # If the number of found names was zero, inform the user of the error and quit.
        if len(combinedList) == 0:
            print("The data that you have provided is either empty or were not found within any of the years specified.")
            print("If you believe this is an error, please check to ensure that your dataset is populated and that you are using the correct column if your data contains multiple columns.")
            quit()

            #print(newRow)

        #print()
        #print("After:")
        #for row in ranges:
            #print(row)
        #print()

        fromMultiple = True

        # With everything formatted, call the remaining code function. This will run all other parts such as generating a random number, displaying results, and
        # creating a CSV to view the finalized results.
        self.formattedSimulation(ranges, columnNumber, confidenceScore, combinedList, fromMultiple)

        # Close cursor and connection.
        mycursor.close()
        self.mydatabase.close()

    def formattedSimulation(self, ranges, columnNumber, confidenceScore, combinedList, fromMultiple):
        
        os.system('cls') # Clear screen

        ######################################################################################################
        # Section 5.2: PROCESS COMBINEDLIST
        # - This section loops through all of the names and merges where the names match according to various conditions.
        # - Last row is handled seprately due to there being nothing to compare nextRow to.
        # - Each condition is listed above each section.
        # + NOTE: If encountering issues where genders are consistently incorrectly assigned, the issue is likely from this area.
        ######################################################################################################

        # Loop through each row.
        #print("Comparing names to find ones with gender variances...")
        for i in range(len(combinedList)):
            currentRow = combinedList[i]
            newRow = []

            # Check various conditions and assign positive or negative values to each gender.
            # Ex.) ('William', 'F', 24) stays positive and ('William', 'M', 20109) is changed to negative for a result of ('William', -20109, 24).
            
            if i < len(combinedList) - 1:
                nextRow = combinedList[i + 1]
                prevRow = combinedList[i - 1]

                if currentRow[1] == 0:
                    newRow.append(currentRow[0])
                    newRow.append(0)
                    newRow.append(0)
                    ranges.append(newRow)
                
                # If the next row is the same, set the gender range. Do not set a name with a female marker to negative.
                if (currentRow[0] == nextRow[0]) and (currentRow[1] != nextRow[1]):
                    if nextRow[1] != "F":
                        newRow.append(currentRow[0])
                        newRow.append(nextRow[2] * -1)
                        newRow.append(currentRow[2])
                        ranges.append(newRow)
                    continue

                # If the next row is the same, set the gender range. Do not set a name with a female marker to negative.
                if (currentRow[0] == nextRow[0]) and (currentRow[1] == nextRow[1]) and (currentRow[1] == "F"):
                    newRow.append(currentRow[0])
                    newRow.append(1)
                    newRow.append(2)
                    ranges.append(newRow)
                    continue

                # If the next row is the same, set the gender range. Do not set a name with a female marker to negative.
                if (currentRow[0] == nextRow[0]) and (currentRow[1] == nextRow[1]) and (currentRow[1] == "M"):
                    newRow.append(currentRow[0])
                    newRow.append(-2)
                    newRow.append(-1)
                    ranges.append(newRow)
                    continue

                # If the next row is the same, set the gender range. Do not set a name with a female marker to negative.
                if (currentRow[0] == nextRow[0]) and (currentRow[1] == nextRow[1]) and (currentRow[1] == "N/A"):
                    newRow.append(currentRow[0])
                    newRow.append(0)
                    newRow.append(0)
                    ranges.append(newRow)
                    continue

                # If the next row is the same, set the gender range. Do not set a name with a female marker to negative.
                if (currentRow[0] == prevRow[0]) and (currentRow[1] == prevRow[1]) and (currentRow[1] == "F"):
                    newRow.append(currentRow[0])
                    newRow.append(1)
                    newRow.append(2)
                    ranges.append(newRow)
                    continue

                # If the next row is the same, set the gender range. Do not set a name with a female marker to negative.
                if (currentRow[0] == prevRow[0]) and (currentRow[1] == prevRow[1]) and (currentRow[1] == "M"):
                    newRow.append(currentRow[0])
                    newRow.append(-2)
                    newRow.append(-1)
                    ranges.append(newRow)
                    continue

                # If the next row is the same, set the gender range. Do not set a name with a female marker to negative.
                if (currentRow[0] == prevRow[0]) and (currentRow[1] == prevRow[1]) and (currentRow[1] == "N/A"):
                    newRow.append(currentRow[0])
                    newRow.append(0)
                    newRow.append(0)
                    ranges.append(newRow)
                    continue

            # Handle the last row
            if i > 0:
                prevRow = combinedList[i - 1]
                # If there is only one row and it indicates female, set a positive range.
                if (currentRow[0] != prevRow[0]) and (currentRow[1] == "F"):
                    newRow.append(currentRow[0])
                    newRow.append(1)
                    newRow.append(2)
                    ranges.append(newRow)
                    continue
                # If there is only one row and it indicates male, set a negative range.
                elif (currentRow[0] != prevRow[0]) and (currentRow[1] == "M"):
                    newRow.append(currentRow[0])
                    newRow.append(-2)
                    newRow.append(-1)
                    ranges.append(newRow)
                    continue
                # If there is only one row and it indicates an unknown name, set to zero.
                elif (currentRow[0] != prevRow[0]) and (currentRow[1] == "N/A"):
                    newRow = [currentRow[0], 0, 0]
                    ranges.append(newRow)
                    continue
            # If this is the only row
            else:
                # If there is only one row and it indicates female, set a positive range.
                if currentRow[1] == "F":
                    newRow.append(currentRow[0])
                    newRow.append(1)
                    newRow.append(2)
                    ranges.append(newRow)
                    continue
                # If there is only one row and it indicates male, set a negative range.
                elif currentRow[1] == "M":
                    newRow.append(currentRow[0])
                    newRow.append(-2)
                    newRow.append(-1)
                    ranges.append(newRow)
                    continue
                # If there is only one row and it indicates an unknown name, set to zero.
                elif currentRow[1] == "N/A":
                    newRow = [currentRow[0], 0, 0]
                    ranges.append(newRow)
                    continue

        # Print all ranges.
        #print()
        #print("Names with gender ranges: ")
        #print(ranges)
        #print()

        ######################################################################################################
        # Section 5.3: RANDOM NUMBER GENERATOR
        # - For each row, set the minimum to the first number and maximum to the second number, establishing a range.
        # - Create a random number within the range.
        #   = If the random number is negative, assign it a male marker.
        #   = If the random number is positive, assign it a female marker.
        ######################################################################################################

        namesAndGenders = []

        for i in ranges:
            #print(i)
            # Create a minimum to the possible random numbers and a maximum to the possible random numbers.
            # Ex.) ('Sarah', -23, 2134) creates a min of -23 and a max of 2134.
            minValue = i[1]
            maxValue = i[2]

            # Generate a random number within the defined range.
            randomNumber = random.randint(minValue, maxValue)
            
            # If random number is above zero, assign a female marker.
            if randomNumber > 0:
                gender = "F"

            # If random number is below zero, assign a male marker.
            elif randomNumber < 0:
                gender = "M"

            # If random number is exactly zero, check which gender the name is represented by the most and assign it to that gender.
            elif randomNumber == 0:
                if (minValue * -1) < maxValue:
                    gender = "F"
                elif (minValue * -1) > maxValue:
                    gender = "F"
                
                # Subset of the above part, if random number is exactly zero and they're represented equally, utlizing a 50/50 tiebreaker.
                elif (minValue * -1) == maxValue:
                    tieBreaker = random.randint(1, 2)
                    if tieBreaker == 1:
                        gender = "F"
                    elif tieBreaker == 2:
                        gender = "M"

            # Append the name and corresponding gender to the list.
            namesAndGenders.append([i[0], gender])

        # For each name, print the element with the corresponding generated gender.
        #print("Names with assigned gender markers: ")
        #print(namesAndGenders)

        ######################################################################################################
        # Section 5.4: CREATE RESULTS FILE
        # - Create a new CSV for the results.
        # - Prompt user to enter if the data contains headers.
        #   = Yes: Remove the first row and create a category header named 'SimulatedGender'.
        #   = No: Continue as normal.
        # - Add the remaining rows as normal.
        ######################################################################################################

        input_csv = "dataWithGenderCategory.csv"
        output_csv = "ResultFile.csv"

        with open(input_csv, 'r', newline='') as infile, open(output_csv, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            # Prompt the user for headers
            while True:
                answer = input("Does your data contain headers? Please type either 'Yes' or 'No': ")
                if answer.lower() == 'yes':
                    # Read and copy the first row with a blank in the new column
                    
                    # Remove the first row
                    namesAndGenders = namesAndGenders[1:]

                    header = next(reader)
                    header.insert(columnNumber, 'SimulatedGender')  # Leave a blank in the new column
                    writer.writerow(header)
                    break
                elif answer.lower() == 'no':
                    break
                else:
                    print("Invalid input. Please type either 'Yes' or 'No'.")

            for row, new_data in zip(reader, namesAndGenders):
                if columnNumber > 1:
                    row.insert(columnNumber, new_data[1])  # Adjusting index to match Python's zero-based indexing
                else:
                    row.insert(1, new_data[1])
                writer.writerow(row)

            infile.close()
            outfile.close()

            if os.path.exists("dataWithGenderCategory.csv"):
                os.remove("dataWithGenderCategory.csv")

        ######################################################################################################
        # Section 5.1: CONFIDENCE SCORE
        # - Divide the names that weren't found by the count of all names.
        # - Display score and associated rating.
        #   + NOTE: This section is non-functional and is merely used to explain what percent of the names
        #           in the user's dataset were also found within the recorded SSA Baby Names database for
        #           that year. In short, a high confidence score is good and means more names were found and
        #           weighted appropriately while a low score means the program will need to do a lot of
        #           randomized 50/50 guesswork for the simulation which is not as good. Ratings do not change
        #           between runs of the same parameters.
        #           As of currently, the author has found the common ideal rating between 85% and 100%.
        #   + NOTE: Any score below 30 strongly indicates an issue with the dataset. If repeatedly encountering
        #           a score this low, please ensure that the correct dataset and column number is selected.
        ######################################################################################################

        if fromMultiple == False:
            # Display the total number of names that were not found.
            print()
            #print("Names not found: ", notFoundNames) # Should be notFoundNames/years for multiple years.
            print("Confidence rating: %", round(confidenceScore, 2))
            
            if confidenceScore == 0:
                print("None of the names from your dataset were recorded in your selected year.")
            elif 0 <= confidenceScore < 10:
                print("Extremely few names from your dataset were recorded in your selected year.")
            elif 10 <= confidenceScore < 20:
                print("A very low number of names from your dataset were recorded in your selected year.")
            elif 20 <= confidenceScore < 30:
                print("A low number of names from your dataset were recorded in your selected year.")
            elif 30 <= confidenceScore < 40:
                print("Under half of names from your dataset were recorded in your selected year.")
            elif 40 <= confidenceScore < 50:
                print("A little under half of the names from your dataset were recorded in your selected year.")
            elif 50 <= confidenceScore < 60:
                print("A little over half of the names from your dataset were recorded in your selected year.")
            elif 60 <= confidenceScore < 70:
                print("Over half of the names from your dataset were recorded in your selected year.")
            elif 70 <= confidenceScore < 80:
                print("A high number of the names from your dataset were recorded in your selected year.")
            elif 80 <= confidenceScore < 90:
                print("A very high number of the names from your dataset were recorded in your selected year.")
            elif 90 <= confidenceScore < 100:
                print("Almost all of the names from your dataset were recorded in your selected year.")
            elif confidenceScore == 100:
                print("All of the names from your dataset were recorded in your selected year.")

        ######################################################################################################
        # Section 5.5: SNAPSHOT RESULTS
        # - Count the number of 'F' and 'M' markers.
        # - Display the percentages of each, rounded to the second decimal place.
        ######################################################################################################

        # Declare variables.
        femaleCount = 0
        maleCount = 0

        # Increment both gender tallies.
        for i in namesAndGenders:
            if i[1] == "F":
                femaleCount = femaleCount + 1
            else:
                maleCount = maleCount + 1

        # Display final percentages of each gender represented in the data.
        print()
        print("Name percentages: ")
        print("The percent of females are: ", str(round(femaleCount / (femaleCount + maleCount), 2)))
        print("The percent of males are: ", str(round(maleCount / (femaleCount + maleCount), 2)))

main()
