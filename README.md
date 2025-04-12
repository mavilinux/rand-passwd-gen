# Random Password Generator

**Random Password Generator** is a Python-based GUI application that allows users to generate random, secure passwords. The user can customize the password's complexity (simple or complex) and length (4, 8, or 16 characters). The generated password can be saved to a text file and copied to the clipboard for easy use.

## Features

- **Password Complexity**: 
  - **Simple**: Letters (both uppercase and lowercase) and digits.
  - **Complex**: Letters (both uppercase and lowercase), digits, and punctuation characters.
  
- **Password Length**: 
  - Choose between 4, 8, or 16 characters in length.
  
- **Clipboard Copy**: 
  - Copy the generated password to your clipboard with a click of a button.
  
- **Save to File**: 
  - Save the password, site name, username/email, and the generation date to a text file (`passwords.txt`).

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/mavilinux/rand-passwd-gen.git
   ```

2. **Install dependencies**:
   This project requires the `pyperclip` library for clipboard functionality:
   ```
   pip install pyperclip
   ```

3. **Run the application**:
   After installing the dependencies, run the `rand_passwd_gen.py` script:
   ```
   python rand_passwd_gen.py
   ```

## Usage

1. **Open the application**:
   Run the script, and the GUI window will open.

2. **Generate a Password**:
   - Enter the **site name** and **email/username**.
   - Choose the **password length** (4, 8, or 16) from the combo box.
   - Select **password complexity** (simple or complex).

3. **Save the Password**:
   Click on **Generate and Save Password** to generate and save the password to a text file.

4. **Copy the Password**:
   After generating the password, click **Copy to Clipboard** to copy it to your clipboard.

5. **Exit the Application**:
   Click **Exit** to close the program.

## Example of Output in `passwords.txt`

```
Site Name: Google
Email/Username: user@example.com
Password: hP4r$8kV
Date: 2025-03-18 12:34:56
----------------------------------------
Site Name: Facebook
Email/Username: user@fb.com
Password: nJ5!dA2T
Date: 2025-03-18 12:35:01
----------------------------------------
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
