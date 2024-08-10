# Playwright Test for SDET Challenge

This repository contains a Playwright test script written in Python for the website [http://sdetchallenge.fetch.com/](http://sdetchallenge.fetch.com/). The test script interacts with the webpage, fills in input values, performs a weighing operation, and takes different actions based on the results.

## Prerequisites

Before running the test, ensure that you have the following installed on your machine:

- Python 3.7 or later
- Pip (Python package installer)

## Setup Instructions

### 1. Clone the Repository
`git clone https://github.com/AndiWilson/Automation-Challenge-Fetch.git`
`cd test/playwright`

### 2. Install the Required Packages
Use pip to install Playwright and any other dependencies:
`pip install playwright`

### 3. Install Playwright Browsers
`playwright install`

## Running the test
Once the setup is complete, you can run the test using the following command (BEST UI VIEWING EXPERIENCE)

`pytest --browser webkit --headed --slowmo=500`

This command will:

Launch a Chromium browser instance.
Navigate to the SDET challenge webpage.
Fill in the input fields with predefined values.
Perform the weighing operation.
Take appropriate actions based on the result (e.g., resetting the scale and reweighing, testing success, and error messages).

## Understanding the Test Script
The main test logic is located in the test_scale.py file. It includes:

Filling Input Values: The script fills the left and right input fields with predefined numbers.
Performing Weighing: It simulates the weighing operation by clicking the "Weigh" button.
Decision Logic: Based on the weighing results, the script decides whether to reset the scale, adjust weights, or verify specific messages.

## Troubleshooting
If you encounter issues when running the test, consider the following:

Ensure that you have the correct version of Python installed.
Verify that all dependencies are installed by running pip install -r requirements.txt (create this file if necessary).
Ensure that the website http://sdetchallenge.fetch.com/ is accessible and functional.

