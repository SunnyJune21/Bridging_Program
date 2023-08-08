# 1. Plotting a straight line using Matplotlib
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 5])
ypoints = np.array([0, 25])

plt.plot(xpoints, ypoints)
plt.show()


# 2. Plotting a scatter plot using Matplotlib
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 3, 4, 7, 9])
ypoints = np.array([0, 2, 5, 6, 9])

plt.plot(xpoints, ypoints, 'o')
plt.show()


# 3. Plotting a curve using Matplotlib with given data points
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([20, 30, 5, 12, 39, 48, 50, 3])

plt.plot(x, y)
plt.title("Curve plotted using the given points")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# 4. Creating a smooth curve plot
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([20, 30, 5, 12, 39, 48, 50, 3])

X_Y_Spline = make_interp_spline(x, y)
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

plt.plot(X_, Y_)
plt.title("Smooth Curve Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# 5. Creating a bar chart for programming language popularity
import matplotlib.pyplot as plt

def bar_chart(numbers, labels, pos):
    plt.bar(pos, numbers, color=color)
    plt.xticks(ticks=pos, labels=labels)
    plt.title("Popularity of different programming languages", fontsize=12)
    plt.xlabel("Programming Languages")
    plt.ylabel("Popularity")
    legend = plt.bar(pos, numbers, color=color)
    plt.legend(legend, labels, loc="upper left", fontsize = 8)
    plt.show()

numbers = [15, 19, 10, 16, 22]
labels = ["Python", "C++", "Ruby", "Java", "HTML"]
color = ["red", "pink", "gold", "skyblue", "violet"]
pos = list(range(5))
bar_chart(numbers, labels, pos)


# 6. Creating a pie chart for programming language popularity
import matplotlib.pyplot as plt

def pie_chart():
    numbers = [22, 35, 18, 25]
    labels = ['Python', 'Ruby', 'C++', 'Java']
    colors = ["pink", "violet", "gold", "skyblue"]
    fig, ax = plt.subplots()
    ax.pie(numbers, colors=colors, autopct='%1.1f%%')
    plt.title("Popularity of different programming languages")
    plt.legend(labels, loc="lower right", title="Programs", fontsize = 8)
    plt.show()

if __name__ == '__main__':
    pie_chart()


# 7. Improved pie chart for programming language popularity
import matplotlib.pyplot as plt

def pie_chart():
    numbers = [22, 35, 18, 25]
    labels = ['Python', 'Ruby', 'C++', 'Java']
    colors = ["pink", "violet", "gold", "skyblue"]
    fig, ax = plt.subplots()
    ax.pie(numbers, colors=colors, autopct='%1.1f%%', pctdistance=1.25, labeldistance=0.6)
    plt.title("Popularity of different programming languages")
    plt.legend(labels, loc="center left", fontsize = 6)
    plt.show()

if __name__ == '__main__':
    pie_chart()


# 8. Enhanced pie chart for programming language popularity
import matplotlib.pyplot as plt

def pie_chart():
    numbers = [22, 35, 18, 25]
    labels = ['Python', 'Ruby', 'C++', 'Java']
    colors = ["pink", "violet", "gold", "skyblue"]
    explode = (0.1, 0.2, 0.0, 0.1)
    fig, ax = plt.subplots(figsize =(8, 5))
    ax.pie(numbers, colors=colors, explode=explode, autopct='%1.2f%%', shadow=True, radius=1)
    plt.legend(labels, loc="lower right", fontsize = 8)
    plt.title("Popularity of different programming languages")
    plt.show()

if __name__ == '__main__':
    pie_chart()


# 9. Pie chart for chemical composition of air
import matplotlib.pyplot as plt

def pie_chart():
    numbers = [78, 0.03, 20.9, 1.07]
    labels = ["Nitrogen", "Carbon Dioxide", "Oxygen", "Others"]
    colors = ["pink", "green", "violet", "skyblue"]
    explode = (0.1, 0.4, 0.1, 0.2)
    fig, ax = plt.subplots(figsize =(8, 5))
    ax.pie(numbers, autopct='%1.2f%%',
           labels=labels, textprops={'fontsize': 8}, pctdistance=0.6,
           colors=colors, explode=explode, startangle = 50)
    plt.title("The Chemical Composition of Air", fontsize = 12)
    plt.show()

if __name__ == '__main__':
    pie_chart()


# 10. Donut pie chart for chemical composition of air
import matplotlib.pyplot as plt

labels = ["Nitrogen", "Carbon Dioxide", "Oxygen", "Others"]
numbers = [78, 0.03, 20.9, 1.07]
colors = ["pink", "gold", "violet", "skyblue"]
plt.style.use('ggplot')
plt.title("The Chemical Composition of Air", fontsize = 12)
plt.pie(numbers, autopct='%1.2f%%', textprops={'fontsize': 8},
        colors=colors, labels=labels, startangle=50)
plt.axis("equal")

legend = plt.legend(loc="upper left", fontsize=6)
legend.get_frame().set_edgecolor('black')
legend.get_frame().set_facecolor('white')

circle = plt.Circle(xy=(0,0), radius = 0.75, facecolor="white")
plt.gca().add_artist(circle)
plt.show()


# 11. Mounting Google Drive, setting directory path, and image processing
# Mount Google Drive to access files
from google.colab import drive
drive.mount('/content/gdrive')

# Add the path to the desired folder in Google Drive to sys.path
import sys
sys.path.append('/content/gdrive/MyDrive/Colab Notebooks/img')

# Change the working directory to the desired folder in Google Drive
import os
os.chdir('/content/gdrive/MyDrive/Colab Notebooks/img')

# Image processing and edge detection
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Load the image and resize it
img = cv2.imread("flower.jpg")
img = cv2.resize(img, (140, 160))
cv2_imshow(img)

# Perform canny edge detection on the image
color_edges = cv2.Canny(img, threshold1=100, threshold2=500)
cv2_imshow(color_edges)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2_imshow(gray)

# Apply median blur to the grayscale image
gray = cv2.medianBlur(gray, 3)
cv2_imshow(gray)

# Apply adaptive thresholding to the grayscale image to detect edges
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 15)
cv2_imshow(edges)
