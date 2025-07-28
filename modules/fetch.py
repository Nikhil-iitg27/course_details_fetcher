import re
import requests
from bs4 import BeautifulSoup

def helper(rows, sem, format):
    
    """
    Helper function to fetch Course details for a given semester.

    Returns:
        dict: Course details for a given semester.
    """
    
    details = {"courses": [], "course_codes": [], "distribution": []}
    found = False
    index = -1  # Initialize index with a default value
    semester = "Semester-" + sem
    
    # Iterate over rows and columns to find the semester
    for row in rows:
        columns = row.find_all("td")
        if(len(columns) < 3): continue

        if not found:
            for col_index, column in enumerate(columns):
                text = ' '.join(column.get_text(strip=True).split())
                if semester in text:
                    index = col_index
                    found = True
                    break
            if not found:  # If semester not found in this row, continue to next row
                continue
        else:
            if index == -1:  # If semester was not found
                continue
                
            # get course names and remove non-breaking space
            text = columns[index].get_text(strip=True).replace('\xa0', ' ')
            text = text.replace('Laboratory', 'Lab')
            # remove newlines, carriage returns and extra spaces
            text = text.replace('\n', ' ').replace('\r', ' ').strip()
            text = re.sub(r'\s+', ' ', text.strip())
            # remove spaces around "-"
            text = re.sub(r'\s*-\s*', '-', text)
            
            # Observing the HTML stucture 
            if not text: break
            if text == "Course Name": continue
            details['courses'].append(text)
            
            # Get the distribution details
            about = dict()
            for i in range(4):
                about[format[i]] = columns[index+i+1].get_text(strip=True).replace('\xa0', ' ')
            
            # Get the course code and update details
            code = columns[index-1].get_text(strip=True).replace('\xa0', ' ')
            details['course_codes'].append(code)
            details['distribution'].append(about)
    
    return details
 
def fetch_courses(URL, semesters, format):
    """
    Fetch course details for the given semesters from the given URL.

    Args:
        URL (str): URL to fetch course names from.
        semesters (list): list of semesters to fetch course details for.
        format (list): format of the distribution details.
        
    Returns:
       list(list): Course details including course name, course code and distribution details.
    """
    
    # Get the HTML content and create soup object
    response = requests.get(URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Get the table and rows
    table = soup.find_all('table')[0]
    rows = table.find_all('tr')
    
    # Fetch details for each semester
    DETAILS = []
    for sem in semesters:
        details = helper(rows, sem, format)
        DETAILS.append(details)
    
    
    return DETAILS