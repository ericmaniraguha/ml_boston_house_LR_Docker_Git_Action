## Boston Housing Dataset Analysis - Machine Learning - Linear Regression - Docker - Github Action

This project aims to analyze the Boston Housing Dataset using machine learning techniques for regression analysis.

## Part I

## Overview

The Boston Housing Dataset is a widely used dataset in machine learning for regression analysis. It contains information collected by the U.S Census Service concerning housing in the area of Boston, Massachusetts. The dataset includes various features such as per capita crime rate, average number of rooms per dwelling, and median value of owner-occupied homes. The target variable is the median value of owner-occupied homes in $1000's.

## Data Loading and Preprocessing

1. The dataset is loaded using pandas' `read_csv()` function from a CSV file named `BostonHousing.csv`.
2. Data preprocessing steps include handling missing values (if any), scaling the features using `StandardScaler`, and splitting the dataset into training and testing sets.

## Analysis and Modeling

1. Exploratory Data Analysis (EDA) is performed to understand the distribution and relationships between features.
2. Linear Regression is chosen as the modeling technique due to its simplicity and interpretability.
3. The Linear Regression model is trained on the training dataset and evaluated using Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip`.
3. Run the Jupyter Notebook or Python script to analyze the dataset and train the regression model.

## Files Included

- `BostonHousing.csv`: CSV file containing the Boston Housing Dataset.
- `analysis.ipynb`: Jupyter Notebook containing the analysis code.
- `requirements.txt`: Text file listing the required dependencies.

## Results

The trained Linear Regression model achieves the following performance metrics on the test set:

- Mean Absolute Error (MAE): X
- Mean Squared Error (MSE): Y
- Root Mean Squared Error (RMSE): Z

## Conclusion

The analysis of the Boston Housing Dataset provides insights into the factors affecting housing prices in the area. The trained Linear Regression model can be used to make predictions on new data and gain further understanding of the housing market.

## References

- [UCI Machine Learning Repository: Boston Housing Dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/housing/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)

## Part II

## Requirements

To run the code in this project, you need the following dependencies:

- Python 3.x
- scikit-learn
- pandas
- matplotlib
- seaborn

You can install these dependencies using pip:

```bash
pip install scikit-learn pandas matplotlib seaborn
```

## Tools Overview

1. **GitHub:**

   - Web-based platform for version control using Git.
   - Hosting for software development and collaboration.
   - Features include pull requests, issue tracking, and project management tools.

2. **Heroku:**

   - Cloud platform as a service (PaaS) for building, deploying, and managing applications.
   - Supports multiple programming languages and frameworks.
   - Provides automatic scaling, continuous integration, and add-ons for various services.

3. **Git CLI:**
   - Command-line tool for interacting with Git repositories.
   - Performs version control operations such as cloning, adding files, committing changes, and managing branches.
   - Widely used for efficient management of Git repositories from the command line.

## Create a new environment

```
conda create -n venv python=3.7 -ycon
```
