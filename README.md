# Code Sentinel
This is a code vulnerability analysis program capable of finding code injection, XSS and SQL injection vulnerabilities in source code files. It uses Python's re, tkinter, filedialog, simpledialog, ttk, PIL and ThemedStyle libraries to create a graphical interface and allow user interaction.

## Installation
It is not necessary to install any additional packages to run the program, as it only uses standard Python libraries.

The program's executable file can be found in the project's dist folder, inside a subfolder named Sentinel.

## How to use
When opening the program, the user can choose between two options: analyze a file or type a program for analysis.

## Analyze file
If this option is chosen, the program will open a file selection window for the user to choose the file he wants to analyze. The program will then analyze the file and display the result in the main window, listing all the vulnerabilities found in the source code.

## Analyze typed program
If this option is chosen, the user must type the source code he wants to analyze in the text box displayed in the main window. The program will then analyze the source code and display the result in the main window, listing all the vulnerabilities found in the code.

## How it works
The program searches for files with supported extensions in the folder specified in the code, which contains the list of supported extensions (supported_extensions) and the path variable that stores the folder path. Then, for each file found, the program uses the magic library to determine the file type. If the file type is text/, the program uses the bandit tool to detect security vulnerabilities in the code. Otherwise, the program displays a message stating that it is unable to scan the file.

To detect code injection, XSS and SQL injection vulnerabilities, the program uses regular expressions to search for patterns in the source code. The find_code_injection_vulnerabilities() function searches for patterns that can be used to execute arbitrary code, such as the eval(), exec(), os.system() and subprocess.run() functions. The find_xss_vulnerabilities() function looks for patterns that can be used to run malicious scripts in web browsers, such as <script> and <img> tags with src and onerror attributes. The find_sql_injection_vulnerabilities() function searches for patterns that can be used to inject malicious SQL commands into databases, such as SELECT, DROP TABLE and DELETE FROM keywords. All functions return a list of dictionaries with information about the vulnerabilities found, such as the type of vulnerability, the pattern found and the source code line where the vulnerability was detected.

The find_vulnerabilities() function uses these three functions to search for vulnerabilities of all types after searching for vulnerabilities, the find_vulnerabilities() function stores them in a list and returns that list.

The main() function then takes this list of vulnerabilities and displays them on the screen for the user, along with a warning if no vulnerabilities were found or if an error occurred during runtime.

It is important to remember that this is just a simplified example of a security program. In practice, there are many other types of vulnerabilities that can be exploited and many other techniques that can be used to find them. In addition, it is essential to always keep the program up to date and test it frequently to ensure system security.

Finally, it is important to highlight that information security is a critical issue that must be taken seriously by all companies and organizations. Investing in technologies and professionals specialized in security is essential to guarantee the protection of data and confidential information.

## Limitations
The program only supports detection of the vulnerabilities mentioned above and text files. Binary files will not be analyzed.

## Additional notes
The program uses the bandit package to detect vulnerabilities in text files. Make sure bandit is installed on your system before using the program.





