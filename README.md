<h1 align="center">Gender Distribution Simulation Tool</h1>
<p align="center"><i>A tool for generating a simulated gender distribution that accounts for gender ambiguity using a first name category.</i></p>
<div align="center">
  <a href="https://github.com/Bolton-A/genderSimulation/stargazers"><img src="https://img.shields.io/github/stars/Bolton-A/genderSimulation" alt="Stars Badge"/></a>
<a href="https://github.com/Bolton-A/genderSimulation/network/members"><img src="https://img.shields.io/github/forks/Bolton-A/genderSimulation" alt="Forks Badge"/></a>
<a href="https://github.com/Bolton-A/genderSimulation/pulls"><img src="https://img.shields.io/github/issues-pr/Bolton-A/genderSimulation" alt="Pull Requests Badge"/></a>
<a href="https://github.com/Bolton-A/genderSimulation/issues"><img src="https://img.shields.io/github/issues/Bolton-A/genderSimulation" alt="Issues Badge"/></a>
<a href="https://github.com/Bolton-A/genderSimulation/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Bolton-A/genderSimulation?color=2b9348"></a>
</div>
<br>
<!-- Note: This link is currently set up with the localhost and is not enabled for outside access. -->
<p align="center"><i>Interested in this project? Visit the <a href="http://localhost:3000/">website</a> to learn more!</i></p>
<br>
This code contains the simulation tool portion of my final project for CISS:451 or 'Senior Projects I', completed during my final Spring 2024 semester. This project is intended to showcase a variety of skills in designing programming systems, implementing frameworks and libraries, and creating a cohesive and useful code from the ground up. 
<br>
<br>
If you like this project, Please click the :star:!
<br>
<br>
A detailed explanation of the code and how to use it is below.

## Setting Up

**Database Instructions**
1. Install and set up a [MySQL database](https://dev.mysql.com/downloads/installer/). Write down your host, username, password, and port; as these will all be used in future steps.
2. Download the folder ['CreateDatabase'](https://github.com/Bolton-A/genderSimulation/blob/main/CreateDatabase.zip). In that folder, you will find a list of .xlsx files reading 'yob1880', 'yob1881', etc. Ensure that these files are in the same folder as 'importToMySQL.py'.
3. Open 'importToMySQL.py'. Within the code, locate the block of text below and change it so that your host, username, password, and port aligns with what you set up for your MySQL.
```
mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="password",
                passwd="password",
                port=3306
            )
```
4. Use ``` pip install _____``` to add any imports that return an error when attempting to run, replacing the blank with the specified import.
5. Click 'Run' and give the program a few minutes to run. It will indicate which year it is currently on throughout the run process.
6. Upon completion, you will be ready to run '[PythonSimulation.py](https://github.com/Bolton-A/genderSimulation/blob/main/PythonSimulation.py)'!

**Simulation Instructions**
1. Download the code in '[PythonSimulation.py](https://github.com/Bolton-A/genderSimulation/blob/main/PythonSimulation.py)' and open it within your preferred code editor.
2. Within the code, locate the block of text below and change it so that your host, username, password, and port aligns with what you set up for your MySQL. (If you did not setup MySQL, please reference the above section.)
```
mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="password",
                passwd="password",
                port=3306
            )
```
3. Use ``` pip install _____``` to add any imports that return an error when attempting to run, replacing the blank with the specified import.
4. Click 'Run' and follow the prompts for a successful run! Below, you will find a detailed guide on how to use the system, a reference for all of the sample datasets, and an introduction to the website documenting this application.

## Running The Application

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
|            4. Quit Application             |
##############################################
```
***1. Run Simulation***
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

***2. Single***
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

***3. Range***
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
***4. Visit Website***
1. Simply press ```2``` on your keyboard and then press ```enter``` and you will be taken to the website documenting this tool.

***5. Visit Github***
1. Simply press ```3``` on your keyboard and then press ```enter``` and you will be taken to the Github repository of this tool.

**6. Quit Application**
1. Simply either exit out of the run by pressing the red square at the top or by typing ```5``` and then pressing ```enter```. With this, the code will close.
> [!CAUTION]
> Unless the results have already been written to ResultFile.csv, any progress will not be saved.

## Samples
- [actors2307](https://github.com/Bolton-A/genderSimulation/blob/main/SampleDatasets/actors2307.csv): The largest sample dataset of the group, this sample contains 2307 actors from SNL and contains a gender category that you can use for comparing the system's results against the real life values. Do note that this sample does also contain 'unknown' and 'andy' values as well as stage names, meaning that you may need to filter those out of the results to see the system's true accuracy. Click [here](https://www.kaggle.com/datasets/hhllcks/snldb) for source.
- [forbes200.csv](https://github.com/Bolton-A/genderSimulation/blob/main/SampleDatasets/forbes200.csv): The second largest sample dataset of the group, this sample contains 200 of the wealthiest people in the United States. There is not a gender category pre-existing within this dataset, which can further solidify the system's abilities to function only using the names category. Click [here](https://www.kaggle.com/datasets/ayessa/forbes-top-200-richest-american) for source.
- [wrestling115.csv](https://github.com/Bolton-A/genderSimulation/blob/main/SampleDatasets/wrestling115.csv): This file is moderately small and contains information on 115 U.S. wrestlers that attended a wrestling event. This file contains a gender category for you to compare your results to. Click [here](https://www.kaggle.com/datasets/julienjta/wrestling-world-tournament) for source.
- [wrestlingRange1.csv](https://github.com/Bolton-A/genderSimulation/blob/main/SampleDatasets/wrestlingRange1.csv): This sample is a subset of the above and contains 50 records run with the range of 1976 to 1990 (taken from the age column). This sample is best used in combination with wrestlingRange2.csv to demonstrate the higher accuracy of doing split ranges. Click [here](https://www.kaggle.com/datasets/julienjta/wrestling-world-tournament) for source.
- [wrestlingRange2.csv](https://github.com/Bolton-A/genderSimulation/blob/main/SampleDatasets/wrestlingRange2.csv): This sample isa  subset of wrestling115.csv and contains 64 records with the range of 1991 to 2004 (taken from the age column). This sample is best used in combination with wrestlingRange1.csv to demonstrate the higher accuracy of doing split ranges. Click [here](https://www.kaggle.com/datasets/julienjta/wrestling-world-tournament) for source.

<!-- Note: These links are currently set up with the localhost and is not enabled for web access. -->
## [Website](http://localhost:3000/)

![image](https://github.com/Bolton-A/genderSimulation/assets/112293016/062056df-b06d-4791-b582-9b611068a0b5)

Early in the project's development, I planned on creating a website interface in order to provide the users with a simple graphical interface to process their datasets with. While that is still a feature that I plan to implement in the future, the current iteration of the project has been divided so that the frontend website explains the tool and it's features while the separate tool provides the functionality of the tool. You can find various links to information compiled on the website below.

- [Home](http://localhost:3000/)
- [About](http://localhost:3000/about)
- [Terms Of Use](http://localhost:3000/termsofuse)
- [Contact](http://localhost:3000/contact)

# Contribute

Contributions are always welcome! Please create a pull request or contact me.

## :man_astronaut: Show your support

Give a ⭐️ if you enjoyed this project!
