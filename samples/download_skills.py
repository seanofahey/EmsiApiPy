import EmsiApiPy
import pandas as pd

# create the connection
conn = EmsiApiPy.SkillsClassificationConnection()

# download all the skills
data = conn.get_list_all_skills()

# load into pandas
df = pd.DataFrame(data['data'])

# export
writer = df.to_csv("skills_list.csv", index = False)
