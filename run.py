import argparse
from modules import *

def main():
    URL = "https://www.iitg.ac.in/acad/CourseStructure/Btech2018/"
    SEMESTERS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
    parser = argparse.ArgumentParser(description="Create a semester folder structure.")
    parser.add_argument("--sem", default="all", help="Semester numbers (E.G. 1, 2, etc.)")
    parser.add_argument("--branch", default="MC", help="Branch to fetch course details from (E.G. CSE, MC, etc.)")
    
    args = parser.parse_args()
    URL = URL + args.branch + ".htm"
    
    if args.sem == "all":
        semesters = SEMESTERS
    else:
        indices = [int(x) - 1 for x in args.sem.split(",")]
        semesters = [SEMESTERS[i] for i in indices]
    
    print(f"Fetching course names for {','.join(semesters)} from {URL}...")
    COURSES = fetch_courses(URL, semesters)
    
    if COURSES:
        print(f"Found courses:")
        for i, courses in enumerate(COURSES):
            print("Semester -", semesters[i], ":")
            for course in courses:
                print(f" - {course}")

    #     create_folder_structure(courses, semesters)
    # else:
    #     print("No content found. Unable to create folder structure.")
    
    # print("Done.")

if __name__ == "__main__":
    main()