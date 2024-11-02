import os
import subprocess
import shutil

def main():
    # Step 1: Get the input file from the user
    input_file = input("Enter the path of your input file: ")
    output_file = "all_responses.txt"
    output_dir = "httpx_responses"
    
    # Step 2: Run httpx-toolkit with no color
    print("Running httpx-toolkit...")
    httpx_command = [
        "httpx-toolkit", "-l", input_file, "-sc", "--no-color", "-o", output_file
    ]
    subprocess.run(httpx_command, check=True)
    
    # Step 3: Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Step 4: Define filter commands
    filters = {
        "httpx_200.txt": r"\[200\]",
        "httpx_30x.txt": r"\[30[0-9]\]",
        "httpx_40x.txt": r"\[40[0-9]\]",
        "httpx_50x.txt": r"\[50[0-9]\]"
    }
    
    # Step 5: Filter and create files based on status codes
    print("Filtering responses by status code...")
    for filename, pattern in filters.items():
        with open(filename, "w") as outfile:
            grep_command = ["grep", pattern, output_file]
            subprocess.run(grep_command, stdout=outfile)
    
    # Step 6: Move the filtered files into the output directory
    print("Moving filtered files to directory:", output_dir)
    for filename in filters.keys():
        shutil.move(filename, os.path.join(output_dir, filename))

    print("Process complete. Check the '{}' directory for results.".format(output_dir))

if __name__ == "__main__":
    main()
