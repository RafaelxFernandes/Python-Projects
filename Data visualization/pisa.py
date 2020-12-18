import matplotlib.pyplot as plt
import numpy as np

columns_count = 3
bar_width = .2

# Data from Mean score in PISA 2012 for Math, Reading and Science
korea_scores = (554, 536, 538)
canada_scores = (518, 523, 525)
china_scores = (613, 570, 580)
france_scores = (495, 505, 499)

index = np.arange(columns_count)

# Plotting bar charts
korea = plt.bar(index, korea_scores, bar_width, alpha=.4, label="Korea")
canada = plt.bar(index + bar_width, canada_scores, bar_width, alpha=.4, label="Canada")
china = plt.bar(index + 2*bar_width, china_scores, bar_width, alpha=.4, label="China")
france = plt.bar(index + 3*bar_width, france_scores, bar_width, alpha=.4, label="France")

countries = [korea, canada, china, france]

def create_labels(data):
    for item in data:
        x = item.get_x()
        height = item.get_height()
        width = item.get_width()
        plt.text(x + width / 2., height * 1.05, '%d' % int(height), ha="center", va="bottom")

for country in countries:
    create_labels(country)
    

# Graph configuration
plt.title("Test scores by country in PISA 2012")
plt.xlabel("Subjects")
plt.ylabel("Mean score")
plt.xticks(index + (bar_width*3/ 2), ("Mathematics", "Reading", "Science"))
plt.legend(frameon=False, bbox_to_anchor=(1, 1) , loc=2)
plt.grid(True)

plt.show()