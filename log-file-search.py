import os
import glob

def main():
    # OUTPUT PATH CONFIGURATION - Modify this path as needed
    OUTPUT_PATH = r"C:\SearchResults"  # Change this to your desired output directory
    
    print("=== Log File Search Program ===")
    print("This program searches for a word/string in all log files within a folder.\n")
    
    # 1. Get the folder path from user
    while True:
        folder_path = input("Enter the path to the Windows folder to search: ").strip()
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            break
        else:
            print("Error: The specified path does not exist or is not a directory. Please try again.")
    
    # 2. Get the output file name from user
    output_filename = input("Enter the name for the output text file (without .txt extension): ").strip()
    if not output_filename.endswith('.txt'):
        output_filename += '.txt'
    
    # Use the configured output path
    output_folder = r"C:\Users\Administrator\Desktop"
    
    # Create output directory if it doesn't exist
    try:
        os.makedirs(output_folder, exist_ok=True)
    except Exception as e:
        print(f"Error creating output directory: {e}")
        return
    
    output_path = os.path.join(output_folder, output_filename)
    
    # Create the empty output file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            pass  # Creates empty file
        print(f"Output file created: {output_path}")
    except Exception as e:
        print(f"Error creating output file: {e}")
        return
    
    # 3. Get the search term from user
    search_term = input("Enter the word or string to search for: ").strip()
    if not search_term:
        print("Error: Search term cannot be empty.")
        return
    
    print(f"\nSearching for '{search_term}' in all log files in '{folder_path}'...")
    print("=" * 60)
    
    # Initialize counter
    total_matches = 0
    files_processed = 0
    
    # Get all log files in the folder
    log_files = glob.glob(os.path.join(folder_path, "*.log"))
    
    if not log_files:
        print("No .log files found in the specified folder.")
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write("No .log files found in the specified folder.\n")
        print("Program has ended.")
        return
    
    # Open output file for writing
    try:
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(f"Search Results for: '{search_term}'\n")
            output_file.write(f"Searched in folder: {folder_path}\n")
            output_file.write("=" * 60 + "\n\n")
            
            # Process each log file
            for file_path in log_files:
                files_processed += 1
                filename = os.path.basename(file_path)
                print(f"Processing: {filename}")
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as input_file:
                        line_number = 0
                        file_matches = 0
                        
                        for line in input_file:
                            line_number += 1
                            # Check if search term is in the line (case-insensitive)
                            if search_term.lower() in line.lower():
                                total_matches += 1
                                file_matches += 1
                                
                                # Write the matching line to output file
                                output_file.write(f"File: {filename} (Line {line_number})\n")
                                output_file.write(f"{line.rstrip()}\n")
                                output_file.write("-" * 40 + "\n")
                        
                        if file_matches > 0:
                            print(f"  Found {file_matches} match(es) in {filename}")
                
                except Exception as e:
                    print(f"  Error reading {filename}: {e}")
                    output_file.write(f"Error reading file {filename}: {e}\n")
                    output_file.write("-" * 40 + "\n")
            
            # Write summary to output file
            output_file.write(f"\nSEARCH SUMMARY:\n")
            output_file.write(f"Files processed: {files_processed}\n")
            output_file.write(f"Total matches found: {total_matches}\n")
            
            # Handle case where no results were found
            if total_matches == 0:
                output_file.write("\nNo results were found.\n")
    
    except Exception as e:
        print(f"Error writing to output file: {e}")
        return
    
    # Inform user of results
    print("\n" + "=" * 60)
    if total_matches > 0:
        print(f"Search complete! Found {total_matches} match(es) across {files_processed} file(s).")
        print(f"Results are available in: {output_path}")
    else:
        print("Search complete! No results were found.")
        print(f"'No results were found.' has been written to: {output_path}")
    
    print("\nProgram has ended.")

if __name__ == "__main__":
    main()