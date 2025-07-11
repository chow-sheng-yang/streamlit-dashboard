import json

with open('track_requirements.json') as f:
    track_requirements = json.load(f)

#######################
# Helper Functions

def get_grade_mapping():
    grade_point_mapping = {
            "A+" : 5,
            "A" : 5,
            "A-" : 4.5,
            "B+" : 4,
            "B" : 3.5,
            "B-" : 3,
            "C+" : 2.5,
            "C" : 2,
            "D+" : 1.5,
            "D" : 1,
            "F" : 0
        }
    return grade_point_mapping

def grade_point_mapper(grade):
    grade_mapping = get_grade_mapping()
    if grade in grade_mapping.keys():
        return grade_mapping[grade]
    return None
    
def get_track_requirements(track:str, type=None):
    if track.startswith('MINOR-'):
        return 20
    elif track.startswith('MAJOR-'):
        return 40
    else:
        return track_requirements[track][type]