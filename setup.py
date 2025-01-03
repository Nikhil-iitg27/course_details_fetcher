import os
import argparse
from conda_setup import *

def main():
    
    parser = argparse.ArgumentParser(description="Create a conda environment file or install requirements in existing environment.")
    parser.add_argument("--create", action="store_true", help="Install requirements in existing environment.")
    
    args = parser.parse_args()
    path = os.path.join(os.getcwd(), "requirements.txt")
    
    if not args.create:
        install(path)
    else:
        name = input("Enter the name of the environment (default: env):")
        create_env(name, path)

if __name__ == '__main__':
    main()