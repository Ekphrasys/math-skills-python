import statistics

def read_numbers_from_file(file_path):
    # Reads numbers from a text file
    with open(file_path, 'r') as file:
        # Read the content of the file
        content = file.read()
        # Extract numbers and convert to a list of floats
        numbers = list(map(float, content.split()))
    return numbers

def calculate_statistics(numbers):
    """Calculates and returns average, median, variance, and standard deviation."""
    average = sum(numbers) / len(numbers)
    median = statistics.median(numbers)
    variance = statistics.variance(numbers)
    std_dev = statistics.stdev(numbers)
    return average, median, variance, std_dev

def main():
    file_path = "./data.txt"
    try:
        numbers = read_numbers_from_file(file_path)
        if not numbers:
            print("File is empty or contains invalid numbers.")
            return
        
        # Calculate statistics
        avg, med, var, std_dev = calculate_statistics(numbers)
        
        # Display the results
        print(f"Average: {avg}")
        print(f"Median: {med}")
        print(f"Variance: {var}")
        print(f"Standard Deviation: {std_dev}")
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("File contains invalid data")

if __name__ == "__main__":
    main()
