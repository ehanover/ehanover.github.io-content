# Yelp Restaurant Search Website

My Yelp Restaurant Search Website helps the user search for restaurants with a variety of search options, view details for a specific restaurant found in a search, and browse restaurants with special promotions.

This website was my submission to the 2020 Capital One [Software Engineering Summit](https://campus.capitalone.com/summits/). The program is a one week opportunity to practice problem solving and collaboration at a more professional level. I was one of the students selected to attend, and I will attend the Summit in August. 

### Technology choices
Since part of the Summit challenge is to develop a full website quickly, I picked a web framework that I was already familiar with, Vue.js. However, I had never used Vue to develop an application with so many different components and requirements. One of the requirements for the website was an interactive map from the Google Maps API. Adding the API was surprisingly simple and made my amateur website look much more professional.

The Yelp API is the main source of data for the website. Using that API was also simple because it provided simple endpoints to access the data. I also decided to implement the Zomato API that provides user reviews for many restaurants. However, the Zomato API is clearly not as popular or robust as the Yelp API. I had the some success finding reviews based using a location search with the coordinates returned from the Yelp API, but the majority of search results return reviews for the completely wrong restaurant. Additionally, the Zomato API is not up to date with the Yelp API so even if the location search returns the correct restaurant based on the location, it's likely that it returns information for a restaurant that doesn't exist anymore. 

In addition to the core requirements, I chose to implement data visualization using the [Highcharts library](https://www.highcharts.com/). Highcharts offers many unique graph types and I think the graphs I chose are unique and present the data in an interesting way. 

### Extensions
* Replace the Zomato API with an accurate and professional data source
* Add a chat bot (suggested by Capital One)
* Fix the browser location request so it only asks about location once
