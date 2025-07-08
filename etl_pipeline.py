# etl_pipeline.py

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler

# 1. EXTRACT
def load_data(file_path):
    print("Loading data...")
    df = pd.read_csv(file_path)
    return df

# 2. TRANSFORM
def preprocess_data(df):
    print("Handling missing values...")
    imputer = SimpleImputer(strategy='mean')
    df[['age', 'salary']] = imputer.fit_transform(df[['age', 'salary']])

    print("Encoding categorical values...")
    label_encoder = LabelEncoder()
    df['gender'] = label_encoder.fit_transform(df['gender'])

    print("Scaling features...")
    scaler = StandardScaler()
    df[['age', 'salary']] = scaler.fit_transform(df[['age', 'salary']])

    return df

# 3. LOAD
def save_data(df, output_path):
    print("Saving processed data...")
    df.to_csv(output_path, index=False)
    print("Data saved successfully to", output_path)

# Main function
def run_etl():
    input_file = "input_data.csv"
    output_file = "processed_data.csv"

    df = load_data(input_file)
    print("\nRaw Data Preview:\n", df.head())

    processed_df = preprocess_data(df)
    print("\nProcessed Data Preview:\n", processed_df.head())

    save_data(processed_df, output_file)

if __name__ == "__main__":
    run_etl()
    
