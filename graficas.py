# %%
import pandas as pd
import numpy as np
import seaborn as sns

# %%
df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")
df.info()

# %%
#type(df[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']])
type(df)
# %%
areas= df[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']]
sns.boxplot(data=areas)
# %%
sns.histplot(data=df, x= 'weekday')

# %%
sns.histplot(data=df, x= 'hour')
# %%
sns.histplot(data=df, x="weekday", y="Food%")

#%%
df.query('weekday==1')[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']]


# %%
sns.boxplot(data=df.query('weekday==1')[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']]).set(xlabel='Categoria', ylabel='Porcentaje', title='Lunes')
# %%
sns.boxplot(data=df.query('weekday==5')[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']]).set(xlabel='Categoria', ylabel='Porcentaje', title='Viernes')
# %%
sns.boxplot(data=df.query('weekday==7')[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']]).set(xlabel='Categoria', ylabel='Porcentaje', title='Domingo')
# %%
sns.boxplot(data=df.query('weekday==2')[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']]).set(xlabel='Categoria', ylabel='Porcentaje', title='Martes')
# %%
sns.boxplot(data=df.query('weekday==3')[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']]).set(xlabel='Categoria', ylabel='Porcentaje', title='Miercoles')
# %%
sns.boxplot(data=df.query('weekday==4')[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']]).set(xlabel='Categoria', ylabel='Porcentaje', title='Jueves')
# %%
sns.boxplot(data=df.query('weekday==6')[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']]).set(xlabel='Categoria', ylabel='Porcentaje', title='Sabado')
# %%
sns.scatterplot(data=df, x='Food%', y='discount%', hue='weekday')
# %%
sns.heatmap(data=df.corr())
# %%

# %%
horarios= df.pivot("hour", "weekday")
sns.heatmap(data=horarios)
# %%
