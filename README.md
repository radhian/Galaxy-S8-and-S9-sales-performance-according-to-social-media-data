# Galaxy-S8-and-S9-sales-performance-according-to-social-media-data

<b>1.	Introduction </b> 

This project evaluates how the social media data can be leveraged to analyze the sales performance of galaxy s8 and s9. For both mobile phones, we are going to predict the sales numbers (in millions of units) according to the trends on YouTube search, web search and google shopping. The sales data is elaborated from several news snapshots while the social media data (i.e. trends) is retrieved from google trends. By using python, the data analysis adapts Ordinary Least Square (OLS) regression method to find whether the sales and the social media trends have a relation. The evaluation is carried out every quarter year from 2017-2018.   

<b>Research questions</b> : How to predict the sales numbers of galaxy s8 and s9 accoding to trends on youtube search and web search?

<b>Trend scale</b> : Worldwide



<b>2.	Methods</b> 

2.1.	Research methodology  
First thing first, this research is started from the question: “How to predict the sales numbers of Galaxy s8 and s9 according to trends on the Social Media Trends?”. In this quantitative analysis, sales numbers for Galaxy s8 and s9 are compared with data from Google Trends. An output number between 0 and 100 is provided by Google Trends by analyzing the number of searches for a specific keyword. Accordingly, this output number would be the independent variable. As we know, the independent variable (i.e. trends) is expected to have an influence towards dependent variable (i.e. sales numbers). In common sense, if people is interested in a product, they will try to find more information about the product. A simple way for gaining information is usually through a today’s social media (i.e. google search, YouTube, Google Shopping). Thus, as the interest in those products is rising, the search number on the corresponding social media is improving. Hence, the purchase decisions are eventually increasing. 
To simplify this, the hypothesis for this research would be “The number of sales increases proportionally when the number of search on the corresponding social media increase”. A linear regression is utilized as a data analytic model. The linear regression can determine whether the sales and trends are correlated linearly. Also, we are able to predict the future sales for those smartphones if the datasheet shows a good linear correlation between sales and trends. 

2.2	     Data Collection
The sales data of Galaxy s8 and s9 are retrieved from the news snapshots from internet. The data were collected quarterly from January 2017 until September 2018. The sales data for Galaxy s8 is only available on Q1-Q4 2017. Whereas the sales data for Galaxy s9 is only available on Q1-Q3 2018.
The trends data are collected from Google Trends which can be searched via the search term, timeframe, and the geographic location. The search term requires the specific keywords that users are likely to search and representing the smartphones models. In this case, the keywords for each smartphone would be “galaxy s8” and “galaxy s9”. The geographic location is determined as a worldwide. For the time frame, we need to specify the trends for every quarter year period. Accordingly, the sales and trends data are available to be proceed. 





<b>3.	Results</b> 

3.1.	Correlation evidence 

In python, we will utilize “statsmodels” library to perform a OLS linear regression. Statsmodel is a Python library designed for more statistically-oriented approaches to data analysis, with an emphasis on econometric analyses. The OLS regression will determine the linear characteristic between 2 sets of data (i.e. sales and trends). Apparently, the OLS regression results in python will provide a lot of information, as shown in table 3.1. The parameters that we think are more important will eventually prove our hypothesis. 
Our hypothesis is whether sales and trends have a significant relationship linearly. Mainly, two parameters that responsible for this are “R-squared” and “P-value”. “R-squared” is a statistical measurement of how well the regression line approximates the real data points. P-value indicates whether the result accept or reject the hypothesis. P-value with the null-hypothesis (i.e. coefficient equals to 0) is indicating a true condition. If it is less than the confidence level, often 0.05, it indicates that there is a statistically significant relationship between the term and the response. 

According the results, all of the results shows a strong correlation between sales and trends data for every social media. In this case, all P-values are below the confident level (i.e. 0.5). The evidence is also stronger because of the high values of R-squared. It indicates the variance of the linear estimation and the scattered data is quite small. Thus, the scattered data is considerably fit enough with the linear estimation. Therefore, our hypothesis is considerably proven. 
However, the Google shopping results always show the smallest R-squared result and the largest P-value. This phenomenon depicts the google shopping has the weakest relationship to the sales. Figure 1. can explain how this can happen. Among those figures, the trends of google shopping did not drop dramatically after the launch in the first month. While the sales dropped significantly after the first month of launch, especially for galaxy s8. Thus, the sales are slightly not aligned with the google shopping trends. As the result, Google shopping shows the weakest relation among others.

