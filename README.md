# Project_Team_2

### Project Overview:
The purpose of this project is to demonstrate the various coding languages we have learned over the course of the Bootcamp by using a dataset, building a machine learning model to provide a prediction, and visualizing the results for users.

### Selected Topic:
Predicting user income level based on the following features:

### Description of Data Source:
Our datasource comes from kaggle: https://www.kaggle.com/lodetomasi1995/income-classification

The Data Source contains information on age, workclass, final weight (total number of people represented in row), education level, marital status, occupation, familial relationship, race, gender, capital gain, capital loss, hours worked per week, and native country.

### Database Engine
Postgres - to be used for data cleaning

### List of tables
Income_Table - contains the columns listed in the description of data source.

## Machine Learning Model

### Data-processing
1.	Find and drop total of 2399 missing data. Remaining 30162 rows of data for our machine learning model.
2.	Drop unnecessary columns: "fnlwgt", "education-num", "capital-gain", "capital-loss".
3.	Using `One-Hot Encoding` to fit and transform categorical variables.
4.	Using `StandardScaler` module standardizes the data so that the mean of each feature is 0 and standard deviation is 1.

### Features used in the model
- Age: Current age (in years)
- Workclass: Employment status of an individual (e.g.	Private)
- Education: Highest degree obtained (e.g. HS-grad, Bachelors)
- Marital-status: Marital status of an individual (e.g. Divorced, Married-AF-spouse)
- Occupation: Industry/role employed in (e.g. Exec-managerial, Craft-repair)
- Relationship: Represents what this individual is relative to others(e.g. Husband, Wife)
- Race: Descriptions of an individual’s race (e.g. White, Black)
- Sex: Gender assigned at birth (Male/Female)
- Hours-per-week: Weekly hours employed (e.g. 40)
- Native-country: Country of origin for an individual

### Training and testing dataset
Using Scikit-learn's `train_test_split` module to split 75% of features (X) and target (y) data into training data and 25% for testing data.

### Explanation of model choice, including benefits and limitations

- Random Forest vs. Logistic regression:

In the context of low-dimensional data (i.e., when the number of covariates is small compared to the sample size), logistic regression is considered a standard approach for binary classification. 

In this project, we focus on prediction rather than explanation, giving the dataset we have, Logistic regression is preferred.


- SVM vs. Logistic regression:

Logistic regression works with the identified independent variable, while SVM works well with unstructured and semi-structured data like text and images. 

Logistic regression is used to solve classification problems based on a statistical approach, while SVM is used for both classification and regression based on geometrical properties of the data. 

In this project, we identified “income” as the independent variable. Predicting one’s income is greater than 50K or less than 50K based on these features: age, hours-per-week,  education, marital-status, work-class,  occupation, sex, relationship, race.  
It is a two-class classification problem. As such, Logistic regression is preferred.


- The benefits of using logistic regression are that it has good accuracy for simple datasets. It performs well when the dataset is linearly separable(in our case, greater than 50K or less than 50K).
 However, logistic regression is vulnerable to overfitting and outliers. 


### Preliminary model evaluation
Run our models with the same train test split, comparison the balanced accuracy score and precision, result as below:

 Models               |Balanced accuracy score   |Precision      |
 ---------------------|------------------------- |-------------- |
 SVM                  |0.7478                    |0.8372         |
 Logistic Regression  |0.7534                    |0.8396         |
 Random Forest        |0.74                      |0.81           |
 
Our best scores are with Logistic Regression with a balanced accuracy score of 0.75 and precision of 0.84.

