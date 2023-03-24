# Day 2 - Data Preparation

#Exercise 1 - Create DataFrame
def codice_2_1():
    print('''
    pd.DataFrame(np.random.random((4,4)),columns=list('ABCD'))
    ''')

#Exercise 2 - view content DataFrame    
def codice_2_2():
    print('''
    df.columns[-3:]
    ''')

#Exercise 3 - Rename columns
def codice_2_3():
    print('''
    df_ex_3=df.copy()
    new_col=[]
    for col in range(len(df_ex_3.columns)):
        new_col.append(len(df_ex_3.columns[col]) + col)
    df_ex_3.columns=new_col
    df_ex_3
    ''')

#Exercise 4 - index DataFrame    
def codice_2_4():
    print('''
    df.loc[(df['age']<30)&(df['sex']==2)&(df['marriage']==1)].shape[0]
    ''')
    
def check_2_4(solution):
    try:
        if solution==1180:
            return ("Correct answer!")
        else:
            return ("Retry!")    
    except:
         return ("Retry!")   
    
#Exercise 5 - unique
def codice_2_5():
    print('''
    df.loc[(df['age']>50)&(df['sex']==1)].education.nunique()
    ''')

    
def check_2_5(solution):
    try:
        if solution==6:
            return ("Correct answer!")
        else:
            return ("Retry!")
    except:
         return ("Retry!")   

    
#Exercise 6
def codice_2_6():
    print('''    
df["education"]=df["education"].apply( lambda x: x if ((x>0) and (x<5)) else 0 )
df['education'].value_counts()
''')

# Exercise 7
def codice_2_7():
    print('''
    #7.1
    id_series=pd.Series(np.arange(100))
    age_series=pd.Series(np.random.randint(18,65+1, size=100))
    sex_series=pd.Series(np.random.randint(1,2+1, size=100))
    df_ex_7=pd.DataFrame({ 'id': id_series, 'age': age_series,'sex':sex_series })
    #7.2.1
    print(df_ex_7.loc[42])
    #7.2.2
    print(df_ex_7.loc[42,'sex'])
    #7.2.3
    print(df_ex_7['sex'])
    #7.3
    df_ex_7=df_ex_7.rename({'sex':'gender'},axis=1)
    #7.4
    df_ex_7['salary']=pd.Series(np.random.randint(20000,500000+1,size=100))
    df_ex_7.head()
    ''')
    
#Exercise 8    
def codice_2_8():
    print('''
    student_data=pd.concat([student_data1,student_data2],axis=0).reset_index(drop=True)
    student_data.merge(attendance,how='left',on='student_id').merge(results,how='left',on='exam_id')
    ''')

    
#Exercise 9 - Missing values and duplicates
def codice_2_9():
    print('''
    #9.1
    print(df_titanic['Embarked'].value_counts(dropna=False))
    df_titanic['Embarked']=df_titanic['Embarked'].fillna('missing')
    #9.2
    age_mode=df_titanic['Age'].mode().iloc[0]
    df_titanic['Age']=df_titanic['Age'].fillna(age_mode)
    #9.3
    df_titanic=df_titanic.dropna(subset=["Cabin"])
    df_titanic=df_titanic.drop_duplicates(subset=['Ticket','Cabin'])
    print("How many passenger remain?",df_titanic.shape[0])
    ''')
    
def check_2_9(solution):    
    try:
        if solution==161:
            return ("Correct answer!")
        else:
            return ("Retry!")    
    except:
         return ("Retry!")      
    
    
    
    
    