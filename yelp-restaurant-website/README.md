# Yelp Restaurant Search Website

My Yelp Restaurant Search Website lets the user search for restaurants with a variety of search options, view details for a specific restaurant found in a search, and browse restaurants with active special promotions.

This website was my submission to the 2020 Capital One [Software Engineering Summit](https://campus.capitalone.com/summits/). The program is a one week opportunity to practice  problem solving and collaboration at a higher professional level. I was one of the students selected to attend, and I will attend the Summit in August. 

### Technology choices
Since part of the challenge of the Software Engineering Summit is developing a full website quickly, I picked a web framework that I was already familiar with, Vue.js. However, I had never used Vue to develop an application with so many different components and requirements. One of the requirements for the website was an interactive map from the Google Maps API. Adding the API was surprisingly simple and made my amateur website look much more professional and legit. 

The Yelp API is the main source of data for the website. Using that API was also simple because it provided simple and understandable endpoints. I also decided to implement the Zomato API that provides user reviews for many restaurants. However, the Zomato API is clearly not as popular or robust as the Yelp API. I had the most success finding reviews based using a location search with the coordinates given from the Yelp API, but this is clearly flawed and the majority of search results return reviews for the wrong restaurant. Additionally, the Zomato API is not up to date with the Yelp API so even if the location search returns the correct restaurant based on location, it's likely that it's a restaurant that has been replaced by a newer restaurant. 

Another extension I chose to implement was data visualization using the [Highcharts library](https://www.highcharts.com/). Highcharts offered many unique graph types and I think the graphs I chose are unique and present the data in an interesting yet effective way. 

### Extensions
* Replace the Zomato API with an accurate and professional data source
* Add a chat bot (suggested by Capital One)
* Fix location request so it only asks once