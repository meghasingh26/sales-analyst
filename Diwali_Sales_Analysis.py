import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

#importing file
df = pd.read_csv('C:/Users/ACER/Desktop/Diwali Sales Data.csv', encoding='unicode_escape' )
print(df.head(10))
print(df.shape)

#datacleaning
print("----------------------------data cleaning-------------------------------------")
print(df.describe())
print(df.info())

#removing status and unnmaed1 as they are null
print("--------------------------remove null coloumn axis=1 mean column-----------------------------")
print(df.drop(['Status','unnamed1'],axis=1,inplace=True))
print("-------------------------return no of missing values-----------------------------------")
print(df.isnull().sum())
print('---------------------drop null rows in df-----------------------------')
print(df.dropna(inplace=True))
print('------------------exploratory data analysis-------EDA---------------------')
print(df.columns)
print('==========================================================================================================')
print('----------------------exploratory data analysis------EDA-----------------------')
print('==========================================================================================================')
print('---------------------------gender wise countplot graph--------------------------------')

ax=sns.countplot(x='Gender',data=df,hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)
    sns.set(rc={'figure.figsize':(28,6)})
    plt.show()
print('------------------------------genser wise sales---------------------------')      
gen_wise_sale=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)  
print(gen_wise_sale)
print('--------------------------gen wise sales countplot-------------------------')
sns.barplot(x='Gender',y='Amount',data=gen_wise_sale)
sns.set(rc={'figure.figsize':(28,6)})
plt.show()
print('-------------------------------age wise graph-----------------------------')
ag=sns.countplot(x='Age Group',data=df,hue='Gender')
for bars in ag.containers:
    ag.bar_label(bars)
sns.set(rc={'figure.figsize':(28,6)})
plt.show()
print('---------------------------------------age wise most sales---------------------------------------------')
age_wise_sale=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
print(age_wise_sale)
print('-----------------------------------age wise most sales graph----------------------------------------')
sns.barplot(x='Age Group',y='Amount',data=age_wise_sale)
sns.set(rc={'figure.figsize':(28,6)})
plt.show()
print('--------------------------state wise orders-----------------------------------------------')
state_wise_order=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
print(state_wise_order)
print('--------------------------top 10 state wise orders graph-----------------------------------------------')
sns.barplot(x='State',y='Orders',data=state_wise_order,hue='State')
sns.set(rc={'figure.figsize':(28,6)})
plt.show()
print('------------------------amount wise state sales-------------------------------------------')
amt_wise_sale=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
print(amt_wise_sale)
print('----------------------------amount wise top 10 state sales---------------------------------')
sns.barplot(x='State',y='Amount',data=amt_wise_sale,hue='State')
sns.set(rc={'figure.figsize':(22,8)})
plt.show()
print('-------------------------------marital status wise --------------------------')
# Marital_Status=0
# non-married=1
ms = sns.countplot(data = df, x = 'Marital_Status')
sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
     ms.bar_label(bars)
     xlabel='Marital_Status'
     ylabel='Amount'
     plt.show()
print('-----------------------marital status and gender wise sale-------------------------')
ms_wise_sale=df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
print(ms_wise_sale)
print('-------------------------ms wise sale and non-ms---------------------------------------')
sns.barplot(x='Marital_Status',y='Amount',data=ms_wise_sale,hue='Gender')
sns.set(rc={'figure.figsize':(5,5)})
plt.show()
print('------------------------------most purchases by occupation---------------------------')
co=sns.countplot(x='Occupation',data=df)
for bars in co.containers:
    co.bar_label(bars)
sns.set(rc={'figure.figsize':(28,5)})
plt.show() 
print('---------------------------occupaton wise amount of purchase-------------------------')
occ_wise_sale=df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
print(occ_wise_sale)
print('----------------------------graph of occ_wise_sales-----------------------')
sns.barplot(x='Occupation',y='Amount',data=occ_wise_sale,hue='Occupation')
plt.legend(loc='upper right')
sns.set(rc={'figure.figsize':(28,10)})
plt.show()
print('-------------------------product catagory amount-------------------------------')
pc=sns.countplot(x='Product_Category',data=df,hue='Product_Category')
for bars in co.containers:
    pc.bar_label(bars)
sns.set(rc={'figure.figsize':(28,6)})
plt.show() 
print('-----------------------top 10 most saled product amount------------------------')
product_wise_sale=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
print(product_wise_sale)
print('--------------------------graph of top 10 product saled---------------------------')
sns.barplot(x='Product_Category',y='Amount',data=product_wise_sale,hue='Product_Category')
plt.legend(loc='upper right')
sns.set(rc={'figure.figsize':(28,6)})
plt.show()
print('------------------------------top 10 id has most sales----------------------------------------')
product_id_wise_sale = df.groupby(['Product_ID'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
print(product_id_wise_sale)
print('-----------------------------graph of top 10 id with most sales------------------------------------') 
sns.barplot(data = df, x = 'Product_ID',y= 'Amount')
sns.set(rc={'figure.figsize':(20,5)})
plt.legend(loc='upper right')
xlabel='Product_ID'
ylabel='Amount'
plt.show()
print('=================================================================================================================================')
print('-----------------------------------------------THANK YOU------------------------------------------')