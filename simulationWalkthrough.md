## [Step-by-Step Simulation Instructions](https://github.com/Bolton-A/genderSimulation/blob/main/PythonSimulation.py)

### Navigating the Menu
1. Complete the steps for downloading and installing MySQL, populating the database, connecting it to Python, and then downloading the simulation code. That process is outlined [here](https://github.com/Bolton-A/genderSimulation/blob/main/README.md).
2. Click ```Run``` at the top banner of Visual Studio Code with the simulation code opened.
3. Click ```Run Without Debugging``` in the panel that opens after step 2. This will launch your code.
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
