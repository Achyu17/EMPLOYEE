import pandas  as pd
df=pd.read_excel("empl.xlsx")
print(df)
#to print first and last rows
print(df.head())
print(df.tail())
#to find the employees who joined after 2000
print(df.loc[df['Year of Joining'] > 2000])
#to find the employees who draws salary more than 1lakhs
print(df.loc[df['Salary']>100000])
#to find the employees who are from mid east region
print(df.loc[df['Region']=="Mideast"])
#to find the employees their first name ,email,date of joining,salary
print(df[['First Name','E Mail','Date of Joining','Salary']])
#to sort employee name according to salary
print(" ***Sorting by Name Salary")
print(df.sort_values(["Salary","First Name"]))
#to sort employees name according to his age
print(df.sort_values(["Age in Yrs.","First Name"]))
#to print female and male employee details
print(df.loc[df['Gender'] =='F'])
print(df.loc[df['Gender']=='M'])




