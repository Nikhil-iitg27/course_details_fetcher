def get_det_str(det, format):
    details_str = "\n"
    for i in range(len(det['courses'])):
        code = det['course_codes'][i]
        name = det['courses'][i]
        spaces = int((60 - len(name))/2)*" "
        left_space = (len(name)%2)*" "
        dist = ' '.join((det['distribution'][i][tag] + " ") for tag in format)
        details_str += code + left_space + spaces + name + spaces + dist + "\n"
    
    return details_str