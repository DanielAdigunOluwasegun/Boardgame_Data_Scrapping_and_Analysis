import os
from bs4 import BeautifulSoup
import glob
import pandas as pd 

if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/*.html"):
	print("parsing: " + one_file_name)
	scrapping_time = os.path.splitext(os.path.basename(one_file_name))[0].replace("boardgames","")
	f = open(one_file_name, "r", encoding="utf-8")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	board_table = soup.find("table", {"class": "collection_table"})
	board_tbody = board_table.find("tbody")
	board_rows = board_tbody.find("tr").find_all("th")
	print(board_rows)
	# for r in board_rows:
	#     game_rank = r.find("td", {"id": "collection_rank"})
	#     print(game_rant)
	    #currency_short_name = r.find("td", {"class": "currency-name"}).find("span",{"class": "curreny-symbol"}).find("a").text
# 	    game_name = r.find("td", {"class": "collection_objectname"}).find("align":"center").text
# 	    game_grating = r.find("td", {"class": "collection_bggrating"})
# 	    game_arating = r.find("td", {"class": "collection_bggrating"})
# 	    game_voters = r.find("td", {"class": "collection_bggrating"})
# 	    game_pricelist = r.find("td", {"class": "collection_shop"})
#	 	#print(game_rank)
# 	    #print(game_name)
# 	    #print(game_grating)
# 	    #print(currency_market_cap)
# 	    #print(currency_price)
# 	    #print(currency_volume)
# 	    #print(currency_supply)
# 	    #print(currency_change)

# 	    df = df.append({
# 	    	'scrapping_time': scrapping_time,
# 	    	'name': equity_name,
# 	    	'sector': equity_sector,
# 	    	'price': equity_price,
# 	    	'change': equity_change,
# 	    	'YTD': equity_ytd,
# 	    	'date': equity_date
# 	    	}, ignore_index=True)
# #print(df)
# df.to_csv("parsed_results2/nse_dataset.csv")
