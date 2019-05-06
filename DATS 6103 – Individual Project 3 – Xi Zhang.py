#!/usr/bin/env python
# coding: utf-8

# In[1]:


#DATS 6103 – Individual Project 2 – Xi Zhang
#Import libraries
import math
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import seaborn as sns
plt.style.use('ggplot')


# In[2]:


#Sign up for ploty
py.sign_in('Lieasea','qNHnauItAC7OY9UqCfOP')


# In[3]:


#Ignore the warnings below.
import warnings
warnings.filterwarnings('ignore')


# In[4]:


plotly.offline.init_notebook_mode()


# ## Overview of Access of Electricity to the World
# Overview of global electricity access from 2000 to 2015.

# In[5]:


#Read raw data,reset the index
dd = pd.read_excel("Data/Total.xls", header=3)
#select the data from 2000 to 2015
df = dd.iloc[:,-21:-3]
#Append country code and country name to dataframe
df['1998'] = dd['Country Code']
df['1999'] = dd['Country Name']
df.rename(columns={df.columns[0]: "Country Code" }, inplace=True)
df.rename(columns={df.columns[1]: "Country Name" }, inplace=True)
#Fill missing data to 0
df = df.fillna(0)
df.head(10)


# In[6]:


#World Choropleth Map
def mapper(year):
    data = [go.Choropleth(
        locations = df['Country Code'],
        z = df[year],
        text = df['Country Name'],
        colorscale=[[0.0, 'rgb(165,0,38)'], 
                    [0.1, 'rgb(215,48,39)'], 
                    [0.2, 'rgb(244,109,67)'], 
                    [0.3, 'rgb(253,174,97)'], 
                    [0.4, 'rgb(254,224,144)'], 
                    [0.5, 'rgb(224,243,248)'], 
                    [0.6, 'rgb(171,217,233)'], 
                    [0.7, 'rgb(116,173,209)'], 
                    [0.8, 'rgb(69,117,180)'], 
                    [1.0, 'rgb(49,54,149)']],
        autocolorscale = False,
        reversescale = True,
        marker = go.choropleth.Marker(
            line = go.choropleth.marker.Line(
                color = 'rgb(180,180,180)',
                width = 0.5
            )),
        colorbar = go.choropleth.ColorBar(
            tickprefix = '%',
            title = 'Percentage of Access'),
    )]

    layout = go.Layout(
        title = go.layout.Title(
            text = 'Access to Electricity ' + str(year) + '<br> (% of population)'
        ),
        geo = go.layout.Geo(
            showframe = False,
            showcoastlines = False,
            projection = go.layout.geo.Projection(
                type = 'equirectangular'
            )
        ),
        annotations = [go.layout.Annotation(
            x = 0.55,
            y = 0.1,
            xref = 'paper',
            yref = 'paper',
            text = 'Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
                CIA World Factbook</a>',
            showarrow = False
        )]
    )

    fig = go.Figure(data = data, layout = layout)
    return py.iplot(fig, filename = 'd3-world-map')


# In[7]:


mapper('2000')


# In[8]:


mapper('2015')


# In[9]:


#Count countries
len(df)


# In[55]:


#Remove non-numeric columns
df_int = df.drop(['Country Code','Country Name'], axis=1)
dfsum = df_int.sum()
#Standerdize to percentage level
dfsum = dfsum/264
#Use a bar chart to show changes in electricity Access between 2000 and 2015
dfsum.plot("bar", alpha=0.5, figsize=(18,7), color="#0abab5")
plt.title("World Total Electricity Access by Year", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("% of Population", fontsize=12)
plt.xticks(rotation=0, fontsize=12)
#Save the plots to folder
plt.savefig("img/TotalElectricityAccess.png", bbox_inches='tight') 
plt.show()


# The world map gives a very visual view of how electricity rates have changed in different countries over the past decade.The bar chart illustrates that the global electricity supply rate has been rising steadily since 2000.

# ## The State of Nuclear Power in Electricity
# Due to the economic advantages and environmental considerations, nuclear power has become the most potential and most likely to gradually replace the traditional energy generation mode in recent years. But because of upfront costs and international regulations, not every country can afford nuclear power. So this time I will study ten countries with nuclear power plants and further illustrate he state of nuclear power in electricity.

# In[11]:


#Read raw data,reset the index
uu = pd.read_excel("Data/Nuclear.xls", header=3)
#select the data from 2000 to 2015
nuclear = uu.iloc[:,-21:-3]
#Append country code and country name to dataframe
nuclear['1998'] = uu['Country Code']
nuclear['1999'] = uu['Country Name']
nuclear.rename(columns={nuclear.columns[0]: "Country Code" }, inplace=True)
nuclear.rename(columns={nuclear.columns[1]: "Country Name" }, inplace=True)
#Fill missing data to 0
nuclear = nuclear.fillna(0)
#Fill na to the mean value
#nuclear.fillna(nuclear.mean(axis=0), axis=0)
#m = nuclear.mean(axis=1)
#for i, col in enumerate(nuclear):
#    nuclear.iloc[:, i] = nuclear.iloc[:, i].fillna(m)
#Filter the top 10 countries of electricity production from nuclear sources
nuclear_top = nuclear.sort_values('2010', ascending = False).head(10).drop(['Country Code'], axis = 1)
nuclear_top.head(10)


# In[12]:


#World Choropleth Map
def mapper_nuclear(year):
    data = [go.Choropleth(
        locations = nuclear['Country Code'],
        z = nuclear[year],
        text = nuclear['Country Name'],
        colorscale=[[0.0, 'rgb(165,0,38)'], 
                    [0.1, 'rgb(215,48,39)'], 
                    [0.2, 'rgb(244,109,67)'], 
                    [0.3, 'rgb(253,174,97)'], 
                    [0.4, 'rgb(254,224,144)'], 
                    [0.5, 'rgb(224,243,248)'], 
                    [0.6, 'rgb(171,217,233)'], 
                    [0.7, 'rgb(116,173,209)'], 
                    [0.8, 'rgb(69,117,180)'], 
                    [1.0, 'rgb(49,54,149)']],
        autocolorscale = False,
        reversescale = True,
        marker = go.choropleth.Marker(
            line = go.choropleth.marker.Line(
                color = 'rgb(180,180,180)',
                width = 0.5
            )),
        colorbar = go.choropleth.ColorBar(
            tickprefix = '%',
            title = 'Percentage of Total'),
    )]

    layout = go.Layout(
        title = go.layout.Title(
            text = 'Electricity production from nuclear sources ' + str(year) + '<br> (% of total)'
        ),
        geo = go.layout.Geo(
            showframe = False,
            showcoastlines = False,
            projection = go.layout.geo.Projection(
                type = 'equirectangular'
            )
        ),
        annotations = [go.layout.Annotation(
            x = 0.55,
            y = 0.1,
            xref = 'paper',
            yref = 'paper',
            text = 'Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
                CIA World Factbook</a>',
            showarrow = False
        )]
    )

    fig = go.Figure(data = data, layout = layout)
    return py.iplot(fig, filename = 'd3-world-map')


# In[13]:


mapper_nuclear('2010')


# In[14]:


#Set the country name column as index
nuclear_top.set_index('Country Name',inplace=True)


# In[15]:


#Due to the limitations of the data, the top 60 countries with nuclear power were selected for the study
nuclear1 = pd.read_excel("Data/Nuclear.xls", header=3, index_col=0)
nuclear2 = nuclear1.iloc[:,-19:-3]
nuclear_top60 = nuclear2.sort_values('2010', ascending = False).head(60)
nuclear_top60_list = list(nuclear_top60.index)
nuclear_top60_list


# In[16]:


#The top 10 countries with the highest use of nuclear power
topnuclear = nuclear_top60.loc[['France',
 'Slovak Republic',
 'Belgium',
 'Ukraine',
 'Hungary',
 'Switzerland',
 'Sweden',
 'Armenia',
 'Slovenia',
 'Bulgaria'],
['2000','2001','2002','2003','2004','2005','2006','2007',
'2008','2009','2010','2011','2012','2013','2014','2015']]
topnuclear


# In[56]:


def fun_line(data):
    #Set up the figure size.
    plt.figure(figsize=(10,10))
    for i in range(0,10):
        #label x-axis
        x = list(data.columns.values)
        #ME from every country in every year.
        y = data.ix[i,:]
        # plotting the line and adjust detail.
        plt.plot(x, y,  marker='o') 
    # Show the legend on the plot.
    plt.legend(loc=(1.1,0.7))    
    # Name the x axis.
    plt.xlabel('Years') 

fun_line(topnuclear)
# Name the y axis(the units may need to adjust in the latter plot). 
plt.ylabel('% of total') 
# Set title for the plot.
plt.title('Electricity Production from Nuclear Sources') 
#Save the plots to folder
plt.savefig("img/Top10NuclearLine.png", bbox_inches='tight')  
# Show plot. 
plt.show() 


# In[18]:


def PiePlot(year):
    df = nuclear_top60[year]
    top = df.sort_values(ascending=False)
    top = top.reset_index()
    top.index = top.index + 1
    others = top[10:].sum()[1]
    top = top[:10]
    top.loc[11] = ['All Other Countries', others]
    
    countryPlot = top[year].plot.pie(subplots=True,
                                     autopct='%0.1f',
                                     fontsize=10,
                                     figsize=(10,10),
                                     legend=True,
                                     labels=top['Country Name'],
                                     shadow=False,
                                     explode=(0.15,0,0,0,0,0,0,0,0,0,0),
                                     startangle=90,title = ('Electricity Production from Nuclear Sources ' + year))


# In[57]:


PiePlot('2013')
#Save the plots to folder
plt.savefig("img/NuclearPie.png", bbox_inches='tight')  
plt.show()


# In[20]:


#Build a function of single line chart.
def fun_singleline(d, c):
    plt.figure(figsize=(10,10))
    #label x-axis.
    x = list(d.columns.values)
    #ME from every country in every year.
    y = d.ix[c,:]
    # plotting the line and adjust detail.
    plt.plot(x, y,  marker='o') 
    # Show the legend on the plot.
    plt.legend(loc=(1.1,0.7))    
    # Name the x axis.
    plt.xlabel('Years') 


# In[58]:


#Function of Single line chart:
fun_singleline(topnuclear, 'France')
#label the x-axis and title the chart.
plt.ylabel('% of total') 
plt.title('Electricity Production from Nuclear Sources in France')
#Save the plots to folder
plt.savefig("img/FranceNuclear.png", bbox_inches='tight')  
plt.show() 


# It is clear that France is the world leader in the use of nuclear power for electricity, far ahead of other countries (accounting for about 80% of total electricity generation and 7.6 percent of the world's nuclear power generation). Therefore, I will take France as an example to analyze the growth rate of nuclear power generation in recent years and the interaction between nuclear power generation and traditional power generation. And a rough prediction for the next few years.

# In[33]:


#Nuclear sources of electricity in France
listFrance = topnuclear.loc['France']
#Other sources of electricity in France
multi = pd.read_excel("Data/multi.xls", index_col = 0, header=3)
Franceothers = multi.loc[['France'],
['2000','2001','2002','2003','2004','2005','2006','2007',
'2008','2009','2010','2011','2012','2013','2014','2015']]
listFranceothers = Franceothers.loc['France']


# In[23]:


#Build a primitive dataframe for two different power sources in France
d = {'Country Name':['France(Nuclear)'],'2001':[-0.35],'2002':[0],'2003':[0],'2004':[0],'2005':[0],'2006':[0],'2007':[0],
              '2008':[0],'2009':[0],'2010':[0],'2011':[0],'2012':[0],'2013':[0],'2014':[0],'2015':[0]}
growthrate = pd.DataFrame(data=d)
#Set the country name column as index
growthrate.set_index('Country Name',inplace=True)
growthrate.loc['France(Others)'] = 0.00


# In[24]:


#Calculate the annual growth rate in nuclear power
listgrowthnuclear=growthrate.iloc[0]
i=0
for i in range (0,15):
    listgrowthnuclear[i] =listFrance[i+1] - listFrance[i]
listgrowthnuclear


# In[60]:


#Line-bar chart of groth rate of nuclear
listgrowthnuclear.plot(figsize=(14, 5), kind="line",color = "#FC8743")
listgrowthnuclear.plot(figsize=(14, 5), kind="bar",color = "#B92222")
plt.legend(bbox_to_anchor=(1, 1), fontsize=12)
plt.title("Growth Rate of Nuclear Electricity Resources in France in Recent 15 Years", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("percentage % of Total", fontsize=12)
plt.xticks(rotation=1, fontsize=12)
#Save the plots to folder
plt.savefig("img/FranceNuclearLineBar.png", bbox_inches='tight')  
plt.show()


# In[34]:


#Calculate the annual growth rate in other resources 
listgrowthothers = growthrate.iloc[1]
i=0
for i in range (0,15):
    listgrowthothers[i] = listFranceothers[i+1] - listFranceothers[i]
listgrowthothers


# In[61]:


#Line-bar chart of groth rate of other resources
listgrowthothers.plot(figsize=(14, 5), kind="line",color = "#0abab5")
listgrowthothers.plot(figsize=(14, 5), kind="bar",color = "#3B8AC6")
plt.legend(bbox_to_anchor=(1, 1), fontsize=12)
plt.title("Growth Rate of Other Electricity Resources in France in Recent 15 Years", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("percentage % of Total", fontsize=12)
plt.xticks(rotation=1, fontsize=12)
#Save the plots to folder
plt.savefig("img/FranceOthersLineBar.png", bbox_inches='tight')  
plt.show()


# In[36]:


#Fill the calculation result into dataframe
growthrate.iloc[0] = listgrowthnuclear
growthrate.iloc[1] = listgrowthothers


# In[37]:


growthrate


# In[63]:


#The growth rate of different energy use is shown in a bar chart
growthrate.plot(figsize=(14, 6), kind="bar")
plt.legend(bbox_to_anchor=(1, 1), fontsize=12)
plt.title("Growth Rate of Multiple Electricity Resources in Top 10 Nuclear Coutries", fontsize=16)
plt.xlabel("Country", fontsize=14)
plt.ylabel("percentage % of Total", fontsize=12)
plt.xticks(rotation=1, fontsize=12)
#Save the plots to folder
plt.savefig("img/France-Nuclear-Others-Bar.png", bbox_inches='tight')  
plt.show()


# It can be seen from the two histograms that the increase and decrease of nuclear energy are obviously higher than other energy sources, but for France, the growth rate of nuclear energy is still higher in recent years.And it seems that while nuclear power is on the rise, other sources of energy are likely to decline in the same year.

# In[64]:


#Line plot of growth rate of multiple electricity resources in france in recent 15 years
#Line of groth rate of other resource
listgrowthothers.plot(figsize=(14, 5), kind="line",color = "#0abab5")
#Line of groth rate of nuclear
listgrowthnuclear.plot(figsize=(14, 5), kind="line",color = "#FC8743")
plt.legend(bbox_to_anchor=(1, 1), fontsize=12)
plt.title("Growth Rate of Multiple Electricity Resources in France in Recent 15 Years", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("percentage % of Total", fontsize=12)
plt.xticks(rotation=1, fontsize=12)
#Save the plots to folder
plt.savefig("img/France-Nuclear-Others-Line.png", bbox_inches='tight')  
plt.show()


# The relationship between two different energy sources is more intuitive in the line diagram. In this 15-year data, we can see that the peak value of nuclear energy often corresponds to the valley value of other energy sources. And we can see that in recent years, the growth of nuclear power generation has decreased, while the growth of traditional energy has increased. So we can expect France's traditional energy consumption to increase in the next few years.
# In the following research, I will continue to discuss the relationship between nuclear energy and other energy sources in detailed categories.

# ## The Impact of Nuclear and other Sources of Electricity

# In[40]:


#Set up a data frame for multiple electricity resources in top 60 nuclear countries
comparediff = nuclear_top60.loc[nuclear_top60_list,['2010']]
comparediff.rename(columns={comparediff.columns[0]: "Nuclear" }, inplace=True)
#Append coal
coal = pd.read_excel("Data/coal.xls", index_col = 0, header=3)
comparediff['Coal'] = coal.loc[nuclear_top60_list,['2010']]
#Append oil
oil = pd.read_excel("Data/oil.xls", index_col = 0, header=3)
comparediff['Oil'] = oil.loc[nuclear_top60_list,['2010']]
#Append hydroelectric
hydro = pd.read_excel("Data/hydro.xls", index_col = 0, header=3)
comparediff['Hydroelectric'] = hydro.loc[nuclear_top60_list,['2010']]
#Append the sum of oil, gas and coal
multi = pd.read_excel("Data/multi.xls", index_col = 0, header=3)
comparediff['Oil/Gas/Coal'] = multi.loc[nuclear_top60_list,['2010']]

comparediff.tail()


# In[65]:


#Compare different electricity resources in bar chart
top10_4 = comparediff[0:10]
top10_4.plot(figsize=(14, 6), kind="bar")
plt.legend(bbox_to_anchor=(1, 1), fontsize=12)
plt.title("Multiple Electricity Resources in Top 10 Nuclear Coutries", fontsize=16)
plt.xlabel("Country", fontsize=14)
plt.ylabel("percentage % of Total", fontsize=12)
plt.xticks(rotation=50, fontsize=12)
#Save the plots to folder
plt.savefig("img/Top10-Multiple-Bar.png", bbox_inches='tight')  
plt.show()


# As the use of nuclear power declines (especially below 50 percent), countries tend to have a single source that is the country's primary source of electricity. This single resource is often many times larger than any other resource except nuclear power (such as Switzerland and Bulgarian coal).This may represent this country's main source of electricity generation before nuclear power.

# In[42]:


nuclear4 = comparediff.loc[:,['Nuclear','Coal','Oil', 'Hydroelectric']]
s=nuclear4.loc['France']
s_labels=list(sorted(s.keys()))
s_fracs=[s.get(s_labels[i]) for i in range(len(s_labels))]

p=nuclear4.loc['Bulgaria']
p_labels=list(sorted(p.keys()))
p_fracs=[p.get(p_labels[i]) for i in range(len(p_labels))]

fig=plt.figure()
plt.pie(p_fracs,labels=p_labels,radius=2.3,autopct='%1.1f%%',pctdistance=0.8)
plt.pie(s_fracs,labels=s_labels,radius=1,autopct='%1.1f%%',pctdistance=0.8)
plt.legend(loc='best', bbox_to_anchor=(-0.2, 1.4))

#plt.title('s,p',fontsize=20,loc='center')
plt.show()


# ### Ratio of Electricity Resources in France (inner) and Bulgaria (outer)
# More than 80 percent of France's electricity comes from nuclear power. In Bulgaria, coal produces more than half the electricity. In addition to nuclear power, coal is far more important in Bulgaria than hydropower or oil.This further illustrates what the main source of electricity was before nuclear power. This nested pie chart is a milestone in the recent development of nuclear power.

# In[66]:


#Compare different electricity resources in bar chart
top60_2 = comparediff.loc[:,['Nuclear','Oil/Gas/Coal']]
top60_2.plot(figsize=(14, 6), kind="line")
plt.legend(bbox_to_anchor=(1, 1), fontsize=12)
plt.title("Change of other Sources of Electricity as Nuclear Power Diminishes", fontsize=16)
plt.xlabel("Country", fontsize=14)
plt.ylabel("percentage % of Total", fontsize=12)
plt.xticks(rotation=50, fontsize=12)
#Save the plots to folder
plt.savefig("img/Top60-Nuclear-Others-Line.png", bbox_inches='tight')  
plt.show()


# But with the development of time, what does the development of nuclear energy bring to the traditional power resources?
# The 60 countries selected are ranked in descending order of nuclear power use. With the decrease of the utilization rate of nuclear energy, it is obvious that the utilization rate of oil, gas and coal is gradually increasing. So nuclear power does complement other sources of electricity.

# In[70]:


def scatter(Resource):
    df = comparediff
    plt.figure(figsize = (10,6))
    # use the function regplot to make a scatterplot
    sns.regplot(x=df["Nuclear"], y=df[Resource])
    #sns.plt.show()

    # Without regression fit:
    sns.regplot(x=df["Nuclear"], y=df[Resource])
    plt.title("Correlation between Nuclear and " + Resource + " on Electricity", fontsize=16)
    #sns.plt.show()


scatter('Coal')
#Save the plots to folder
plt.savefig("img/Scatter-Coal.png", bbox_inches='tight')
plt.show()
scatter('Oil')
#Save the plots to folder
plt.savefig("img/Scatter-Oil.png", bbox_inches='tight')
plt.show()
scatter('Hydroelectric')
#Save the plots to folder
plt.savefig("img/Scatter-Hydro.png", bbox_inches='tight')
plt.show()


# In these scatter plots, we can see that coal, oil and hydropower are negatively correlated with nuclear power, among which nuclear power has the greatest impact on coal and the least impact on hydropower. But we can expect coal and fuel to be replaced as nuclear power becomes more widely used. As a result, less and less waste gas will be released into the atmosphere, and our environment will eventually be improved.

# ## Reference

# The World Bank Group (2019). Access to electricity (% of population), from 
#     https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS

# The World Bank Group (2019). Electricity production from nuclear sources (% of total), from 
#     https://data.worldbank.org/indicator/EG.ELC.NUCL.ZS

# The World Bank Group (2019). Electricity production from coal sources (% of total), from 
#     https://data.worldbank.org/indicator/EG.ELC.COAL.ZS
# 

# The World Bank Group (2019). Electricity production from coal sources (% of total), from 
#     https://data.worldbank.org/indicator/EG.ELC.PETR.ZS
# 

# The World Bank Group (2019). Electricity production from hydroelectric sources (% of total), from 
#     https://data.worldbank.org/indicator/EG.ELC.HYRO.ZS
# 

# The World Bank Group (2019). Electricity production from oil, gas and coal sources (% of total), from 
#     https://data.worldbank.org/indicator/EG.ELC.FOSL.ZS

# ## Publications
# 

# GitHub.io: https://f0000000x.github.io/f000000x.github.io/
# 

# GitHub:https://github.com/f0000000x/Project-3

# Zenodo: https://zenodo.org/record/2669677#.XNCwYutKhbU
