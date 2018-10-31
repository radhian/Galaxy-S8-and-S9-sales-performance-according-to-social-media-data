########################################################################################################################
## Name of Project : Samsung Galaxy sales analysis                                                                    ##
## File Name       : Sales_SocialMedia_Relation.py                                                                    ##
## Author          : Radhian Ferel Armansyah                                                                          ##
## Date            : 26th October 2018                                                                                ##
## Description     : This project evaluates how the social media data can be leveraged to analyze the sales           ##
##                   performance of galaxy s8 and s9. In order to narrow down the project outcome, we are going to    ##
##                   predict the sales numbers for both mobile phone based on the trends on youtube search and web    ##
##                   search(google search). The sales data is elaborated from several news/snapshots,                 ##
##                   while the social media data is retrieved from google trends                                      ##
########################################################################################################################




import statsmodels.api as sm
import pandas as pd
from pandas import DataFrame


DataSets = pd.ExcelFile(r'C:\Users\Radhian Ferel\Documents\Business Intelligent samsung\data analytics, galaxy s8 s9.xlsx')


###########################################      Galaxy s8/s8+ Analysis    ###########################################

## Read data from microsoft excel
galaxy_s8 = pd.read_excel(DataSets, 'galaxy s8')

## assign sales data
df_sales_s8 = DataFrame(galaxy_s8,columns=['Sales (in Million of Units)'])

## assign youtube search data
df_youtube_s8 = DataFrame(galaxy_s8,columns=['youtube search'])

## assign Web search data
df_web_s8 = DataFrame(galaxy_s8,columns=['Web search'])

##  assign Google Shopping data
df_GoogleShop_s8 = DataFrame(galaxy_s8,columns=['Google Shopping'])


## youtube search and sales performance relationship model
YS_sales_relation_s8 = sm.OLS(df_sales_s8,df_youtube_s8)
results_YS_s8 = YS_sales_relation_s8.fit()

## web search and sales performance relationship model
WS_sales_relation_s8 = sm.OLS(df_sales_s8,df_web_s8)
results_WS_s8 = WS_sales_relation_s8.fit()

## google shopping and sales performance relationship model
GS_sales_relation_s8 = sm.OLS(df_sales_s8,df_GoogleShop_s8)
results_GS_s8 = GS_sales_relation_s8.fit()



##########################################      Galaxy s9/s9+ Analysis    ##########################################

## Read data from microsoft excel
galaxy_s9 = pd.read_excel(DataSets, 'galaxy s9')

## assign sales data
df_sales_s9 = DataFrame(galaxy_s9,columns=['Sales (in Million of Units)'])

## assign youtube search data
df_youtube_s9 = DataFrame(galaxy_s9,columns=['youtube search'])

## assign Web search data
df_web_s9 = DataFrame(galaxy_s9,columns=['Web search'])

##  assign Google Shopping data
df_GoogleShop_s9 = DataFrame(galaxy_s9,columns=['Google Shopping'])


## youtube search and sales performance relationship model
YS_sales_relation_s9 = sm.OLS(df_sales_s9,df_youtube_s9)
results_YS_s9 = YS_sales_relation_s9.fit()

## web search and sales performance relationship model
WS_sales_relation_s9 = sm.OLS(df_sales_s9,df_web_s9)
results_WS_s9 = WS_sales_relation_s9.fit()

## google shopping and sales performance relationship model
GS_sales_relation_s9 = sm.OLS(df_sales_s9,df_GoogleShop_s9)
results_GS_s9 = GS_sales_relation_s9.fit()




#############################################      Print Result Summary    #############################################

## Print Result summary (Galaxy S8)
print('------------------------------------- Result galaxy s8(Youtube Search)  -------------------------------------')
print(results_YS_s8.summary())
print('------------------------------------- Result galaxy s8(Web Search)  -------------------------------------')
print(results_WS_s8.summary())
print('------------------------------------- Result galaxy s8(Google Shopping)  -------------------------------------')
print(results_GS_s8.summary())


## Print Result summary (Galaxy S9)
print('------------------------------------- Result galaxy s9(Youtube Search)  -------------------------------------')
print(results_YS_s9.summary())
print('------------------------------------- Result galaxy s9(Web Search)  -------------------------------------')
print(results_WS_s9.summary())
print('------------------------------------- Result galaxy s9(Google Shopping)  -------------------------------------')
print(results_GS_s9.summary())