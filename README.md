# Password Generator
Welcome to the "Password Generator" repository, a Python-based tool that generates secure passwords. This generator offers two modes for password creation: one that produces 5 letters followed by 5 digits, and another that alternates between letters and digits.


## Program Instructions
- Objective: Generate secure passwords based on user preferences.
- How to Use: Run the program and follow the prompt. Enter 'A' to generate a password with 5 random letters followed by 5 digits.
  Enter 'B' to generate a password that alternates between letters and digits. The program will display the generated password.
  If an invalid option is chosen, the program will provide an error message.
- Password Options: Option A: 5 letters and 5 digits (e.g., `abcde12345`). Option B: Alternating letters and digits (e.g., `a1b2c3d4e5`).


## Implementation Details
- The password generator is implemented in Python.
- Random letters are chosen from the full English alphabet (both uppercase and lowercase).
- The program uses Python’s `random` module to generate both letters and digits.
- User input is validated to ensure it matches the expected format ('A' or 'B').


## How to Run
- Clone the Repository:
  ``` bash
      git clone https://github.com/ChristosGkovaris/Password-Generator.git
      cd Password-Generator
- Ensure you have Python installed: Every Python version.
- Run the Program: **python password.py** / **python password_v2.py**
