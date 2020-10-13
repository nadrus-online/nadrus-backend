from dataclasses import dataclass


@dataclass
class Tutor:
    first_name: str
    last_name: str
    email: str
    phone: str
    subjects: list
    target_ages: list
    target_grades: list
    motivation: str
    sora_tarefeya: str
    picture: str
    zoom_link: str
    notes: str
    experience: str
    group_preferable_size: list
    profile_summary: str
    town: str

    def jsonify(self):
        return vars(self)
