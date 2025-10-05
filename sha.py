#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File Hasher Utility (SHA256)

A command-line tool to calculate the SHA256 hash of a local file.
It reads the file in chunks to handle very large files without
consuming excessive memory, making it ideal for verifying downloads.
"""

import hashlib
import argparse
import os

# --- Constants ---
# The size of the chunks (in bytes) to read from the file.
CHUNK_SIZE = 65536  # 64KB

def calculate_sha256(filepath: str) -> str | None:
    """
    Calculates the SHA256 hash digest for the specified file.

    Args:
        filepath: The full path to the file.

    Returns:
        The hexadecimal hash digest as a string, or None if an error occurs.
    """
    # Initialize the SHA256 hash object
    sha256_hash = hashlib.sha256()

    try:
        # Open the file in binary read mode ('rb')
        with open(filepath, 'rb') as f:
            # Loop to read file in chunks until the end is reached
            while True:
                data = f.read(CHUNK_SIZE)
                # If no more data is read, break the loop
                if not data:
                    break
                # Update the hash object with the current chunk of data
                sha256_hash.update(data)

        # Return the final hash digest in hexadecimal format
        return sha256_hash.hexdigest()

    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: File not found at '{filepath}'")
        return None
    except IOError as e:
        # Handle other potential I/O errors (e.g., permissions)
        print(f"Error reading file '{filepath}': {e}")
        return None

if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser(
        description="Calculate the SHA256 hash of a file.",
        epilog="Example: python file_hasher.py /path/to/your/file.zip"
    )

    # Add the required argument for the file path
    parser.add_argument(
        "file_path",
        type=str,
        help="The path to the file to be hashed."
    )

    # Parse the arguments provided by the user
    args = parser.parse_args()
    target_file = args.file_path

    print(f"Target File: {target_file}")
    
    # Check if the file path actually exists before processing
    if not os.path.exists(target_file):
        print("Error: The provided path does not exist.")
        exit(1)

    print("Calculating hash... Please wait.")
    
    # Calculate and retrieve the hash
    file_hash = calculate_sha256(target_file)

    # Output the result
    if file_hash:
        print("\n" + "="*70)
        print(f"SHA256 Digest: {file_hash}")
        print("="*70 + "\n")
    else:
        # Exits with an error code if hashing failed (e.g., I/O error)
        exit(1)

