# RandomChoicePicker

RandomChoicePicker is a simple Python application that allows you to add options with weights and randomly pick an option based on the weights.

## Requirements

- Python 3.6 or higher
- tkinter
- PyInstaller (for building the executable)

You can install Python from the [official website](https://www.python.org/downloads/). Once Python is installed, you can install tkinter and PyInstaller using pip:

```bash
pip install tkinter pyinstaller
```

## Setting Up a Virtual Environment

Before installing the project dependencies, it's recommended to create a virtual environment. This keeps the dependencies required by different projects separate by creating isolated Python environments for them.

Here's how you can create a virtual environment:

### Mac/Linux

1. Open the Terminal.
2. Navigate to the project directory.
3. Run the following command to create a virtual environment:

   ```bash
   python3 -m venv env
   ```

4. Activate the virtual environment:

   ```bash
   source env/bin/activate
   ```

### Windows

1. Open Command Prompt.
2. Navigate to the project directory.
3. Run the following command to create a virtual environment:

   ```bash
   python -m venv env
   ```

4. Activate the virtual environment:

   ```bash
   .\env\Scripts\activate
   ```

After the virtual environment is activated, you can install the project dependencies with pip:

```bash
pip install tkinter pyinstaller
```

This adds instructions for creating and activating a virtual environment on Mac/Linux and Windows. It also includes the command to install the project dependencies after the virtual environment is activated.

## Build Instructions

To build the executable, navigate to the directory containing the script in the terminal and run the following command:

```bash
pyinstaller --onefile app.py
```

This will create an executable in the `dist` directory.

## Install Instructions

### Mac

1. Open the Terminal.
2. Navigate to the `dist` directory.
3. Run the executable with `./app`.

### Linux

1. Open the Terminal.
2. Navigate to the `dist` directory.
3. Run the executable with `./app`.

### Windows

1. Open Command Prompt.
2. Navigate to the `dist` directory.
3. Run the executable with `app.exe`.

## Usage

After launching the application, you can add options with weights using the "Add Option" button. You can remove options using the "Remove Option" button. To pick an option, click the "Pick Option" button.
