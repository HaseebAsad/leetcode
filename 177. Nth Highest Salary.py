import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_vals = employee.sort_values(by = ['salary'], ascending = False)['salary'].unique().tolist()
    column_name = f'getNthHighestSalary({N})'
    if N > 0 and len(unique_vals) >= N:
        result = pd.DataFrame({column_name: [unique_vals[N-1]]})
    else:
        result = pd.DataFrame({column_name: [None]})
    return result
