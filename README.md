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

### Explanation of model choice, including benefits and limitations

- Random Forest vs. Logistic regression:
In the context of low-dimensional data (i.e., when the number of covariates is small compared to the sample size), logistic regression is considered a standard approach for binary classification. 

In this project, we focus on prediction rather than explanation, giving the dataset we have. Logistic regression is preferred.


- SVM vs. Logistic regression:
Logistic regression works with the identified independent variable, while SVM works well with unstructured and semi-structured data like text and images. 
Logistic regression is used to solve classification problems based on a statistical approach, while SVM is used for both classification and regression based on geometrical properties of the data. 

In this project, we identified “income” as the independent variable. Predicting one’s income is greater than 50K or less than 50K based on these features: age, hours-per-week,  education, marital-status, work-class,  occupation, sex, relationship, race.  
It is a two-class classification problem. As such, Logistic regression is preferred.


- The benefits of using logistic regression are that it has good accuracy for simple datasets. It performs well when the dataset is linearly separable(in our case, greater than 50K or less than 50K).
 However, logistic regression is vulnerable to overfitting and outliers. 


### Preliminary model evaluation
Run our models with the same train test split, comparison the balanced accuracy score and precision, result as below:
                      | Balanced accuracy score  | Precision     |
 ---------------------|------------------------- |-------------- |
 SVM                  |0.7478                    |0.8372         |
 ---------------------|--------------------------|---------------|
 Logistic Regression  |0.7534                    |0.8396         |
----------------------|--------------------------|---------------|
 Random Forest        |0.74                      |0.81           |
 ---------------------|--------------------------|---------------|


Our best scores are with Logistic Regression with a balanced accuracy score of 0.75 and precision of 0.84.

### List of tables
Income_Table - contains the columns listed in the description of data source.
