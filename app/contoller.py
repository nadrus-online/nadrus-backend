import re

from app import app
from entities.tutor import Tutor
from googleapi.googleapi import GoogleApi

config = app.config['config']
logger = config.get_logger()

all_subjects = [
    {'name': 'رياضيات', 'id': 1},
    {'name': 'فيزياء', 'id': 2},
    {'name': 'لغة عبريّة', 'id': 3},
    {'name': 'لغة عربيّة', 'id': 4},
    {'name': 'لغة انجليزيّة', 'id': 5},
    {'name': 'دين اسلامي', 'id': 6},
    {'name': 'بسيخومتري', 'id': 7},
    {'name': 'مدنيات', 'id': 8},
    {'name': 'علوم حاسوب', 'id': 9},
    {'name': 'الكترونيكا', 'id': 10},
    {'name': 'كيمياء', 'id': 11},
    {'name': 'بيولوجيا', 'id': 12},
    {'name': 'إعلام', 'id': 13},
    {'name': 'تاريخ والكتابة الابداعية والنقد والادب', 'id': 14},
]


def get_tutors() -> list:
    """Returns a list of objects holding all tutors.
    Note: If the Google form changes, the existing rows WILL NOT be updated, so their row (represented by a list) will
    have less elements. In order to have a list with a fixed size, we pad such results with the empty string.

    :return: List of tutors.
    """
    sample_spreadsheet_id = config.MENTORS_SHEET_ID
    sample_range_name = 'A:Q'
    # used for padding missing columns
    cols = re.search('([A-Z]):([A-Z])', sample_range_name)
    rows_count = ord(cols[2]) - ord(cols[1]) + 1

    service = GoogleApi.get_service()
    result = service.spreadsheets().values().get(spreadsheetId=sample_spreadsheet_id,
                                                 range=sample_range_name).execute()
    values = result.get('values', [])
    if not values:
        logger.info('got an empty list of rows for document %s', config.MENTORS_SHEET_ID)
        return []
    # remove header column
    values.pop(0)
    values = list(map(lambda v: v if len(v) == rows_count else v + [''] * (rows_count - len(v)), values))
    return [Tutor(value[1], value[2], value[3], "+972" + str(value[4])[1:], _get_id_to_subject_list(value[5]),
                  value[6].split(','), value[7].split(','), value[8], value[9], value[10], value[11], value[12],
                  value[13].split(','), value[14], value[15], value[16])
            for value in values]


def get_subjects() -> list:
    """Urgh... did you really expect to see documentation here?
    """
    return all_subjects


def _get_id_to_subject_list(subjects) -> list:
    """Returns a list of objects. Each object has subject's name, mapped by its ID.

    :param subjects: List of subjects (each is a coma-separated string).
    :return: List of dictionaries {id -> name}.
    """
    try:
        return [next(item for item in all_subjects if item['name'] == subject.strip())
                for subject in subjects.split(',')]
    except StopIteration as si:
        logger.error("couldn't generate subjects dict", si)
        return []
