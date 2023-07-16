# Code Sentinel
![Demonstration](./layout/img/the-sentinel.jpg)<br><br>
Code Sentinel is a Python application that analyzes code files for vulnerabilities. It helps identify potential security issues such as code injection, cross-site scripting (XSS), SQL injection, CSRF (Cross-Site Request Forgery), and SSRF (Server-Side Request Forgery).

## Features
- Supports various programming languages including Python, Java, JavaScript, C, C++, Ruby, HTML, and PHP.
- Analyzes code files for vulnerabilities.
- Displays vulnerability details including type, pattern, and line number.
- Provides a user-friendly graphical interface for file selection and displaying results.

## Installation
To use Code Sentinel, follow the steps below:

1. Clone the repository:
```
git clone https://github.com/Sentinel-vulnerability/Code-Sentinel.git
```
2. Install the required dependencies:

start ./code_sentinel.sh and authorize the installation of dependencies

```
pip install re
pip install tkinter
pip install Pillow
pip install ttkthemes
pip install atheris
```
## Usage
To run Code Sentinel, execute the following command:
```
./code_sentinel.sh or python3 sentinel.py
```
The Code Sentinel window will appear, allowing you to perform the following actions:
- Click the "Anexar Arquivo" (Attach File) button to select a code file for analysis.
- Once the file is selected, Code Sentinel will analyze it for vulnerabilities.
- If vulnerabilities are found, they will be displayed in the application window, showing the type, pattern, and line number of each vulnerability.
- If no vulnerabilities are found, a message indicating this will be displayed.

Please note that Code Sentinel supports the following file extensions: `.py`, `.java`, `.js`, `.c`, `.cpp`, `.html`, and `.php`.

## Vulnerability Detection
Code Sentinel detects the following types of vulnerabilities:
- Code Injection: It searches for patterns such as eval(, exec(, os.system(, subprocess.run(, $(, and `.*` in the code.
- XSS (Cross-Site Scripting): It looks for patterns like <script>...</script> and <img...src=...onerror=...>.
- SQL Injection: It identifies patterns such as SELECT *, DROP TABLE, and DELETE FROM in the code (case-insensitive).
- CSRF (Cross-Site Request Forgery). 
- SSRF (Server-Side Request Forgery).

Please note that the CSRF and SSRF vulnerability detections are not yet implemented in the current version of Code Sentinel.

## Contributions
Contributions to Code Sentinel are welcome! If you would like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Develop and test your changes.
4. Commit your changes and push them to your fork.
5. Submit a pull request explaining your changes.

Also, if you want to be part of the project and organization, please contact me: ``` pedro.lima1979@hotmail.com```

## License
Please read the project license [Link](https://github.com/Sentinel-vulnerability/.github/blob/main/LICENSE.md).

