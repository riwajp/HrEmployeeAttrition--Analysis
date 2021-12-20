import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
# print(data.dtypes)


def attrition_by_gender():
    dsf = {'gender': ['Female', 'Male']}
    percents = [0, 0]
    grp_by_gender = data.groupby('Gender')
    for gender in grp_by_gender.groups:
        print(gender)
        left = grp_by_gender.get_group(
            gender)['Attrition'].value_counts()['Yes']
        total = len(grp_by_gender.get_group(gender)['Attrition'])
        left_percent = left/total * 100
        if gender == 'Male':
            percents[1] = left_percent
        else:
            percents[0] = left_percent
        dsf['left_percent'] = percents
    sns.barplot(x="gender", y='left_percent', data=dsf)
    plt.show()


# attrition_by_gender()
# male little more likely to leave


def attrition_by_x(x):
    grp_by_x = data.groupby(x)
    df = {}
    years_list = []
    attrition_rate = []
    genders = []
    for years, items in grp_by_x:
        grp_by_gender = items.groupby('Gender')
        for gender, items in grp_by_gender:
            years_list.append(years)

            genders.append(gender)

            try:
                left = items['Attrition'].value_counts()['Yes']
            except:
                left = 0
            total = len(items['Attrition'])
            percent = left/total * 100
            attrition_rate.append(percent)
    df['years'] = years_list
    df['attrition_rate'] = attrition_rate
    df['gender'] = genders
    print(df)

    sns.lineplot(x="years", y='attrition_rate', data=df, hue='gender')
    plt.show()


# attrition_by_x('TotalWorkingYears')
