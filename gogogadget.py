""" The following code is for the creation of a wine tasting journal, or what I like to call a Wino-mentary"""

#Greets then asks what user wants to do: New Entry, Search, or View All
import csv

write_stuff=open('wino.csv', 'a')
read_stuff= csv.DictReader((open("wino.csv", "rb")), delimiter= ',', quotechar= '"')

print "\nHi Jeanette!\n" "Drinking wine AGAIN I see...\n" 
tell_me = raw_input("What do you want to do?")
print ""


more = ["New", "new", "N", "n", "add", "New entry"]
old = ["Search", "search", "s", "S"]
see_all = ["Show", "view", "view all", "all"]
lush = ["Yes", "yes", "y"]


def add_entry(date, winery, wine_name, wine_type, year, buy, comment):
	data = {"Date of Visit": "", "Winery": "", "Name of Wine": "", "Wine Type": "" , "Year": "" , "Purchased": "", "Notes": ""}
# NEED TO FIX LIST- Seperates each letter
	save_list = []
	# input variable from raw input
	data["Date of Visit"] += date #variables
	data["Winery"] += winery
	data["Name of Wine"] += wine_name
	data["Wine Type"] += wine_type
	data["Year"] += year
	data["Purchased"] += buy
	data["Notes"] += comment
	
	save_list.append(data);

	fieldnames = ["Date of Visit", "Winery", "Name of Wine", "Wine Type", "Year", "Purchased", "Notes"]

	csvwriter = csv.DictWriter(write_stuff, fieldnames=fieldnames)
	
	csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
	for row in save_list:
		csvwriter.writerow(row)
#above code should add data value to dictionary and save to csv

#save data in file- Dictionaries within a master List to search?

if tell_me in more:
	print "OK, gimme the deets!"
	date = raw_input("Date of Visit:")
	winery = raw_input("Winery:")
	wine_name = raw_input("Name of Wine:")
	wine_type = raw_input("Wine Type:")
	year = raw_input("Year:")
	buy = raw_input("Purchased:")
	comment = raw_input("Notes:")
	add_entry(date, winery, wine_name, wine_type, year, buy, comment)
# elif tell_me in old:
# Call Search function
elif tell_me in see_all:
	print "You should be ashamed..."
	for row in read_stuff:
		print row
# # Above calls function to display all existing entries

another = raw_input("You lush! Anymore?")
 
def ask_again():
	print "OK, gimme the deets!"
	date = raw_input("Date of Visit:")
	winery = raw_input("Winery:")
	wine_name = raw_input("Name of Wine:")
	wine_type = raw_input("Wine Type:")
	year = raw_input("Year:")
	buy = raw_input("Purchased:")
	comment = raw_input("Notes:")
	add_entry(date, winery, wine_name, wine_type, year, buy, comment)


while another in lush:
	ask_again()

	another = raw_input("You lush! Anymore?")
else:
	print "You look thirsty!"
	# new function ask q's again which then runs add_entry


if another in see_all: 
	print "You should be ashamed..."
	reader = csv.reader(read_stuff)
	for row in reader:
		print row
else:
	print "You'll be back..."

# print new_entry("2015", "chandon", "cool", ["bubbles", "red"], "2010", "no", "tastes like burning")

#how to create a function that creates new dictionary?
write_stuff.close()





