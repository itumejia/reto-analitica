# %%
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from kneed import KneeLocator

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

dfp = df[["total_items", "weekday"]]

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

#%%
kmeans = KMeans(n_clusters=k).fit(df[["total_items", "weekday"]])
sns.scatterplot(data=df, x="weekday", y="total_items", hue=kmeans.labels_)
plt.show()

#%%

# from sklearn.tree import DecisionTreeClassifier, export_text

# tree = DecisionTreeClassifier()
# tree.fit(df[["Age", "Annual_Income_(k$)", "Spending_Score"]], kmeans.labels_)
# print(export_text(tree, feature_names=["Age", "Annual_Income_(k$)", "Spending_Score"]))