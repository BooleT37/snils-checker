import pandas as pd
from snils_checker import check_snils, normalize_snils

check_snils(normalize_snils(8002678034))

# df = pd.read_csv('in.csv', ';')
# df["is_valid"] = df["snils"]\
#     .map(normalize_snils)\
#     .map(check_snils)
# df