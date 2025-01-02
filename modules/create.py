import os
import time

def create_folder_structure(dir, courses, sem):
    """creates the folder substructure for a particular semester

    Args:
        dir (str): directory where the folder structure is to be created
        courses (list(str)): _description_
        sem (_type_): _description_
    """
    # Create a single semester folder
    semester = "Semester_" + sem
    sem_folder = os.path.join(dir['base_dir'], semester)
    os.makedirs(sem_folder, exist_ok=True)
    
    # Create course folders
    for course in courses:
        course_folder = os.path.join(sem_folder, course)
        os.makedirs(course_folder, exist_ok=True)
        os.makedirs(course_folder, exist_ok=True)
        # Create Pre-Mid and Post-Mid folders
        pre_mid_folder = os.path.join(course_folder, "Pre-Mid")
        post_mid_folder = os.path.join(course_folder, "Post-Mid")
        os.makedirs(pre_mid_folder, exist_ok=True)
        os.makedirs(post_mid_folder, exist_ok=True)
    
    print(f"Folder structure for {sem} created successfully.")