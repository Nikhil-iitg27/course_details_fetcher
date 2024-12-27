import re
import requests
from bs4 import BeautifulSoup

def helper(rows, sem):
    
    """
    Helper function to fetch course names for the given semester.

    Returns:
        list: course names for the given semester.
    """
    
    courses = []
    found = False
    semester = "Semester-" + sem
    
    # Iterate over rows and columns to find the semester
    for row in rows:
        columns = row.find_all("td")
        if(len(columns) < 3): continue

        if not found:
            for col_index, column in enumerate(columns):
                text = ' '.join(column.get_text(strip=True).split())
                if semester in text:
                    index = (col_index)
                    found = True
                    break
        else:
            # get course names and remove non-breaking space
            text = columns[index].get_text(strip=True).replace('\xa0', ' ')
            # remove newlines, carriage returns and extra spaces
            text = text.replace('\n', ' ').replace('\r', ' ').strip()
            text = re.sub(r'\s+', ' ', text.strip())
            # remove spaces around "-"
            text = re.sub(r'\s*-\s*', '-', text)
            
            # Observing the HTML stucture 
            if not text: break
            if text == "Course Name": continue
            text = text.replace('Laboratory', 'Lab')
            courses.append(text)
    
    return courses
 
def fetch_courses(URL, semesters):
    """
    Fetch course names for the given semesters from the given URL.

    Args:
        URL (str): URL to fetch course names from.
        semesters (list): list of semesters to fetch course names for.

    Returns:
        list(list): list of list of course names for the given semesters.
    """
    
    # Get the HTML content and create soup object
    response = requests.get(URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Get the table and rows
    table = soup.find_all('table')[0]
    rows = table.find_all('tr')
    
    # Deal with the default case
    COURSES = []
    if semesters == "all":
        COURSES = fetch_courses(URL, ' '.join(semesters))
    
    for _, sem in enumerate(semesters):
        COURSES.append(helper(rows, sem))
    
    return COURSES