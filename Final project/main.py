import pandas as pd
import matplotlib.pyplot as plt
import os
import statistics as stats
import csv
import random


# Load Data Function
def load_data(file_path):
    """Load population data from CSV file or create a new file if not found."""
    if not os.path.exists(file_path):
        print(f"{file_path} not found. Creating a new file.")
        with open(file_path, 'w') as f:
            f.write("region,year,population,growth_rate\n")  # Add headers
        return []
    else:
        dataList = []
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                dataList.append(row) 
        return dataList

# Standardize Data Function
def standardize_data(data_list):
    """Standardize data fields (e.g., region names to title case)."""
    # TODO: Implement standardization for region names, population, and growth_rate fields
    for i in data_list:
        i['region'] = i['region'].title()
        i['population'] = int(i['population'])
        i['growth_rate'] = float(i['growth_rate'])

# Display Instructions Function
def display_instructions():
    """
    Print user instructions for using the Population Statistics Calculator.
    """
    print("Welcome to the Population Statistics Calculator.")
    print("Options:\n- Add data\n- Calculate statistics\n- Filter data\n- Visualize data\n- Save changes")

# Add Sample Entries Function
def add_sample_entries(data_list):
    """Add sample population data entries to the data list for testing purposes."""
    # TODO: Add at least 10 sample entries with region, year, population, and growth_rate
    inpt = input("Do you want to manually add 10 sample entries, or do you want them randomly generated? (manual/random): ")
    if inpt == "manual":
        for i in range(10):
            add_population_data(data_list)
    elif inpt == "random":
        for i in range(10):
            region = "Region " + chr(random.randint(65, 90))
            while any(region == i['region'] for i in data_list):
                region = "Region " + chr(random.randint(65, 90)) + chr(random.randint(65, 90))
                
            
            year = str(random.randint(1995, 2024))
            population = str(random.randint(100000, 1000000))
            growth_rate = str(round(1 + random.random(), 2))
            data_list.append({'region': region, 'year': year, 'population': population, 'growth_rate': growth_rate})
    standardize_data(data_list)

# Additional Operations Functions
def add_population_data(data_list):
    """Add a new population data entry."""
    region = input("Enter region: ")
    year = input("Enter year: ")
    population = input("Enter population: ")
    growth_rate = input("Enter growth rate: ")
    print(f"Added data for {region} in {year}. The population is {population} with a growth rate of {growth_rate}.")
    data_list.append({'region': region, 'year': year, 'population': population, 'growth_rate': growth_rate})

#Calculates statistics for the attribute
def calculate_statistics(data_list, attribute):
    """Calculate mean, median, mode, and standard deviation for population data."""
    if attribute.lower() == "population":
        data = [int(i['population']) for i in data_list]
        mean = stats.mean(data)
        median = stats.median(data)
        mode = stats.mode(data)
        std_dev = stats.stdev(data)
        return mean, median, mode, std_dev
    elif attribute.lower() == "growth rate":
        data = [float(i['growth_rate']) for i in data_list]
        mean = stats.mean(data)
        median = stats.median(data)
        mode = stats.mode(data)
        std_dev = stats.stdev(data)
        return mean, median, mode, std_dev
    else:
        print("Invalid attribute. Please enter 'population' or 'growth rate'.")
        return

#Prints out statistics for the attribute
def print_statistics(mean, median, mode, std_dev):
    """Print the calculated statistics for the attribute."""
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {std_dev}")

#Filters out data based on region or year
def filter_data(data_list, filter_type, value):
    """Filter data by a specific attribute, like region or year."""
    # TODO: Implement filtering functionality for region or year
    if filter_type.lower() == "region":
        filtered_data = [i for i in data_list if i['region'] == value]
        return filtered_data
    elif filter_type.lower() == "year":
        filtered_data = [i for i in data_list if i['year'] == value]
        return filtered_data
    else:
        print("Invalid filter type. Please enter 'region' or 'year'.")
        return

# Save Data Function
def save_data(file_path, data_list):
    """Save the updated data list to the CSV file."""
    with open(file_path, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['region', 'year', 'population', 'growth_rate'])
        writer.writeheader()
        for row in data_list:
            writer.writerow(row)    

# Visualization Function
def visualize_population_trend(data_list):
    """Visualize population distribution by year or growth trend over time."""
        # TODO: Create a bar chart, line graph, or histogram for population or growth rate trends
    inpt = input("Do you want to visualize population distribution by year or growth trend over time? (year/growth): ")
    if inpt == "year":
        for i in data_list:
            plt.plot(i['year'], int(i['population']))
        plt.title("Population Distribution by Year")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.show()
    elif inpt == "growth":
        for i in data_list:
            plt.plot(i['year'], float(i['growth_rate']))
        plt.title("Growth Trend Over Time")
        plt.xlabel("Year")
        plt.ylabel("Growth Rate")
        plt.show()


# Main Program Loop
def main():
    file_path = 'population_data.csv'  # The .csv file containing population data
    data_list = load_data(file_path)
    display_instructions()

    while True:
        print("\nMenu:")
        print("1. Add Population Data")
        print("2. Calculate Statistics")
        print("3. Filter Data")
        print("4. Add Sample Entries")
        print("5. Visualize Population Trend")
        print("6. Save and Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_population_data(data_list)
        elif choice == '2':
            attribute = input("Enter attribute for statistics (e.g., population): ")
            calculate_statistics(data_list, attribute)
        elif choice == '3':
            filter_type = input("Filter by (region or year): ")
            value = input(f"Enter {filter_type} to filter by: ")
            filter_data(data_list, filter_type, value)
        elif choice == '4':
            add_sample_entries(data_list)
        elif choice == '5':
            visualize_population_trend(data_list)
        elif choice == '6':
            save_data(file_path, data_list)
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()