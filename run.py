import yaml
import time
import argparse
from modules import *
from tqdm import tqdm

def main():
    # get configuration
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # argument parser
    parser = argparse.ArgumentParser(description="Create a semester folder structure.")
    parser.add_argument("--sem", default="all", help="Semester numbers (E.G. 1, 2, etc.)")
    parser.add_argument("--branch", default="MC", help="Branch to fetch course details from (E.G. CSE, MC, etc.)")
    parser.add_argument("--create", action="store_true", help = "To create the folder structure or not")
    parser.add_argument("--details", default="print", help="To print the details of the courses or to write them to a file or both")

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
    DETAILS = fetch_courses(config['VARS']['url'], semesters, config['VARS']['format'])

    # print course details found if print is specified
    if DETAILS:
        print("Found all valid courses:")
        for i, det in enumerate(tqdm(DETAILS)):
            time.sleep(0.2)
            print(f"\n\nFor Semester - {semesters[i]} : Found {len(det['courses'])} courses.")
            det_str = get_det_str(det, config['VARS']['format'])
            if args.details == "print" or args.details == "both":
                print(det_str)
            # create folder structure and write details to a file
            if args.create:
                create_folder_structure(config['PATHS'], args.details, det_str, det, semesters[i])

    else:
        print("No content found. Unable to create folder structure.")

    print("Done.")

if __name__ == "__main__":
    main()