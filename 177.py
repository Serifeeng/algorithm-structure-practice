''' 
176. soru ile ayni mantikta
Sadece bu soruda N degeri var
Siralanan degerler arasindan n ninci deger yazilir
'''
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_df=employee['salary'].drop_duplicates().sort_values(ascending=False)

    if len(unique_df)< N:
        return pd.DataFrame({"dd":[None]})
    return pd.DataFrame({'NthHighestSalary':[unique_df.iloc[N-1]]})


employee = pd.DataFrame({
    'id': [1,2,3,4,5,6,7],
    'salary': [234,543,765,12,3,432,567]
})

print(nth_highest_salary(employee, 3))
