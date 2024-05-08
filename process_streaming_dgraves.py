import csv
import socket
import time
import random
import logging

# Use logging module from standard library, and update the logging configuration to overwrite the old log file on each run using filemode='w'
logging.basicConfig(filename='streaming_log.txt', filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for network communication
HOST = "localhost"  # The IP address of the server where data will be sent
PORT = 9999         # The port number on which the server is listening
ADDRESS_TUPLE = (HOST, PORT)  # Tuple used by the socket for addressing

# File paths for the input and output data
INPUT_FILE_NAME = "AvianInfluenza.csv"  # CSV file containing the data to be streamed
OUTPUT_FILE_NAME = "out9.txt"  # File where the streamed data will be written

# Function to prepare a message from a CSV row
def prepare_message_from_row(row):
    """
    Encodes a CSV row into a format suitable for network transmission.
    Returns the row as a byte string.
    """
    return f"{','.join(row)}\n".encode()

# Function to stream data from a CSV file to a network and write to a file
def stream_data(input_file_name, output_file_name, address_tuple):
    """
    Streams data from a CSV file to a specified network address and simultaneously writes to an output file.
    """
    try:
        # Opening the input CSV file for reading and output file for writing
        with open(input_file_name, "r") as input_file, open(output_file_name, "w") as output_file:
            reader = csv.reader(input_file)
            header = next(reader)  # Read the header row
            output_file.write(','.join(header) + '\n')  # Write the header to the output file

            # Create the socket object for UDP communication
            sock_object = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            # Read and process each row from the CSV file
            for row in reader:
                message = prepare_message_from_row(row)
                sock_object.sendto(message, address_tuple)  # Send the message over the network
                output_file.write(','.join(row) + '\n')  # Write the same data to the output file
                output_file.flush()  # Ensure data is immediately written to the file system
                time.sleep(random.uniform(1, 3))  # Introduce a random delay to simulate streaming
                logging.info(f"Sent and logged: {','.join(row)}")  # Log the action

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")  # Log if the input file is not found
    except socket.error as e:
        logging.error(f"Socket error: {e}")  # Log if there is a network-related error
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")  # Catch-all for any other errors

if __name__ == "__main__":   # If this is the script we are running (not imported as a module), then run it!
    logging.info("Starting data streaming.")  # Log that the data streaming process has begun
    stream_data(INPUT_FILE_NAME, OUTPUT_FILE_NAME, ADDRESS_TUPLE)  # Call the stream_data function with the specified input file, output file, and network address
    logging.info("Streaming complete!")  # Log that streaming is complete
