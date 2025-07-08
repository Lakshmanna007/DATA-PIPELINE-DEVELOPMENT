# DATA-PIPELINE-DEVELOPMENT

"COMPANY":CODTECH IT SOLUTIONS

"NAME":T LAKSHMANNA

"Intern ID": CT06DF463

"DOMAIN": Data Science

"DURATION": 6 WEEKS

"MENTOR": NEELA SANTHOSH

# ETL Pipeline Project

## Description:
An automated ETL pipeline using Python, Pandas, and Scikit-learn that:
- Extracts CSV data
- Handles missing values
- Encodes categorical variables
- Scales numeric features
- Saves the processed data

## 🎯 Objectives

The main goals of this project are:

- To read raw data from a CSV file
- To clean the data by handling missing values
- To convert categorical values into numerical formats (label encoding)
- To scale numerical features for uniformity
- To output a clean and ready-to-use dataset into a new CSV file
- 
## 🧰 Technologies Used

- **Python 3.8+**
- **Pandas** – for data loading, manipulation, and storage
- **Scikit-learn** – for preprocessing tools like `SimpleImputer`, `LabelEncoder`, and `StandardScaler`

## How to Run:
1. Place `input_data.csv` in the same folder.
2. Run: `python etl_pipeline.py`
3. Output: `processed_data.csv` will be generated
   
## OUT PUT
Loading data...

Raw Data Preview:
       name   age  gender   salary
0    Alice  25.0  Female  50000.0
1      Bob   NaN    Male  60000.0
2  Charlie  30.0    Male      NaN
3    David  28.0    Male  52000.0
4      Eve  27.0  Female  58000.0
Handling missing values...
Encoding categorical values...
Scaling features...

Processed Data Preview:
       name       age  gender    salary
0    Alice -1.550434       0 -1.355815
1      Bob  0.000000       1  1.355815
2  Charlie  1.550434       1  0.000000
3    David  0.310087       1 -0.813489
4      Eve -0.310087       0  0.813489
Saving processed data...
Data saved successfully to processed_data.csv
