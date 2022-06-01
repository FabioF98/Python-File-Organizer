# File Organizer with Image Analysis

This python script was created as a project for the Python Programming section of the Data Science course of Start2Impact, an italian startup (B Corp certified) which has been selected among the best ones in Europe in terms of education and social impact by the European Social Innovation Competition.

The goal of the project was to create a python script in order to handle different types of files based on their extensions.

## First Step

The starting point for this program was a folder containing : 
* 2 text files (.txt & .odt)
* 2 audio files (.mp3)
* 4 images (.png, .jpg & .jpeg)

After locating the correct folder, the program loops alphabetically over every files and creates new subfolders based on the data types of the file inside the main folder, for example in this case we have a text folder, an audio folder and an image folder, where each of the files will be placed based on their extension. As it moves the files the program also prints information regarding each one of them, in particular :
* File name
* File type
* File dimension (in bytes)

While doing this the script also creates a new file called *recap.csv* which contains information regarding every file, regardless of its extension. One specific request for this task was that the program needed to check whether the subfolders already existed and if the recap.csv file already containted some information, if that was the case the script updates the recap.csv file instead of overwriting it, so not to lose all previous data.ù

## Second Step
The file **addfile.py** is a python script intended to be used from the Command Line Interface. The goal of this file was to move a *single file*, positioned inside the *files* folder, to its correct folder (based on the type), updating the recap.csv file. The interface of the program has as its unique argument the file name, in case the name of the file doesn't exist the program will communicate it with a dedicated error message. 

## Third Step
The script has to iterate over each image inside the image folder in order to create a table with the following information :
* Height of the image (in pixel)
* Width of the image (in pixel)
* If the image is grayscale, the *grayscale* column must indicate the value of the color level
* If the image is RGB or RGBA, specific columns must indicate the value of each color level





