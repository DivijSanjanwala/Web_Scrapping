from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html 5")
soup = BeautifulSoup(webpage.content, "html.parser")

ratings_data = soup.find_all(attrs={"class": "Rating"})
ratings = []

for rating in ratings_data[1:]:
  ratings.append(float(rating.string))
print(ratings)

plt.hist(ratings)
plt.show()

# Since all the table items of the company has the CSS class
# "company", we will use the select() function to get all.
companies_data = soup.select('.company')
companies = []
for company in companies_data[1:]:
  companies.append(company.get_text())
print(companies)

# Using panda to create a DataFrame

# First create a dictionary
dictionary_panda = {"Company": companies, "Ratings": ratings}

# Then convert it to a DataFrame using panda. 
data_frame_companies = pd.DataFrame.from_dict(dictionary_panda)

mean_values = data_frame_companies.groupby('Company').Rating.mean()
top_ten = mean_values.nlargest(10)
print(top_ten)

cocoa_percent_data = soup.select('.CocoaPercent')

cocoa_percent = []

for td in cocoa_percent_data[1:]:
  percent = int(td.get_text().strip('%'))
  cocoa_percent.append(percent)
print(cocoa_percent)

cocoa_percent_rating_dict = {"Companies": companies, "CocoaPercentage": cocoa_percent, "Rating": ratings}

data_frame_cocoa_percent = pd.DataFrame.from_dict(cocoa_percent_rating_dict)

top_ten_cocoa = data_frame_cocoa_percent.nlargest(100)

print(top_ten_cocoa)

plt.scatter(df.CocoaPercentage, df.Rating)
plt.show()

z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")

plt.clf()










