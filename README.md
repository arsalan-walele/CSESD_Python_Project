# CSESD_Python_Project
# Personal Expense Tracker

This is a command-line Python application to track personal expenses. The program allows users to add expenses, view their recorded expenses, and calculate the total amount spent.

## Features

- **Add Expense**: Allows the user to input details of a new expense, such as date, category, description, and amount. The expense is saved to a CSV file.
- **View Expenses**: Displays all recorded expenses along with the total amount spent.
- **Persistent Storage**: Expenses are saved in a CSV file (`expenses.csv`), which is created automatically if it doesn't already exist.

## Requirements

- Python 3.x
- No additional libraries are required besides Python's standard library.

## How to Use

1. **Running the Program**:  
   To start the expense tracker, run the script using Python.  
   ```
   python expense_tracker.py
   ```

2. **Menu Options**:  
   After running the program, you will see a menu with three options:
   - **1**: Add a new expense.
   - **2**: View all expenses.
   - **3**: Exit the program.

3. **Adding an Expense**:  
   When selecting option 1, you will be prompted to enter:
   - The **date** of the expense (in YYYY-MM-DD format).
   - The **category** of the expense (e.g., Food, Transport, Bills).
   - A **description** of the expense.
   - The **amount** spent.

   After entering the details, the expense will be saved in the `expenses.csv` file.

4. **Viewing Expenses**:  
   Selecting option 2 will display a list of all recorded expenses, showing:
   - Date
   - Category
   - Description
   - Amount

   At the end of the list, the program will display the **total amount spent**.

5. **Exit**:  
   Choosing option 3 will exit the application.

## File Structure

The application uses a CSV file (`expenses.csv`) to store the expenses, with the following columns:
- `Date`: The date of the expense (YYYY-MM-DD).
- `Category`: The category of the expense (e.g., Food, Transport).
- `Description`: A description of the expense.
- `Amount`: The amount spent.

If the file doesn't exist, the program will automatically create it with the necessary headers.

## Example Usage

### Adding an expense
```
Enter the date (YYYY-MM-DD): 2024-12-25
Enter the category (e.g., Food, Transport, Bills): Food
Enter a description: Dinner at restaurant
Enter the amount: 50.75
Expense added successfully.
```

### Viewing expenses
```
Date           Category       Description             Amount    
-----------------------------------------------------------------
2024-12-25     Food           Dinner at restaurant    50.75     
-----------------------------------------------------------------
Total expenses: 50.75
```

## Troubleshooting

- **FileNotFoundError**: If you encounter a "File not found" error, it means no expenses have been recorded yet. The file will be created automatically the first time you add an expense.
  
- **Invalid amount**: If you enter a non-numeric value for the amount, an error message will prompt you to enter a valid number.

## License

This project is open-source.
