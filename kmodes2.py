# %%
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from kneed import KneeLocator

var1="Beauty%"
var2="Baby%"

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

dfp = df[[var1, var2]]

ssd = []
ks = range(1,11)
for k in range(1,11):
    km = KMeans(n_clusters=k)
    km = km.fit(dfp)
    ssd.append(km.inertia_)

kneedle = KneeLocator(ks, ssd, S=1.0, curve="convex", direction="decreasing")
kneedle.plot_knee()
plt.show()

k = round(kneedle.knee)
print(f"Number of clusters suggested by knee method: {k}")


kmeans = KMeans(n_clusters=k).fit(df[[var1, var2]])
sns.scatterplot(data=df, x=var1, y=var2, hue=kmeans.labels_)
plt.show()

#%%
cluster0=df[kmeans.labels_==0]
cluster0.describe()

#%%
cluster1=df[kmeans.labels_==1]
cluster1.describe()

#%%
cluster2=df[kmeans.labels_==2]
cluster2.describe()

#%%

# from sklearn.tree import DecisionTreeClassifier, export_text

# tree = DecisionTreeClassifier()
# tree.fit(df[["Age", "Annual_Income_(k$)", "Spending_Score"]], kmeans.labels_)
# print(export_text(tree, feature_names=["Age", "Annual_Income_(k$)", "Spending_Score"]))
# %%
sns.boxplot(data=cluster1[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']]).set(xlabel='Categoria', ylabel='Porcentaje')

# %%
sns.boxplot(data=cluster2[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']]).set(xlabel='Categoria', ylabel='Porcentaje')

# %%
sns.histplot(data=cluster1, x= 'weekday')
# %%
sns.histplot(data=cluster2, x= 'weekday')
# %%
sns.histplot(data=cluster1, x= 'hour')
# %%
sns.histplot(data=cluster2, x= 'hour')
# %%

# %%
