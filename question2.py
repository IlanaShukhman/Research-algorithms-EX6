import pandas as pd

'''
In this question I was uncertain about the הוצאות / הכנסות and how to get the budget.
I saw that "Income" (-) was significantly lower than "Expenses" (+), 
and so I went with that if the expenses of an office were a certain number, the budget must be higher.
'''
data = pd.read_csv("national-budget.csv")


def education_budget(year: int) -> int:
    df = data[(data['שם רמה 2'] == 'חינוך') & (data['שנה'] == year) & (data['הוצאה נטו'] > 0)]
    Total = df['הוצאה נטו'].sum()
    return Total


def security_budget_ratio(year: int) -> float:
    res_df = data[(data['שנה'] == year) & (data['הוצאה נטו'] > 0)]
    total = res_df['הוצאה נטו'].sum()

    df = data[(data['שם סעיף'] == 'משרד הבטחון') & (data['שנה'] == year) & (data['הוצאה נטו'] > 0)]

    security_total = df['הוצאה נטו'].sum()
    return (security_total / total) * 100


def largest_budget_year(office: str) -> int:
    max_budget = 0
    max_year = 0
    for year in range(1997, 2022):
        df = data[(data['שם סעיף'] == office) & (data['שנה'] == year) & (data['הוצאה נטו'] > 0)]
        if df['הוצאה נטו'].sum() > max_budget:
            max_budget = df['הוצאה נטו'].sum()
            max_year = year
    return max_year


'''
This function returns how much the budget of an office grew from previous year.
'''


def growth_of_budget(office: str, year: int) -> int:
    df = data[(data['שם סעיף'] == office) & (data['שנה'] == year) & (data['הוצאה נטו'] > 0)]
    budget_this_year = df['הוצאה נטו'].sum()
    df = data[(data['שם סעיף'] == office) & (data['שנה'] == year - 1) & (data['הוצאה נטו'] > 0)]
    budget_last_year = df['הוצאה נטו'].sum()
    return budget_this_year - budget_last_year


if __name__ == '__main__':
    print(education_budget(2015))
    print(security_budget_ratio(2015))
    print(largest_budget_year('משטרה ובתי סוהר'))
    print(growth_of_budget('משרד הבטחון', 2015))
