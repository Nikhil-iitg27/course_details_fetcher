def get_requirements(filepath):
    
    requirements = []
    with open(filepath) as f:
        
        for line in f:
            
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            package = line.split('==')[0]
            requirements.append(package)
    
    return requirements