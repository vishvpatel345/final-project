import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Load the Titanic dataset

data = pd.read_csv(“titanic.csv”)

Display basic information

print(“First 5 rows:”)
print(data.head())

print(”\nDataset Information:”)
print(data.info())

print(”\nMissing Values:”)
print(data.isnull().sum())

print(”\nSurvival Count:”)
print(data[“Survived”].value_counts())

Handle missing values

data[“Age”] = data[“Age”].fillna(data[“Age”].median())

data[“Embarked”] = data[“Embarked”].fillna(
data[“Embarked”].mode()[0]
)

Calculate survival percentage

survival_rate = data[“Survived”].mean() * 100
print(”\nOverall Survival Rate:”, round(survival_rate, 2), “%”)

Survival by gender

print(”\nSurvival by Gender:”)
print(data.groupby(“Sex”)[“Survived”].mean() * 100)

Survival by passenger class

print(”\nSurvival by Passenger Class:”)
print(data.groupby(“Pclass”)[“Survived”].mean() * 100)

Survival by age group

data[“AgeGroup”] = pd.cut(
data[“Age”],
bins=[0, 12, 18, 35, 60, 100],
labels=[“Child”, “Teenager”, “Young Adult”, “Adult”, “Senior”],
include_lowest=True
)

print(”\nSurvival by Age Group:”)
print(data.groupby(“AgeGroup”, observed=False)[“Survived”].mean() * 100)

Visualization 1: Overall survival count

sns.countplot(data=data, x=“Survived”)
plt.title(“Titanic Survival Count”)
plt.xlabel(“Survived (0 = No, 1 = Yes)”)
plt.ylabel(“Number of Passengers”)
plt.tight_layout()
plt.show()

Visualization 2: Survival by gender

sns.barplot(data=data, x=“Sex”, y=“Survived”)
plt.title(“Survival Rate by Gender”)
plt.xlabel(“Gender”)
plt.ylabel(“Survival Rate”)
plt.tight_layout()
plt.show()

Visualization 3: Survival by passenger class

sns.barplot(data=data, x=“Pclass”, y=“Survived”)
plt.title(“Survival Rate by Passenger Class”)
plt.xlabel(“Passenger Class”)
plt.ylabel(“Survival Rate”)
plt.tight_layout()
plt.show()

Visualization 4: Age distribution

sns.histplot(data=data, x=“Age”, hue=“Survived”, bins=20)
plt.title(“Age Distribution by Survival”)
plt.xlabel(“Age”)
plt.ylabel(“Number of Passengers”)
plt.tight_layout()
plt.show()

Visualization 5: Correlation heatmap

numeric_data = data.select_dtypes(include=“number”)

sns.heatmap(numeric_data.corr(), annot=True, cmap=“coolwarm”)
plt.title(“Titanic Dataset Correlation”)
plt.tight_layout()
plt.show()

print(”\nTitanic Survival Analysis Completed!”)