import yaml
import argparse
from modules import fetch_courses, create_folder_structure
from tqdm import tqdm

def main():
    # get configuration
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # argument parser
    parser = argparse.ArgumentParser(description="Create a semester folder structure.")
    parser.add_argument("--sem", default="all", help="Semester numbers (E.G. 1, 2, etc.)")
    parser.add_argument("--branch", default="MC", help="Branch to fetch course details from (E.G. CSE, MC, etc.)")

    # parse arguments
    args = parser.parse_args()
    config['VARS']['url'] = config['VARS']['url'] + args.branch + ".htm"

    # get semesters in roman
    if args.sem == "all":
        semesters = config['VARS']['semesters']
    else:
        indices = [int(x) - 1 for x in args.sem.split(",")]

        # find the invalid, valid semesters
        invalid_sems = []
        for i in indices:
            if (i > 7 or i < 0):
                invalid_sems.append(str(i+1))
            else:
                config['VARS']['valid_semesters'].append(i)

        # print the invalid semesters
        if invalid_sems:
            print(f"Invalid semester number(s) {','.join(invalid_sems)}.")

        # get the semesters for the vaild indices in roman
        semesters = [config['VARS']['semesters'][i] for i in config['VARS']['valid_semesters']]

    # if all sems are invalid
    if not semesters:
        print("No valid semesters found. Unable to proceed.")
        return

    # fetch courses
    print(f"Fetching course names for {','.join(semesters)} from {config['VARS']['url']}...")
    COURSES, DISTRIBUTION = fetch_courses(config['VARS']['url'], config['VARS']['format'], semesters)

    # print courses found
    if COURSES:
        print("Found all valid courses:")
        for i, courses in enumerate(tqdm(COURSES)):
            print(f"\nFor Semester - {semesters[i]} : Found {len(courses)} courses.")
            
            # create folder structure
            create_folder_structure(config['PATHS'], courses, semesters[i])

    else:
        print("No content found. Unable to create folder structure.")

    print("Done.")

if __name__ == "__main__":
    main()