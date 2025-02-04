# PassWord-Generator

A secure and user-freidnly password generator application built with Python and Tkinter. This applications allows users to generate a secure, customizable password and copy it to the clipbpard with ease. 

## Features
- Generate passwords with customizable length (1-20 characters)
- Include or exclude character types which are:
   * Lowecase letters (a-z)
   * Uppercase letters (A-Z)
   * Digits (0-9)
   * Symbols (!@#$%^&*, etc.)
- Copy the generated password to the clipboard by clicking the "Copy" button or hovering over the password
- Invalid Input Handling : The application handles invalid inputs and closes after 15 consecutive invalid attempts
- Clean and intuitive graphical user interface (GUI)

## Dependencies 
- Python 3.12
- Tkinter
- secrets module (included in Python Standard Library)

## Installation
- Download the Application:
  * Download the .exe file from the `dist` folder
  * Alternatively, download run the source code directly.
- Run the Application:
   * If using the .exe file, double-click the `PassGen.exe` to launch the application.
   * If using the source code, ensure Python is installed and run the following command:
     ```python PassGen.py```

## Usage 
- Set Password Length:
  * Enter desired password length (between 1 and 20) in the input field.
- Customize Password Composition:
  * Check or uncheck the boxes to include or exclude:
    + Lowercase letters
    + Uppercase letters
    + Digits
    + Symbols
- Generate Password:
  * Click the Generate Password button to create a secure password.
- Copy Password:
  * Click the Copy to Clipboard button to copy the password.
  * Alternatively, hover over the generated password to copy it automatically.
- Invalid Input Handling:
  * If you enter invalid input (e.g., non-numeric characters or a length outside the allowed range), the application will     display an error message.
  * After 15 invalid attempts, the application will close automatically.
 
