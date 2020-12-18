import matplotlib.pyplot as plt


labels = "Python", "C++", "Ruby", "Java", "PHP"
sizes = [33, 52, 12, 47, 62] # !!! Not real data !!!
separated = (.1, 0, 0, 0, 0)

plt.title("Most used programming languages in 2019")
plt.pie(sizes, labels=labels, autopct="%1.1f%%", explode=separated)
plt.axis('equal')
plt.show()