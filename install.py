import os
import sys
import subprocess

def check_python_version():
    # Check if the Python version is at least 3.6
    if sys.version_info < (3, 6):
        print("Python 3.6 or higher is required. Please upgrade Python.")
        sys.exit(1)

def install_requirements():
    # Install the required packages
    try:
        print("Checking and installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        print("Required packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print("An error occurred while installing the dependencies:", e)
        sys.exit(1)

def create_virtual_environment():
    # Optionally, create a virtual environment for the project
    if not os.path.exists("venv"):
        print("Creating a virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
        print("Virtual environment created.")
    else:
        print("Virtual environment already exists.")

def main():
    check_python_version()   # Ensure Python version is compatible
    create_virtual_environment()  # Create virtual environment if not exists
    install_requirements()   # Install required packages

    print("\nInstallation complete!")
    print("You can now run the main program by executing `python main.py`")

if __name__ == "__main__":
    main()
