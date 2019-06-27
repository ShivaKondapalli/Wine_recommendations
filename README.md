# Wine_recommendations

This project uses a simple Non-Negative Matrix Factorization (NMF) algorithm to compute similarities betwenn wines based on user ratings.

The resulting features from the NMF techinque are then persiste and used to send recommendation to a POST request sent to the
url 'http://localhost:5000/api'. This link won't work, just mentoining it for completness sake.

A flask route awaits a post request to be sent to it, and when it recieves a POST request, it sends a JSON reponse with the 
five most simlar wines to the wine_id asked in the request. 

The structure has three files. 

## model.py

Here, we read our data into a pandas dataframe. And like all NMF techniques required, we change the data to a product-user-matrix.

## server.py

This file contains the flask app which awaits a POST request and send back the response. 

## request.py

Here we send a wine_id of choice to the flask url and get back a json response. 


