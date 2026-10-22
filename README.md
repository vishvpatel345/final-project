Titanic Survival Analysis

1. Project Description

This project performs Exploratory Data Analysis (EDA) on the Titanic dataset to understand the factors that influenced passenger survival.

The project uses Python, Pandas, Matplotlib, and Seaborn to analyze passenger information and create visualizations.

2. Objectives

* Explore the Titanic dataset.
* Identify missing values.
* Calculate the overall survival rate.
* Analyze survival by gender.
* Compare survival rates across passenger classes.
* Examine age distribution and survival.
* Visualize relationships between numerical variables.

3. Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn

4. Project Files

* main.py: Contains the Python source code.
* titanic.csv: Contains the Titanic passenger dataset.
* requirements.txt: Lists the required Python libraries.
* README.md: Contains project documentation and assumptions.

5. Installation

Install the required libraries using:

pip install -r requirements.txt

6. How to Run

1. Keep main.py and titanic.csv in the same folder.
2. Open a terminal in the project folder.
3. Run the following command:

python main.py

7. Analysis Performed

Data Exploration

Displays the first five rows, dataset information, missing values, and survival counts.

Missing Value Handling

Missing ages are replaced with the median age. Missing embarkation ports are replaced with the most frequent port.

Survival Analysis

Calculates the overall survival percentage and compares survival by gender, passenger class, and age group.

Visualizations

The project generates the following charts:

1. Overall survival count.
2. Survival rate by gender.
3. Survival rate by passenger class.
4. Age distribution by survival.
5. Correlation heatmap.

8. Assumptions

* Survived = 0 means the passenger did not survive.
* Survived = 1 means the passenger survived.
* Pclass represents passenger class.
* Missing ages are filled using the median age.
* Missing embarkation ports are filled using the most frequent value.
* Age groups are used to compare survival across different age ranges.
* The analysis identifies patterns and associations; it does not establish that a particular factor caused survival.

9. Expected Outcome

The program displays basic dataset information, missing values, survival statistics, and five visualizations.

The results depend on the dataset provided. A small sample dataset may not represent the full Titanic passenger population.

10. Conclusion

This project demonstrates how exploratory data analysis can be used to study passenger survival patterns. It uses statistical summaries and visualizations to compare survival by gender, passenger class, and age.
