# Math Skills
Redo of the math-skills project in order to practice python

This Python script reads a list of numbers from a text file, calculates basic statistical measures, and prints the results. The calculated statistics include:

- **Average (Mean)**
- **Median**
- **Variance**
- **Standard Deviation**

## Requirements

- Python 3.x

## Usage

1. Create a text file named `data.txt` in the same directory as the script.
2. Add numbers to the file, separated by spaces or new lines.
3. Run the script:
```bash
python3 main.py
```

## Output
The program outputs the following statistics:

- Average: The mean of the integers.
- Median: The middle value of the sorted integers.
- Variance: The measure of spread in the integers.
- Standard Deviation: The square root of the variance.

### Example Output :
```bash
Average: 19952.163366336634
Median: 148.5
Variance: 19507974375.918453
Standard Deviation: 139670.95036520105
```

## File Format
The data.txt file should contain numerical values separated by spaces or new lines.

### Example :
```bash
10 20 30 40 50
```
or
```bash
10
20
30
40
50
```

## Error Handling

- If the file does not exist, the script will output: `"File not found."`
- If the file is empty or contains invalid data, it will output: `"File is empty or contains invalid numbers."`
- If there are non-numeric values, it will output: `"File contains invalid data"`

## Dependencies

This script uses Python's built-in `statistics` module, so no external dependencies are required.

## Author
S. Cointin

## License

This project is licensed under the GPL 3.0 License.
