DATA DESCRIPTION
  Data was mined from https://boardgamegeek.com/browse/boardgame, Name, Rank, Average Rating, Geek Rating, Votes details were extracted for 5000 distinct games. 

ORDER IN WHICH DATA SCRAPPED
1. Load and run board_request.py, this file gets you the html for the first 50 pages of the boardgamegeek website and stores it in a folder name html_files
2. Load and run ratings_parse.py, this file scrapes the geek ratings, average ratings and the votes for all 5000 game into a csv file called boardgame_ratings_data.csv located in the parsed_results folder.
3. load and run board_info_parse_and_merge.py, this file scrapes the Rank and Name of all the games, stores them in a csv file called boardgame_info_data.csv, the code then has a extension that merges boardgame_ratings_data.csv and boardgame_info_data.csv together to create the complete dataset called boardgame_dat.csv.   there is an additional extension of this board_info_parse_and_merge.py that then drops the Name column so we ccan have a dataset that containes only numbers which we would use for our analysis, the name of this final dataset is called boardgame_data.csv

DATA ANALYSIS USING supervised learning models 
A series of analysis were performed on the ddtaset testing different machine learning models and evaluating the efficicncy of each of these models
1. we started with the basic OLS linear regression with the file board_ols.py and predicted a range of values with this model

2. We then used Kneighbors Classifier board_knn.py to analyse the data and predict the same range of values using exactly the same input.
3. Then we run a pair of unsupervised learning models and compare the results and accuracy of each of the model on our data set, the models used are file board_decision.py and board_randomforest.py
