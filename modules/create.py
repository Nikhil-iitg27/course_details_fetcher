import os
import time

def create_folder_structure(dir, courses, sem):
    
    # Create a single semester folder
    semester = "Semester_" + sem
    sem_folder = os.path.join(dir['base_dir'], semester)
    os.makedirs(sem_folder, exist_ok=True)
    
    # Create Pre-Mid and Post-Mid folders
    pre_mid_folder = os.path.join(sem_folder, "Pre-Mid")
    post_mid_folder = os.path.join(sem_folder, "Post-Mid")
    os.makedirs(pre_mid_folder, exist_ok=True)
    os.makedirs(post_mid_folder, exist_ok=True)
    
    # Create course folders
    for course in courses:
        os.makedirs(os.path.join(pre_mid_folder, course), exist_ok=True)
        os.makedirs(os.path.join(post_mid_folder, course), exist_ok=True)

    print(f"Folder structure for {sem} created successfully.")
    time.sleep(0.2)

