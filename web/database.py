import pandas as pd

df = pd.read_csv("web/data.csv")
df0 = df.sort_values(by='date', ascending=False)
df1 = df[df['cluster']==0]
df2 = df[df['cluster']==1]
df3 = df[df['cluster']==2]
df4 = df[df['cluster']==3]

newslist0 = []
newslist1 = []
newslist2 = []
newslist3 = []
newslist4 = []

for i in range(len(df0)):
    newslist0.append(df0.iloc[i].tolist())
    
for i in range(len(df1)):
    newslist1.append(df1.iloc[i].tolist())
    
for i in range(len(df2)):
    newslist2.append(df2.iloc[i].tolist())
    
for i in range(len(df3)):
    newslist3.append(df3.iloc[i].tolist())
    
for i in range(len(df4)):
    newslist4.append(df4.iloc[i].tolist())

index_show = 0
    