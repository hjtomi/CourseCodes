import pandas as pd
import plotly.express as px

pd.options.display.float_format = '{:,.2f}'.format
df_apps = pd.read_csv('apps.csv')
df_apps.sample(5)
del [df_apps['Last_Updated'], df_apps['Android_Ver']]
df_apps['Rating'].isna().values.sum()
df_apps_clean = df_apps.dropna()
df_apps_clean.duplicated()
df_apps_clean = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])
df_apps_clean.sort_values(by='Rating', ascending=False).head()
df_apps_clean.sort_values(by='Size_MBs', ascending=False).head()
df_apps_clean.sort_values(by='Reviews', ascending=False).head(50)
ratings = df_apps_clean['Content_Rating'].value_counts()
fig = px.pie(labels=ratings.index, values=ratings.values)
fig.show()
df_apps_clean[['App', 'Installs']].groupby('Installs').count()
df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
df_apps_clean[['App', 'Installs']].groupby('Installs').count()
df_apps_clean['Price'] = df_apps_clean['Price'].astype(str).str.replace("$", "")
df_apps_clean['Price'] = pd.to_numeric(df_apps_clean['Price'])
df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
df_apps_clean.sort_values(by='Price', ascending=False).head(5)
df_apps_clean['Revenue_Estimate'] = df_apps_clean['Installs'].mul(df_apps_clean['Price'])
df_apps_clean['Category'].nunique()
top10_category = df_apps_clean['Category'].value_counts()[:10]
bar = px.bar(x=top10_category.index, y=top10_category.values)
bar.show()
category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', inplace=True)
h_bar = px.bar(x=category_installs['Installs'], y=category_installs.index, orientation='h', title='Category Popularity')
h_bar.update_layout(xaxis_title='Number of downloads', yaxis_title='Category')
h_bar.show()
cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})
cat_merged_df = pd.merge(cat_number, category_installs, on='Category', how="inner")
cat_merged_df.sort_values('Installs', ascending=False)
scatter = px.scatter(cat_merged_df,  # data
                     x='App',  # column name
                     y='Installs',
                     title='Category Concentration',
                     size='App',
                     hover_name=cat_merged_df.index,
                     color='Installs')

scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
                      yaxis_title="Installs",
                      yaxis=dict(type='log'))

scatter.show()
df_apps_clean['Genres'].nunique()
stack = df_apps_clean['Genres'].str.split(";", expand=True).stack()
num_genres = stack.value_counts()
bar = px.bar(x=num_genres.index[:15], y=num_genres.values[:15], title='Top Genres', hover_name=num_genres.index[:15], color=num_genres.values[:15], color_continuous_scale='Agsunset')
bar.update_layout(xaxis_title='Genre', yaxis_title='Number of Apps', coloraxis_showscale=False)
bar.show()
df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})
df_free_vs_paid.head()
g_bar = px.bar(df_free_vs_paid,
               x='Category',
               y='App',
               title='Free vs Paid Apps by Category',
               color='Type',
               barmode='group')

g_bar.update_layout(xaxis_title='Category',
                    yaxis_title='Number of Apps',
                    xaxis={'categoryorder': 'total descending'},
                    yaxis=dict(type='log'))

g_bar.show()
box = px.box(df_apps_clean,
             y='Installs',
             x='Type',
             color='Type',
             notched=True,
             points='all',
             title='How Many Downloads are Paid Apps Giving Up?')

box.update_layout(yaxis=dict(type='log'))

box.show()
df_paid_apps = df_apps_clean[df_apps_clean['Type'] == 'Paid']
box = px.box(df_paid_apps,
             x='Category',
             y='Revenue_Estimate',
             title='How Much Can Paid Apps Earn?')

box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Ballpark Revenue',
                  xaxis={'categoryorder': 'min ascending'},
                  yaxis=dict(type='log'))

box.show()
df_paid_apps.Price.median()
box = px.box(df_paid_apps,
             x='Category',
             y="Price",
             title='Price per Category')

box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Price',
                  xaxis={'categoryorder': 'max descending'},
                  yaxis=dict(type='log'))

box.show()