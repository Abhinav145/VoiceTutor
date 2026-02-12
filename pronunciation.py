import difflib

def pronunciation_score(expected, spoken):
    ratio = difflib.SequenceMatcher(None, expected.lower(), spoken.lower()).ratio()
    score = round(ratio * 100, 2)
    return score
