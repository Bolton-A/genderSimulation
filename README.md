<h1 align="center">Gender Distribution Simulation Tool</h1>
<p align="center"><i>A tool for generating a simulated gender distribution that accounts for gender ambiguity using a first name category.</i></p>
<div align="center">
  <a href="https://github.com/Bolton-A/genderSimulation/stargazers"><img src="https://img.shields.io/github/stars/Bolton-A/genderSimulation" alt="Stars Badge"/></a>
<a href="https://github.com/Bolton-A/genderSimulation/network/members"><img src="https://img.shields.io/github/forks/Bolton-A/genderSimulation" alt="Forks Badge"/></a>
<a href="https://github.com/Bolton-A/genderSimulation/pulls"><img src="https://img.shields.io/github/issues-pr/Bolton-A/genderSimulation" alt="Pull Requests Badge"/></a>
<a href="https://github.com/Bolton-A/genderSimulation/issues"><img src="https://img.shields.io/github/issues/Bolton-A/genderSimulation" alt="Issues Badge"/></a>
<a href="https://github.com/Bolton-A/genderSimulation/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Bolton-A/genderSimulation?color=2b9348"></a>
<a href="https://github.com/Bolton-A/genderSimulation/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Bolton-A/genderSimulation?color=2b9348" alt="License Badge"/></a>
</div>
<br>
<!-- Note: This link is currently set up with the localhost and is not enabled for outside access. -->
<p align="center"><i>Interested in this project? Please visit my <a href="http://localhost:3000/">Website</a>.</i></p>
<br>
This code contains the simulation tool portion of my final project for CISS:451 or 'Senior Projects I', completed during my final Spring 2024 semester. This project is intended to showcase a variety of skills in designing programming systems, implementing frameworks and libraries, and creating a cohesive and useful code from the ground up. 
<br>
<br>
If you like this project, Please click the :star:!
<br>
<br>
A detailed explanation of the code and how to use it is below.

## [Database](https://github.com/Bolton-A/genderSimulation/blob/main/names.zip)

**Database Instructions**
1. Install and set up a [MySQL database](https://dev.mysql.com/downloads/installer/).
2. Connect Python to MySQL database using [MySQL Connector](https://pynative.com/install-mysql-connector-python/). You will need to use the same MySQL host, username, password, and port to connect to it from Python.
3. Insert each .csv file (year1880, year1881, year1882, etc.) into the new MySQL database. You may need to format the columns within the csv file prior to inserting them. This section can be time consuming and repetitve and I highly suggest automating it through a program like AutoHotKey, which will allow you to set up a script to process and insert the files for you. You can learn how to download and install AutoHotKey [here](https://www.autohotkey.com/docs/v2/howto/Install.htm) and you can find the script that I used for this process [here](https://github.com/Bolton-A/genderSimulation/blob/main/MySQLInsertScript.txt). As a note, this script uses screen coordinates that will need to be tweaked to match your own needs.
4. Once this is complete, you should have a MySQL database containing the necessary tables as well as a connection to your Python code.

## [Simulation](https://github.com/Bolton-A/genderSimulation/blob/main/PythonSimulation.py)

![image](https://github.com/Bolton-A/genderSimulation/assets/112293016/64c7fec2-0637-4560-84f2-330a4e5b3faf)



**Simulation Instructions**
1. Download the raw code and open it within your preferred code editor. This code was created and primarily tested within Visual Studio Code.
2. Modify the section that appears below within your code editor to match your own specified host, user, passwd, and port.
```
mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="password",
                passwd="password",
                port=3306
            )
```
3. Use ``` pip install _____``` to add any imports that return an error when attempting to run, replacing the blank with the specified import.
4. Your code should be ready to run! If you run into any errors at this point, please do not hesitate to reach out to me and I will do my best to help with troubleshooting and resolving those issues.


## Samples

- [SampleForbes200.csv](https://github.com/Bolton-A/genderSimulation/blob/main/SampleForbes200.csv): This sample showcases Forbes 200 wealthiest people within the United States and provides a real-world example of a dataset possessing a name category while lacking a gender category. This sample demonstrates the tool's ability to process realistic datasets while preserving data from other categories. This dataset was created by user @AYESSA on Kaggle and can be found [here](https://www.kaggle.com/datasets/ayessa/forbes-top-200-richest-american).
- [SampleNames.csv](https://github.com/Bolton-A/genderSimulation/blob/main/SampleNames.csv): This sample demonstrates the code's ability to process messy datasets that contain multiple categories, duplicate names, nonexistent names, and full names. 

**Simulation Instructions**
1. Download the file that you would like to process. I suggest moving the file to the same folder as your simulation code.
2. Open it through a .csv editor like Excel to ensure that it was downloaded properly and contains the necessary information.
3. Start the simulation tool and provide the file path to the .csv file.
4. The code should walk you through the rest of the setup process and return a file called 'ResultFile' upon completion.

<!-- Note: These links are currently set up with the localhost and is not enabled for outside access. -->
## [Website](http://localhost:3000/)

![image](https://github.com/Bolton-A/genderSimulation/assets/112293016/c9964dc5-cb42-4540-8970-a191d8c51643)

Early in the project's development, I planned on creating a website interface in order to provide the users with a simple graphical interface to process their datasets with. While that is still a feature that I plan to implement in the future, the current iteration of the project has been divided so that the frontend website explains the tool and it's features while the separate tool provides the functionality of the tool. You can find various links to information compiled on the website below.

- [Home](http://localhost:3000/)
- [About](http://localhost:3000/about)
- [Guide](http://localhost:3000/guide)
- [Terms Of Use](http://localhost:3000/termsofuse)
- [Contact](http://localhost:3000/contact)

# Contribute

Contributions are always welcome! Please create a pull request or contact me.

## :pencil: License

This project is licensed under [MIT](https://opensource.org/licenses/MIT) license.

## :man_astronaut: Show your support

Give a ⭐️ if you enjoyed this project!
