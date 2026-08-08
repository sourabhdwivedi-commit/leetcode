import pandas as pd
emp={
    "name":['sahil','aniket'],
    "salary":[12000,45000],
    "department":['IT','manager']
}

mep_data=pd.DataFrame(emp)

print("\n")
print(mep_data[mep_data['salary']>10000])