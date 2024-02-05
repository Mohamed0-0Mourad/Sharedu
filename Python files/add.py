from download import display_message
#______________________________________________________Mohamed Mourad____________________________________________________

def converter(file_name:str):
    det = file_name.split('.')
    dict= {'txt' : ['pdf', 'docx', 'pptx', 'csv', 'txt', 'xsls'], 'img' : ['jpg', 'jpeg', 'png'],'vid' : ['mp4', 'mov', 'gif'], 'program':['exe'], 'archieve':['zip', 'rar', 'rar5', 'tar.gz', 'tar', 'iso']}

    for form in dict:
        if det[1] in dict[form]:       #detiticts if the current file form is in the database or not
            print('-'*90)
            to = input(f"You are downloading a {det[1]} file\n"
                       f"To which extension do you want to convert your file from the available list\n{dict[form]}\n").strip()
            
            if to in dict[form]:      #detictis whether the requested form is available
                convered_file = open(f"{det[0]}.{to}", 'a')         #creats the converted file 
                convered_file.close()
                display_message(True, 'Convertion')
            else:
                display_message(False, 'Convertion')
                yes = input(f"Sorry the file you're converting to ({to}) is not supported yet\nWe're sending it to our developers to work on!\n"
                        "Do you agree to share an information about ONLY the type of file you're downloading and your contact to inform you? (y,n)\n")
                if yes == 'y':
                    feed_file = open("feedback.txt", 'a')
                    try:
                        feed_file.write(f"convert,{det[1]},{to}\n")
                    except: continue
                    feed_file.close()

def compress(file_name:str):
    files_list= [file_name]
    while True:
        plus = input(f"Is there other fileS you would like to add to the compressed file? (y/n)\n").strip()
        if plus== 'y':
            another_file = input("seperated by commas and with extensions\nEnter the fileS name (with its extension): ").strip()
            files_list.append(another_file)
        elif plus == 'n': break
        else : print("Error! please enter only 'y' or 'n'")
    
    
    ext = ['zip', 'rar', 'rar5', 'tar.gz', 'tar', 'iso']
    to = input(f"To which extension do you want to convert your file from the available list\n{ext}\n")
    new_name = input("Enter the new name of the compressed file without extension: ").strip() + f".{to}"
    #Creates the zipped file 
    compressed = open(f"{new_name}", 'w')
    compressed.close()
    display_message(True, "Compression")
    

def feedback(user_name:str):
    rate = input("Rate us from 5: ")
    hate = input("What did you dislike about our app?\n")
    like = input("What did you like in our app?\n")
    feedback = input("Is there any other things you would like to add?\n")
    feed_file = open('feedback.txt', 'a')
    feed_file.write(f"user name,{user_name}\nrate,{rate}\nlikes,{like}\nhates,{hate}\nadditional,{feedback}\n")        

def scan_virus(file_name: str):
    # Simulate a virus scan (replace this with your actual virus scanning logic)
    is_safe = check_virus(file_name)

    if is_safe:
        print(f"{file_name} is safe. Continue.")
    else:
        print(f"{file_name} is not safe. Stopping download and deleting from server.")
        delete_file(file_name)

def check_virus(file_name: str) -> bool:
    # Replace this with your actual virus scanning logic
    # For demonstration purposes, let's assume all files are safe
    return True

def delete_file(file_name: str):
    # Add logic here to delete the file from the server
    # For demonstration purposes, let's print a message
    print(f"Deleting {file_name} from the server.")
