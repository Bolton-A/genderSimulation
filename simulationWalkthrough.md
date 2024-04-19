## [Step-by-Step Simulation Instructions](https://github.com/Bolton-A/genderSimulation/blob/main/PythonSimulation.py)

### Navigating the Menu
1. Complete the steps for downloading and installing MySQL, populating the database, connecting it to Python, and then downloading the simulation code. That process is outlined [here](https://github.com/Bolton-A/genderSimulation/blob/main/README.md).
2. Click the ```Run``` button in the toolbar of Visual Studio Code.
3. Select ```Run Without Debugging```.
4. You will be shown the menu below. Type the number corresponding with your selection on the keyboard and then press ```enter```. If you want to run a dataset collected from a variety of ages and you are not already aware of the earliest and latest years the data was from, then I suggest selecting ```4``` to calculate the necessary range. More on that later.
```
#################### MENU ####################
|            1. Run Simulation               |
|            2. Visit Website                |
|            3. View Github                  |
|            4. Calculate Year Range         |
|            5. Quit Application             |
##############################################
```
**1. Run Simulation**
1. After selecting ```1```, you will be shown the following interface. This interface will walk you through the process of selecting between running names and genders from a single year or set of years and generating a resulting dataset.
```
|---------------------------------------- Run Simulation ----------------------------------------|
Would you like to filter your data for a single year (Ex. Only people born in 1997) or would you like to select a range of years (Ex. People born from 1997 to 2002)?
Please type either 'single' or 'range': 
```
2. For your first choice, you will choose if you are running names from only a single year or a range of years. It is also important to note that while running as a range can improve accuracy, it is best used by breaking your dataset into even groups and running each group as a separate range for maximum accuracy.
```markdown
| Single                                                
| ✅ Quick                                                |
| ✅ Low horsepower                                       |
| ✅ Good for shared age                                  |  
| ❌ Not accurate at reflecting gender/naming trends      |

| Range
| ✅ Reflects gender/naming trends                        |
| ✅ More likely to pick up obscure names                 |
| ❌ Slow                                                 |
| ❌ High horsepower                                      |
```
> [!NOTE]
> If your data does not contain ages or a specified year of collection, then you may need to assign the year(s) at your own discretion.

**2. Single**
1. If you select 'single', then you will be provided the prompt below. It is encouraged to place the sample that you are copying into the same folder as the simulation code. After you do that, you can simply enter the file name and press ```enter```. (Ex. 'sampleNames.csv')
```
Please enter the file name:
```
2. Next, you will be given the prompt below. This is where you enter the year that you would like the code to compare names from. (Ex. If your dataset surveys 70 year olds and is from the year 2024, then you would calculate 2024 - 70 = 1954, that being the year that you type before pressing ```enter```.
```
Enter the year (e.g., 2000):
```
3. If your dataset contains multiple columns, then the code will provide you the additional prompt below. To figure out which column you need, simply open your dataset and check where the name or first name column is. If it is in column A, then you will type ```1```, if it is in column B, then you will type ```2```, etc. Once you have typed the number corresponding with your column, press ```enter```.
```
Please enter the column number associated with your data (i.e., the first column is column '1', the second column is column '2', etc.):
```
4. Next, you will be shown the message below. This means that the program is calculating the results. Shorter lists of names 1 to 100 should take only a few seconds while longer lists can take much longer. Just let the code run and it will inform you when it is complete.
```
This may take a few minutes. Please wait...
```
5. Lastly, you will be asked if your dataset contains headers, as shown below. Simply respond ```yes``` or ```no``` depending on your dataset and proceed.
```
Does your data contain headers? Please type either 'Yes' or 'No':
```
6. Lastly, the code will display a section similar to below. This means that it has successfully completed running and that the results can be found through the file ```FinalResults.csv``` within the folder containing the simulation. To run another simulation, simply press enter and it will take you back to the main menu.
```
Confidence rating: % __.__
A ____ number of the names from your dataset were recorded in your selected year.

Name percentages:
The percent of females are:  0.__
The percent of males are:  0.__
Press Enter to continue...
```

**3. Range**
1. If you select 'range', then you will be provided the prompt below. It is encouraged to place the sample that you are copying into the same folder as the simulation code. After you do that, you can simply enter the file name and press ```enter```. (Ex. 'sampleNames.csv')
```
Please enter the file name:
```
2. Next, you will be given the prompt below. This is where you enter the lowest year that you would like the code to compare names from. (Ex. If your dataset surveys 21 to 24 year olds and is from the year 2024, then you would calculate 2024 - 24 = 2000 (as 24 is the higher value and will therefore return the minimum), 2000 being the year that you type before pressing ```enter```.
```
Enter the first year (e.g., 1880 - 2022): 
```
3. Similar to the above, you will be given the prompt below. This is where you enter the highest year that you would like the code to compare names from. (Ex. If your dataset surveys 21 to 24 year olds and is from the year 2024, then you would calculate 2024 - 21 = 2003 (as 21 is the higher value and will therefore return the minimum), 2000 being the year that you type before pressing ```enter```.
```
Enter a year higher than ____ and within 1880 - 2022:
```
4. If your dataset contains multiple columns, then the code will provide you the additional prompt below. To figure out which column you need, simply open your dataset and check where the name or first name column is. If it is in column A, then you will type ```1```, if it is in column B, then you will type ```2```, etc. Once you have typed the number corresponding with your column, press ```enter```. In instances where there are multiple columns, this may appear after the indicator in point 5. However, you will need to enter a column number before it will truly begin calculating anything.
```
Please enter the column number associated with your data (i.e., the first column is column '1', the second column is column '2', etc.):
```
5. Next, you will be shown the message below. Ranges tend to run much slower than singles, so be prepared to wait a bit longer.
```
Running year ____...
```
6. Lastly, you will be asked if your dataset contains headers, as shown below. Simply respond ```yes``` or ```no``` depending on your dataset and proceed.
```
Does your data contain headers? Please type either 'Yes' or 'No':
```
7. Lastly, the code will display a section similar to below. This means that it has successfully completed running and that the results can be found through the file ```FinalResults.csv``` within the folder containing the simulation. To run another simulation, simply press enter and it will take you back to the main menu. Note that the ranges do not provide a confidence rating due to how they are processed.
```
Name percentages:
The percent of females are:  0.__
The percent of males are:  0.__
Press Enter to continue...
```
**4. Visit Website**
1. Simply press ```2``` on your keyboard and then press ```enter``` and you will be taken to the website documenting this tool.

**5. Visit Github**
1. Simply press ```3``` on your keyboard and then press ```enter``` and you will be taken to the Github repository of this tool.

**6. Calculate Year Range**
1. Press ```4``` on your keyboard and then press ```enter``` and you will be taken to the year range calculator. This simple calculator is used for calculating what year(s) you will need to specify for step 2 of Single and steps 2 and 3 of Range. It will require the use of an age category within your dataset as well as the year that your dataset was created.
2. Within your dataset, locate the youngest age. This can be easily done by clicking the column with the ages and sorting descending, at which point the lowest age should be on top. Type that when the code provides the prompt below.
```Enter the minimum age of your data sample:```
4. Within your dataset, locate the oldest age. This can be easily done by clicking the column with the ages and sorting ascending, at which point the highest age should be on top. Type that when the code provides the prompt below.
```Enter the maximum age of your data sample:```
5. Locate the year that your dataset was sourced from or the year that it was created. Type that when the code provides the prompt below.
```Finally, please enter the year that your data was collected:```
6. The code should display a result similar to the below section. Press ```enter``` to continue onto the next section after taking note of the range that it provides.
```
For your age range, you will want to set the minimum year as ____ and the maximum as ____ .
Press Enter to continue...
```

**7. Quit Application**
1. Simply either exit out of the run by pressing the red square at the top or by typing ```5``` and then pressing ```enter```. With this, the code will close.
> [!CAUTION]
> Unless the results have already been written to ResultFile.csv, any progress will not be saved.
