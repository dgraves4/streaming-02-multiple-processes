# streaming-02-multiple-processes

This project showcases multiple-process streaming by providing example scripts that illustrate how multiple processes running can encounter various issues.  It also provides a custom process streaming script using an Avian Influenza csv file to simulate streaming.  The custom file also displays the use of logging and error handling. 

## Overview

This example starts a shared database and multiple processes.

The processes represent multiple users, or locations, or programs 
hitting a shared database at the same time. 

## Prerequisites

1. Git
1. Python 3.7+ (3.11+ preferred)
1. VS Code Editor
1. VS Code Extension: Python (by Microsoft)

## Imports
- csv
- socket
- time
- random
- logging (optional- can use print() functions for error handling as well)

## Task 1. Fork 

Fork this repository ("repo") into **your** GitHub account. 

## Task 2. Clone

Clone **your** new GitHub repo down to the Documents folder on your local machine. 

## Task 3. Explore

Explore your new project repo in VS Code on your local machine.

## Task 4. Execute Check Script

Execute 00_check_core.py to generate useful information.

## Task 5. Execute Multiple Processes Project Script

Execute multiple_processes.py.

Read the output. Read the code. 
Try to figure out what's going on. 

1. What libraries did we import?
1. Where do we set the TASK_DURATION_SECONDS?
1. How many functions are defined? 
1. What are the function names? 
1. In general, what does each function do? 
1. Where does the execution begin? Hint: generally at the end of the file.
1. How many processes do we start?
1. How many records does each process insert?

In this first run, we start 3 processes, 
each inserting 2 records into a shared database 
(for a total of 6 records inserted.)

In each case, the process gets a connection to the database, 
and a cursor to execute SQL statements.
It inserts a record, and exits the database quickly.

In general, we're successful and six new records get inserted. 

## Task 6. Execute Multiple Processes Script with Longer Tasks

For the second run, modify the task duration to make each task take 3 seconds. 
Hint: Look for the TODO.
Run the script again. 
With the longer tasks, we now get into trouble - 
one process will have the database open and be working on it - 
then when another process tries to do the same, it can't and 
we end up with errors. 

## Task 7. Document Results After Each Run

To clear the terminal, in the terminal window, type clear and hit enter or return. 

`clear`

To document results, clear the terminal, run the script, and paste all of the terminal contents into the output file.

Use out0.txt to document the first run. 

Use out3.txt to document the second run.

## Task 8. Create custom process streaming script

Create and configure a custom script designed to stream data from a CSV file over a network and log the process:

### Step 1: Set Up Your Python Environment
- Ensure Python 3.7+ is installed on your system.
- Optionally, set up a virtual environment to manage dependencies:

```bash
py -m venv .venv
source .venv/scripts/activate
```  

Certainly! To adapt Task 8 based on the details of your script, I'll break down the steps further into more precise and actionable instructions, ensuring that they align closely with the specific operations and structure of your custom streaming script. This step-by-step guide will be clear and detailed, making it easier for someone to understand and implement.

Revised Task 8 with Detailed Steps
markdown
Copy code
## Task 8. Create Custom Process Streaming Script

Create and configure a custom script designed to stream data from a CSV file over a network and log the process. Follow these detailed steps to replicate the functionality discussed:

### Step 1: Set Up Your Python Environment
- Ensure Python 3.7+ is installed on your system.
- Optionally, set up a virtual environment to manage dependencies:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### Step 2: Script Creation
- Open VS Code or your preferred code editor.
- Create a new file named process_streaming_yourname.py (in this example the file is process_streaming_dgraves.py).

### Step 3: Import Libraries
```bash
import csv
import socket
import time
import random
import logging
```

### Step 4: Configure Logging (optional- use print statements to console if preferred)
```bash
logging.basicConfig(filename='streaming_log.txt', filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
```
- Filemode='w' is optional - this would allow for the streaming log to be overwritten on subsequent runs.

### Step 5: Define constants
Specify the constants for network settings and file paths:

```bash
HOST = "localhost"  # Server IP address
PORT = 9999         # Listening port number
ADDRESS_TUPLE = (HOST, PORT)  # Network address
INPUT_FILE_NAME = "AvianInfluenza.csv"  # Input CSV file
OUTPUT_FILE_NAME = "out9.txt"  # Output file
```

### Step 6: Implement Data Handling Functions
Create the functions that will prepare data for transmission as well as handle streaming:

- Prepare message function:
```bash
def prepare_message_from_row(row):
    """
    Encodes a CSV row into a format suitable for network transmission.
    Returns the row as a byte string.
    """
    return f"{','.join(row)}\n".encode()
```
- Stream data function (including exception and error handling logging): 
```bash
def stream_data(input_file_name, output_file_name, address_tuple):
    """
    Streams data from a CSV file to a specified network address and simultaneously writes to an output file.
    """
    try:
        with open(input_file_name, "r") as input_file, open(output_file_name, "w") as output_file:
            reader = csv.reader(input_file)
            header = next(reader)
            output_file.write(','.join(header) + '\n')
            sock_object = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            for row in reader:
                message = prepare_message_from_row(row)
                sock_object.sendto(message, address_tuple)
                output_file.write(','.join(row) + '\n')
                output_file.flush()
                time.sleep(random.uniform(1, 3))
                logging.info(f"Sent and logged: {','.join(row)}")
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except socket.error as e:
        logging.error(f"Socket error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
## Step 7: Execute and monitor logging
Execute python process_streaming_yourname.py.  A few things will occur: 

- Files will be opened and read (r) to prepare for streaming.
- Each row from the CSV file is processed through the prepare_message_from_row function, which encodes the data into a byte format suitable for transmission over a network.
- Data will be written to an output file (in this case, 'OUTPUT_FILE_NAME is out9.txt).  In this example, an additional flush() method was included (optionally) just as a suggestion to ensure each entry is immediatley written and can be available for other processes that may be occuring.
- Logging will occur as the script operates and the output of this will log to streaming_log.txt in this example.
-  Error handling wil capture and log any issues that occur, specifically file not found and socket errors.  Any additional errors will be captured with 
 





-----

## Ensure GitHub Commands are used for version control

Throughout project when changes to scripts are made, use the following commands to push the changes to the git repository:

```bash
git add .
git commit -m "Describe your changes here"
git push origin main
```

## Helpful Information

To get more help on the early tasks, see [streaming-01-getting-started](https://github.com/denisecase/streaming-01-getting-started).

### Select All, Copy, Paste

On Windows the select all, copy, paste hotkeys are:

- CTRL a 
- CTRL c 
- CTRL v 

On a Mac the select all, copy, paste hotkeys are:

- Command a
- Command c
- Command v

Detailed copy/paste instructions (as needed)

1. To use these keys to transfer your output into a file, 
clear the terminal, run the script, then click in the terminal to make it active.
1. To select all terminal content, hold CTRL and the 'a' key together. 
1. To copy the selected content, hold CTRL and the 'c' key together. 
1. To paste, open the destination file (e.g. out0.py) for editing.
1. Click somewhere in the destination file to make it the active window.
1. Now hit CTRL a (both together) to select all of the destination file.
1. Hit CTRL v (both together) to paste the content from your clipboard.

Do a web search to find helpful videos on anything that seems confusing
and share them in our discussion.

### Reading Error Messages

Python has pretty helpful error messages. 
When you get an error, read them carefully. 

- What error do you get?

### Database Is Locked Error

Do a web search on the sqlite3 'database is locked' error.

- What do you learn?
- Once a process fails, it crashes the main process and everything stops. 

### Deadlock

Deadlock is a special kind of locking issue where a process 
is waiting on a resource or process, that is waiting also. 

Rather than crashing, a system in deadlock may wait indefinitely, 
with no process able to move forward and make progress.

### Learn More

Check out Wikipedia's article on deadlock and other sources to learn how to prevent and avoid locking issues in concurrent processes. 
