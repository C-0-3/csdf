import os
import time
 
# Function to simulate creating files
def create_files(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
   
    for i in range(150):
        file_path = os.path.join(directory, f"malicious_file_{i}.txt")
        with open(file_path, 'w') as file:
            file.write(f"Kya Bolti Public, Machayege, joh nahi naachte unko bhi nachayege {i}.")
        print(f"Created: {file_path}")
 
if _name_ == "_main_":
    test_directory = "./test_malware_simulation"
   
    print("Simulating malicious behavior...")
    create_files(test_directory)
   
    print("Wakey Wakey, You have been Hacked, Love you too.")
