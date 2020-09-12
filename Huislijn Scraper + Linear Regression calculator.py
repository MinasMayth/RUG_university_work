# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:25:15 2020

@author: samya


This is a data scraper for the dutch housing website Huislijn.nl for houses in Groningen. 
The scraper extracts the price, area and number of rooms for each house and then stores them into arrays.
These arrays are then plotted onto a scatter plot and linear regression calculations are performed with them.
There is a possibility to improve this code even further, for example by implementing more cities.

"""

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import re
from bs4 import BeautifulSoup
import requests
    

def bs4_scraper():
    
    #Definition of lists that will be converted to np arrays and used later
    prices = []
    areas = []
    no_of_rooms = []
    
    #Sets the number of pages to be scraped. If this value passes the actual number of pages the function will return empty data, which is fine.
    pages = np.arange(1, 8, 1)
    
    for page in pages:
        
        #Scraping the site for houses for sale in groningen - This could be changed to other cities relatively easily!
        if page == 1:
            url = "https://www.huislijn.nl/koopwoning/nederland/groningen/groningen"
        else:
            url = ("https://www.huislijn.nl/koopwoning/nederland/groningen/groningen?page=" + str(page))
        r = requests.get(url)
        r_html = r.text
        
        soup = BeautifulSoup(r_html, "html.parser")
        
        
        
        #Price finder!
        for uncleaned_data in soup.find_all(class_="object-price"):
            #converts data to string to allow for editing
            uncleaned_data = str(uncleaned_data)
            # Removes all style and class tags
            uncleaned_data = re.sub(r'<[^>]*?>', '', uncleaned_data)
            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in uncleaned_data.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            cleaned_data = '\n'.join(chunk for chunk in chunks if chunk)
            # The data is directly available as prices so it can be converted from string into float and assigned a corresponding name
            price = float(cleaned_data)
            # Appends the price into list
            prices.append(price)
            
         
        #Area and no_of_rooms finder
        for uncleaned_data in soup.find_all(class_="object-size"):
            #converts data to string to allow for editing
            uncleaned_data = str(uncleaned_data)
            # Removes all style and class tags
            uncleaned_data = re.sub(r'<[^>]*?>', '', uncleaned_data)
            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in uncleaned_data.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            cleaned_data = '\n'.join(chunk for chunk in chunks if chunk)
            
            #The data is split back into lines so we can extract the values for area and number of rooms
            lines2 = (line.strip() for line in cleaned_data.splitlines())
            for line in lines2:
                #strings are split into individual chunks.  
                chunks2 = line.split(" ")
                #Validation checker for area
                if chunks2[1] == ('m2'):
                    areas.append(float(chunks2[0]))
                #Validation checker for no_of_rooms
                if chunks2[1] == ('kamers'):
                    no_of_rooms.append(int(chunks2[0]))
                    
        
        
    x = zip(prices,areas,no_of_rooms)
    return(x)


def LinearRegressionFunction(data):
    #Unzips the data so it can be used again
    res = list(zip(*data)) 
    
    #Converts the lists to Numpy array so they can be used in editing
    house_prices = np.array(res[0]).reshape(-1, 1)
    area = np.array(res[1]).reshape(-1, 1)
    number_of_rooms = np.array(res[2]).reshape(-1, 1)
    
    #Plots a graph of Area vs Price (Graph 1)
    plt.scatter(area, house_prices, s=4)
    plt.title("Graph 1")
    plt.xlabel('Area (m^2)')
    plt.ylabel('House Price (€)')
    plt.show()

    #Linear Regression Modelling for Graph 1
    graph1_model = LinearRegression(fit_intercept=True).fit(area, house_prices)
    print('The fitted slope of Graph 1 is:', graph1_model.coef_)
    print('The fitted intercept of Graph 1 is:', graph1_model.intercept_)
    print('The correlation coefficient of Graph 1 is', graph1_model.score(area,house_prices))

    #Plots a graph of Number of rooms vs Price (Fraph 2)
    plt.scatter(number_of_rooms, house_prices, s=4)
    plt.title("Graph 2")
    plt.xlabel('Number of Rooms')
    plt.ylabel('House Price (€)')
    plt.show()
    
    #Linear Regression Modelling for Graph 2
    graph2_model = LinearRegression(fit_intercept=True).fit(number_of_rooms, house_prices)
    print('The fitted slope of Graph 2 is:', graph2_model.coef_)
    print('The fitted intercept of Graph 2 is:', graph2_model.intercept_)
    print('The correlation coefficient of Graph 2 is', graph2_model.score(number_of_rooms,house_prices))

    #Predictions from graph 2
    no_of_rooms = np.arange(2, 7, 1)
    for counter in no_of_rooms:
        prediction = np.array([counter]).reshape((1, -1))
        y_pred = graph2_model.predict(prediction)
        print("Graph 2 price prediction for " + str(counter) + " rooms:", y_pred, sep='\n')


if __name__ == "__main__":
    LinearRegressionFunction(bs4_scraper())