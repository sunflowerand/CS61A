from utils import lower, split, remove_punctuation, lines_from_file
from cats import autocorrect, lines_from_file

abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
print(autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10))