# Day 4 - Data Visualization

# Exercise 1 - Lineplot

def codice_4_1():
    print('''
x = np.linspace(0, 2, 10)

plt.plot(x, x, 'o-', label='linear')
plt.plot(x, x ** 2, 'x-', label='quadratic')
plt.plot(x, x ** 3, 'x-', label='cubic')

plt.legend(loc='best')
plt.title('Linear, Quadratic and Cubic progression')
plt.xlabel('Input')
plt.ylabel('Output')
plt.show()
''')

# Exercise 2 - Scatterplot

def codice_4_2():
    print('''
plt.scatter(df.limit_bal, df.age,
            s=10, alpha = 0.7,
            c=df.age, 
            cmap='viridis'
           )

plt.colorbar()
plt.xlabel('limit_bal')
plt.ylabel('age')
plt.show()
''')

# Exercise 3 - Histogram

def codice_4_3():
    print('''
plt.hist(df.age[df.marriage == 'single'], alpha = 0.3, density = True, bins = 20, label = 'Single')
plt.hist(df.age[df.marriage == 'married'], alpha = 0.3, density = True, bins = 20, label = 'Married')
plt.hist(df.age[df.marriage == 'others'], alpha = 0.3, density = True, bins = 20, label = 'Other')
plt.title("Age Frequency Distribution by Marital Status")
plt.xlabel('Age')
plt.ylabel('Clients')
plt.legend()
plt.show()
''')

# Exercise 4 - Distribution

def codice_4_4():
    print('''
age_single = df.age[df.marriage == 'single']
age_married = df.age[df.marriage == 'married']
age_other = df.age[df.marriage == 'others']

print(df.age.skew(), age_single.skew(), age_married.skew(), age_other.skew())

all_sentence = "The variable Age has a right (or positive) moderately skewed distribution with mean {}, mode {} and median {} years.".format(round(df.age.mean(), 1), df.age.mode()[0], df.age.median())
single_sentence = "Single's Age has a right (or positive) highly skewed distribution with mean {}, mode {} and median {} years.".format(round(age_single.mean(), 1), age_single.mode()[0], age_single.median())
married_sentence = "Married's Age has a symmetrical distribution with mean {}, mode {} and median {} years.".format(round(age_married.mean(), 1), age_married.mode()[0], age_married.median())
other_sentence = "Other's Age has a symmetrical distribution with mean {}, mode {} and median {} years.".format(round(age_other.mean(), 1), age_other.mode()[0], age_other.median())

print(all_sentence + "\\n\\n" + single_sentence + "\\n" + married_sentence + "\\n" + other_sentence) 

''')

# Exercise 5 - Education Levels

def codice_4_5():
    print('''
def education_levels(d):
    if d == 1:
        return 'graduate'
    elif d == 2:
        return 'university'
    elif d == 3:
        return 'high_school'
    else:
        return 'others'
    
df['education'] = [education_levels(i) for i in df['education']]    
    ''')

# Exercise 6 - Barplots

def codice_4_6():
    print('''

# Matplotlib - You have to calculate the number of clients for each education category 

edu_barplot = pd.DataFrame(df.education.value_counts().reset_index()).rename(columns = {'index':'Education', 'education':'Size'})

plt.bar(edu_barplot.Education, edu_barplot.Size, color = sns.color_palette('deep', 4))
plt.xlabel("Education")
plt.ylabel("Number of clients")
plt.show()

# Searbon - Change the estimator of the barplot from np.mean (default) to np.size

sns.barplot(df.education, df.default, ci = None, estimator=np.size)
plt.xlabel("Education")
plt.ylabel("Number of clients")
plt.show()''')
    
# Exercise 7 - Grouped Barplots

def codice_4_7():
    print('''
edu_barplot_grouped = (df.groupby(['education', 'sex']).agg({'default':'mean'})*100).round(1).reset_index()

labels = edu_barplot_grouped.education.unique()
men_means = edu_barplot_grouped.loc[edu_barplot_grouped.sex == 'male', 'default']
women_means = edu_barplot_grouped.loc[edu_barplot_grouped.sex == 'female', 'default']

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Percentage', size = 12)
ax.set_title('Percentage of default clients by Education and Gender', size = 15)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=12)
ax.set_ylim(0,35)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 5),  # 5 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()''')
    
# Exercise 8 - Heatmap

def codice_4_8():
    print('''
f, ax = plt.subplots(figsize=(15, 8)) 
sns.heatmap(corr,
            vmin=-1, vmax = 1,
            cmap=sns.diverging_palette(220, 20, as_cmap=True),
            annot=True, fmt='.2f', annot_kws={"size": 10},
            square=True)
plt.show()
''')

# Exercise 9 - Amazon bestsellers

def codice_4_9():
    print('''
    #9.1
    sns.distplot(df_amazon.Price[df_amazon.Genre == 'Non Fiction'], label='Non Fiction')
    sns.distplot(df_amazon.Price[df_amazon.Genre == 'Fiction'], label='Fiction')
    plt.title("Price Distribution by Genre")
    plt.xlabel('Price')
    plt.ylabel('Books')
    plt.legend()
    plt.show()
    
    #9.2
    plt.title("Reviews trend Year over Year")
    sns.lineplot(data=df_amazon, x="Year", y="Reviews", ci=0, linewidth=3, hue= "Genre")
    
    #9.3
    b=sns.boxplot(x='Year', y='User Rating',data=df_amazon)
    b.tick_params(labelsize=15)
    b.set_xlabel("Year",fontsize=20)
    b.set_ylabel("User Rating",fontsize=20)
    b.set_ylim(3, 5);
    ''')
