# Introduction
This is a prototype authentication process for user using facial recognition.
The API used is from [face_recognition](https://github.com/ageitgey/face_recognition)

## How it works
The database should contain 1 image of each person that you want to identify. The name of each image file should be the name of the person you want to identify.

Enter the path to the input image, and run the script.

## Requirements
1. Python 3.10.12
2. 'Follow the instructions from [here](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf) to install dlib on MacOS or Ubuntu
3. Make sure you have `cmake` installed. If not do `brew install cmake`
4. Install the module using `pip install face_recognition`
   
## Instructions for use
1. clone this repository
2. do `pip install -r requirements.txt`
3. create a `database` directory and upload images of all significant persons into the directory. The name of the image should be the name of the person you want to identify
4. create a `user_inputs` directory and upload the test image into the directory
5. fill in the respective user input image and database directory paths in the script
6. run the program
