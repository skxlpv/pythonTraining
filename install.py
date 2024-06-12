import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# List of modules to install
modules_to_install = ["requests"]


def main():
    for module in modules_to_install:
        print(f"Installing {module}...")
        install(module)
        print(f"{module} installed successfully.")


if __name__ == "__main__":
    main()
