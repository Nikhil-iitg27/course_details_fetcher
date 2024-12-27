import os

def create_folder_structure(sem, course_names):
    
    """
    Creates the folder sub strcutre for the given semesters.

    Args:
        sem (str): Roman numeral format of the semester (E.G. IV, V, etc.)
        course_names (list): Fetched course names for the given semesters.
    """
    
    # Case for all semesters
    if sem == "all":
        for index, _ in enumerate(semesters):
            create_folder_structure(semesters[index], course_names[index])
        return
    
    # Create a single semester folder
    sem_folder = "Semester_" + sem
    os.makedirs(sem_folder, exist_ok=True)
    
    # Create Pre-Mid and Post-Mid folders
    pre_mid_folder = os.path.join(sem_folder, "Pre-Mid")
    post_mid_folder = os.path.join(sem_folder, "Post-Mid")
    os.makedirs(pre_mid_folder, exist_ok=True)
    os.makedirs(post_mid_folder, exist_ok=True)
    
    # Create course folders
    for course_name in course_names:
        os.makedirs(os.path.join(pre_mid_folder, course_name), exist_ok=True)
        os.makedirs(os.path.join(post_mid_folder, course_name), exist_ok=True)

    print(f"Folder structure for {sem} created successfully.")

