# CheeseBurger: Subdomain Scanner and Juicy File Finder

CheeseBurger is a powerful tool designed for security enthusiasts and penetration testers. With CheeseBurger, users can streamline their reconnaissance process, making it easier to identify potential vulnerabilities and gather information for further security assessments.

## Features

-   Capture full-page screenshots of active subdomains.
-   Enumerate and screenshot specified files (referred to as "juicy files").
-   Progress tracking with a loading bar in the terminal.
-   Headless mode support for running the script in environments without a display.
	
## Requirements

-   Python 3.x
-   Required Python libraries:
    -   `requests`
    -   `selenium`
    -   `webdriver_manager`
    -   `colorama`

You can install the necessary libraries using pip:

bash

Copy codeScreenshot Capture Tool

`pip install requests selenium webdriver-manager colorama` 

## Usage

To use the script, run it from the command line with the required parameters:

bash

Copy code

`CheeseBurger --subdomain=<file_subdomains.txt> --screenshot=<folder_screenshots> --protocol=<http/https> --juicy=<file1,file2 or sub-dir1, sub-dir2...>` 

### Parameters

-   `--subdomain=<file_subdomains.txt>`: Path to the text file containing subdomains (one per line).
-   `--screenshot=<folder_screenshots>`: Path to the folder where screenshots will be saved.
-   `--protocol=<http/https>`: The protocol to use for the URLs (must be either `http` or `https`).
-   `--juicy=<file1,file2,...>`: Comma-separated list of files to enumerate on each subdomain.

### Example

bash

Copy code

`CheeseBurger --subdomain=subdomains.txt --screenshot=screenshots --protocol=https --juicy=admin.php,login.html` 

## How It Works

1.  **Initialization**: The script initializes necessary libraries and checks for command-line arguments.
2.  **Subdomain Checking**: It reads the provided subdomain file and checks which subdomains are active.
3.  **Screenshot Capture**: For each active subdomain, it captures a screenshot of the main page and any specified juicy files.
4.  **Progress Indication**: A loading bar is displayed in the terminal to indicate the progress of the operation.

## Error Handling

The script includes basic error handling:

-   If a specified subdomain file is not found, an error message is displayed.
-   If a subdomain is not accessible, a message is shown indicating that the subdomain is inactive.
-   If the script is interrupted by the user, a message is printed.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for improvements.

## Author

[Your Name](https://your-website.com)  
Your Email

## Version: 1.0.0