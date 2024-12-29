import os
import yaml
from .conda_requirements import get_requirements

def install(filepath):
    
    requirements = get_requirements(filepath)
    
    try:
        os.system(f"conda install {' '.join(requirements)} -y")
    except:
        for package in requirements:
            try:
                os.system(f"conda install -y {package}")
            except:
                print(f"Failed to install {package}, try with pip.")