# Sales Data Cleaning Project
This project converts a messy sales dataset to a cleaned version, which is saved in a new CSV file, helping business easily tracking its operation.
# Description
This project uses the data in sales_data_raw.csv, converting into a cleaned version in sales_data_clean.csv. The script in data_cleaning.py provides the steps through the cleaning process, which include:
- Load the raw sales data file.
- Standardize column names (lowercase, underscores)
- Clean string columns (strip whitespace, convert to lowercase, and remove quotes)
- Handle missing values (fill missing qty with the column mean, round the values to integer, and drop rows missing prodname or date)
- Remove invalid data (rows with negative price or qty)
- Save the cleaned dataset to sales_data_clean.csv
# Run Instructions
- Have Python installed
- Install required packages (pandas): pip install pandas
- Navigate to the project root folder
- Run the cleaning script: python src/data_cleaning.py
- Check the cleaned CSV file in sales_data_clean.csv
