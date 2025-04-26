grade_to_mark = {
    'excellent': 5,
    'good': 4,
    'satisfactory': 3,
    'Unsatisfactory (exam retake)': 2,
    'Unsatisfactory (repetition)': 1
}

def get_ects_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 82 <= score <= 89:
        return 'B'
    elif 74 <= score <= 81:
        return 'C'
    elif 64 <= score <= 73:
        return 'D'
    elif 60 <= score <= 63:
        return 'E'
    elif 35 <= score <= 59:
        return 'FX'
    else:
        return 'F'

def get_national_grade(score):
    if 90 <= score <= 100:
        return 'excellent'
    elif 82 <= score <= 89:
        return 'good'
    elif 74 <= score <= 81:
        return 'good'
    elif 64 <= score <= 73:
        return 'satisfactory'
    elif 60 <= score <= 63:
        return 'satisfactory'
    elif 35 <= score <= 59:
        return 'Unsatisfactory (exam retake)'
    else:
        return 'Unsatisfactory (repetition)'
