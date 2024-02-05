import time
import sys
# import dir_path

def display_message(submit, operation):                         #mohamed sherbini
    if submit:
      message = f"{operation} Succeeded!"
    else: 
      message = f"{operation} Failed, Please try again."
    print('-'*90)
    print(message)

def unit(size: str):                                           #Mohamed Sherbini
    det = size.split()
    det[0] = float(det[0])
    if det[1].upper() == 'B':
        size_MB = det[0]/(1024*1024)
    elif det[1].upper() == 'KB':
        size_MB = det[0]/1024
    elif det[1].upper() == 'MB':
        size_MB = det[0]
    elif det[1].upper() == 'GB':
        size_MB = det[0]*1024
    elif det[1].upper() == 'TB':
        size_MB = det[0]*1024*1024
    return float(size_MB)

def any_else():                                                             #mohamed shirbini
  import add
  # Checks if there are more services client wants to make
  answer = input("Do you want another service? If yes type yes, if no just type no thanks: ")

 # If yes choose the service, if no just type no thanks
  if answer == "yes":
    service = input("Choose the service you want (download, compress, or convert): ")
    if service == "download":
        download_file()
        return True
    elif service == "compress":
        add.compress(input("Enter the name of the file you want to compress (With extension): "))
        return True
    elif service == "convert":
        add.converter(input("Enter the name of the file you want to convert (With extension): "))
        return True  
  # If no, closes the connection
  elif answer == "no thanks":
    print("Thank you for using our app!")
    return False
  # If invalid input, prints an error message
  else:
    print("Invalid input. Please enter yes or no thanks.")
    return True

def download_file(server_name, file_name):                         #Mohamed Shirbini
    
    file = open(f"{server_name}.txt", "r")
    found = False
    for line in file:
        # file = file_name.read()
        details = line.split(',')
        if file_name == details[0]:
            found = True
            size_MB = unit(details[1])
            progress(size_MB)
    if found:
        downloaded = open(f"{file_name}", 'w')
        downloaded.close()
        display_message(True, 'Download')
    else:
        display_message(False, 'Download') 
        print("Error! file not found")
    file.close()
    return size_MB

def progress(file_size: float):                                   #mohamed sherbini
  # Initialize some variables
  start_time = time.time()
  current_size = 0
  speed = 0
  bar_length = 50

  # Loop until the file size is reached
  while current_size < file_size:
    # Simulate some file transfer
    current_size += 1
    time.sleep(0.01)

    # Calculate the speed and the percentage
    elapsed_time = time.time() - start_time
    speed = current_size / elapsed_time
    percentage = current_size / file_size

    # Create the progress bar and the speed meter
    bar = "#" * int(bar_length * percentage) + " " * (bar_length - int(bar_length * percentage))
    meter = f"{speed:.2f} MB/s"

    # Print the progress bar and the speed meter
    sys.stdout.write(f"\r[{bar}] {percentage * 100:.2f}% {meter}")
    sys.stdout.flush()

  # Print a new line at the end
  print()

def lister(server_name: str):                                    #Mohamed Mourad
  contents = open(f"{server_name}.txt", 'r')
  dict= {'Document' : ['pdf', 'docx', 'pptx', 'csv', 'txt', 'xsls'], 'Picture' : ['jpg', 'jpeg', 'png'],'Video' : ['mp4', 'mov', 'gif'], 'Music':['mp3'], 'Program': ['exe', 'deb'], 'Archieve': ['zip', 'rar', 'rar5', 'tar.gz', 'tar', 'iso']}
  file_type = 'Details'

  print('_'*90)
  print(f"%51s"%'Server Files')
  print('_'*90)
  print(f"%-40s%-40s%-40s"%('File name', 'Type', 'Size'))
  print('_'*90)
  
  for line in contents:
    file_det = line.strip().split(',')
    file_name = file_det[0].split('.')
    
    for type in dict:                           # loop on dictionary to get the type by extension
      if file_name[1] in dict[type]:            # if extension in the values
        file_type = type
    
    print(f"%-40s%-40s%-10s"%(file_det[0],file_type,file_det[1]))
    print('_'*90)
  contents.close()


def record(file_name: str = None, file_size: str = None, mode= None):                           #Mohamed Mourad 
  dict= {'Document' : ['pdf', 'docx', 'pptx', 'csv', 'txt', 'xsls'], 'Picture' : ['jpg', 'jpeg', 'png'],'Video' : ['mp4', 'mov', 'gif'], 'Music':['mp3'], 'Program': ['exe', 'deb'], 'Archieve':['zip', 'rar', 'rar5', 'tar.gz', 'tar', 'iso']}
  if mode == None:
    file = open("history.txt", 'a')
    file.write(f"{file_name},{file_size}\n")
    file.close()
  elif mode == 'display':
    print('_'*90)
    print(f"%48s"%'History')
    print('_'*90)
    print(f"%-40s%-40s%-40s"%('File name', 'Type', 'Size'))
    print('_'*90)
    file = open("history.txt", "r")
    
    for line in file:
      list = line.strip().split(',')
      ext = list[0].split('.')
      
      for type in dict:
        if ext[1] in dict[type]:
          ext[1]= type
      print(f"%-40s%-40s%-10s "%(list[0],ext[1],list[1]))
      print('_'*90)
    file.close()
