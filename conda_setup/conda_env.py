import os
import argparse
from .conda_requirements import get_requirements

def create_env(name, filepath):
    
    requirements = get_requirements(filepath)
    os.system(f"conda create -n {name} -y {' '.join(requirements)}")
    print(f"-Environment {name} created successfully, activate to continue.")