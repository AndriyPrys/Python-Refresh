# Day 3 - Exploratory Data Analysis

#Exercise 1 - Sex variable

def codice_3_1():
    print('''

df['sex'].value_counts()

# Version 1 - Function
def get_sex(x):
    if x==1:
        return 'male'
    else:
        return 'female'
df['sex'].apply(lambda x: get_sex(x)).value_counts()

# Version 2 - Dictionary
sex_dict = {1:'male', 2:'female'}
df['sex'].apply(lambda x: sex_dict[x]).value_counts()
''')

#Exercise 2 - Describe

def codice_3_2():
    print('''    
df[['sex','marriage']].describe()

df["marriage"].value_counts(normalize=False)

df["marriage"].value_counts(normalize=True)

''')
    
#Exercise 3 - IQR 
    
def codice_3_3():
    print('''
def IQR(x):
    return x.quantile(0.75) - x.quantile(0.25)
''')
    
def check_3_3(sol):   
    try:
        if sol==13.00:
            return ("Correct answer!")
        else:
            return ("Retry!")    
    except:
         return ("Retry!")      
    
#Exercise 4 - qcut 
    
def codice_3_4():
    print('''
qcut_limit_bal = pd.qcut(df.limit_bal, q=3, labels = ["bronze","silver","gold"])
df['credit_lev'] = qcut_limit_bal
''')  
        
#Exercise 5 - Group & Multi-Index 
    
def codice_3_5():
    print('''
df_ex_5 = df.groupby(['sex','marriage']).agg({'id':'count', 'age':['mean','max'], 'limit_bal':['mean','max']})
df_ex_5
    
new_columns = []
for i,c in df_ex_5.columns:
    new_columns.append(i+'_'+c)
    
df_ex_5.columns = new_columns
df_ex_5
''')  

#Exercise 6 - N Clients by gender 
    
def codice_3_6():
    print('''
    
limit_bal_80 = np.percentile(np_limit_bal, 80)
pay_avg_mean = df[df.limit_bal > limit_bal_80].pay_avg.mean()
age_1q = df.age.quantile(.25)

df_sol = df[(df.limit_bal > limit_bal_80) & (df.pay_avg < pay_avg_mean) & (df.age < age_1q)]

n_male = df_sol.sex.value_counts()['male']
n_female = df_sol.sex.value_counts()['female']    
    
''')  
    
def check_3_6(sol1, sol2):   
    try:
        if (sol1 == 33) & (sol2 == 127):
            return ("Correct answer!")
        else:
            return ("Retry!")    
    except:
         return ("Retry!")   

#Exercise 7 - Titanic 
    
def codice_3_7():
    print('''
    
df_titanic['Age'] = pd.cut(df_titanic['Age'], bins=[0,25,40,100], labels = ["young","middle","senior"])
    
grouped_titanic = df_titanic.groupby(['Age', 'Pclass']).agg({'Survived':['count', 'mean']})
grouped_titanic.columns = grouped_titanic.columns.droplevel(0)
grouped_titanic[grouped_titanic['count'] >= 50].sort_values('mean')

''')  
    
def check_3_7(sol1, sol2):   
    try:
        if (sol1 == ('middle' , '3')) & (sol2 == ('middle', '1')):
            return ("Correct answer!")
        else:
            return ("Retry!")    
    except:
         return ("Retry!")   

#Exercise - SQL 
    
def codice_SQL():
    print('''  
%%sql

SELECT 
        USPS, 
        SUM(AWATER_SQMI) as total_AWATER_SQMI, 
        SUM(ALAND) as total_ALAND, 
        SUM(AWATER) as total_AWATER,
        AVG(INTPTLAT) as avg_LAT,
        AVG(INTPTLONG) as avg_LONG
FROM gaz_tracts 
WHERE USPS LIKE 'A%'
GROUP BY USPS
HAVING total_AWATER_SQMI < 1500;

''') 

   