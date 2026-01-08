
'''
Amac dataframedeki en yuksek ikinci maasi bulmak
temel akis
degerleri al
tekrarlananlari kaldir
azalan sekilde sırala
2. deger varsa degeri yaz, yoksa null yaz
'''
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries=employee['salary'].drop_duplicates().sort_values(ascending=False)
    # drop_duplicates() - tekrar edenleri cikarmak icin
    # ascending=False - buyukten kucuge siralamak icin
    
    if len(unique_salaries)< 2:
        return pd.DataFrame({'Second Highest Salary': [None]})
    
    return pd.DataFrame({'Second Highest Salary': [unique_salaries.iloc[1]]})
# iloc[1] - 2. degeri almak icin 

employee = pd.DataFrame({
    'id': [1,2,3,4,5,6,7,8],
    'salary': [100,200,300,456,8000,875,132,45]
})

result=second_highest_salary(employee)
print(result)

