import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

print(data['EducationField'].value_counts())
grp_by_field = data.groupby("EducationField")

sns.kdeplot(grp_by_field.get_group('Medical')['MonthlyRate'], label='Medical')
sns.kdeplot(grp_by_field.get_group('Marketing')
            ['MonthlyRate'], label='Marketing')
plt.legend()
plt.show()
