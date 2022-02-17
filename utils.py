import json
from pprint import pprint as pp

def load_candidates():

    with open ('candidates.json', 'r', encoding="utf-8") as file:
        candidates = json.load(file)

    return candidates

def get_candidates_all():
    return load_candidates()

def get_candidate_by_id(vid):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['id'] == vid:
            return candidate
def get_candidates_by_skill(skill):

    candidates = load_candidates()
    skilled_candidates = []
    skill_lower = skill.lower()

    for candidate in candidates:
        candidate_skills = candidate['skills'].lower().split(", ")
        if skill_lower in candidate_skills:
            skilled_candidates.append(candidate)
    return skilled_candidates


def build_performatted_list(candidates):
    page_content = ""

    for candidate in candidates:
        page_content += candidate["name"] + "\n"
        page_content += candidate["position"] + "\n"
        page_content += candidate["skills"] + "\n"
        page_content += "\n"

    return "<pre>" + page_content + "</pre>"