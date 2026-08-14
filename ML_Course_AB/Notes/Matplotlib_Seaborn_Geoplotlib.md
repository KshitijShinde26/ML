# Applied Machine Learning Notes - Part: Visualization Libraries

# Matplotlib

## Definition

Matplotlib is a Python library used for creating line plots, bar charts,
scatter plots, histograms, pie charts, and other visualizations.

### Common Functions

-   plt.plot()
-   plt.bar()
-   plt.scatter()
-   plt.hist()
-   plt.pie()
-   plt.show()

### Example

``` python
import matplotlib.pyplot as plt

x=[1,2,3]
y=[2,4,6]
plt.plot(x,y)
plt.show()
```

# Seaborn

## Definition

Seaborn is built on top of Matplotlib and is mainly used for statistical
visualization.

### Common Plots

-   Heatmap
-   Pairplot
-   Boxplot
-   Violin Plot
-   Count Plot

### Example

``` python
import seaborn as sns
tips=sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=tips)
```

# Geoplotlib

## Definition

Geoplotlib is used for geographic data visualization on maps.

### Applications

-   GPS tracking
-   Population mapping
-   Crime mapping
-   Traffic analysis

### Example

``` python
from geoplotlib.utils import read_csv
import geoplotlib

data = read_csv("locations.csv")
geoplotlib.dot(data)
geoplotlib.show()
```

# Comparison

  Library      Purpose
  ------------ --------------------------
  Matplotlib   General plotting
  Seaborn      Statistical plots
  Geoplotlib   Geographic visualization

# Viva Questions

1.  What is Matplotlib?
2.  Why is Seaborn preferred?
3.  What is Geoplotlib?
