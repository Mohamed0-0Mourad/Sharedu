#__________________________________________ IMPORTS _____________________________________________________
import server
import download 
import add

# from turtle import*
# speed(100)
# width(20)
# penup()
# goto(0,-100)
# pendown()
# lt(45)
# for i in range(5):
    # penup()
    # fd(i*50)
    # lt(90)
    # pendown()
    # circle(i*50,90)
    # penup()
    # lt(90)
    # fd(i*50)
    # lt(90)
# hideturtle

mood = server.mood()
#_______________________________________SERVER SCRIPT______________________________________________
if mood == 1:
    user = server.greetings()
    server_name = input("Enter a name to assign to your server (You must save it to give it to with whom you share with): ")
    ip, port = server.getip_port(server_name, mood)
    print('-'*90)
    files_name = server.getfilename(server_name)
    server.hintaya()
    server.sendr(mood, server_name, filenames=files_name, ipaddress=ip, port_host= port)
    
    while True: 
        again = download.any_else()
        if not again:
            break
    
    feed = input('Would you like to rate us? y/n: ')
    if feed == 'y': add.feedback(user)

#_____________________________________CLIENT SCRIPT______________________________________________
else:
    user = server.greetings()
    server_name = server.getip_port(user, mood)
    server.sendr(mood, server_name, user= user)
    download.lister(server_name)
    
    files_name = input("(seperated by space & with extension)\nEnter the name of the fileS you want to download: ").strip().split()
    for file in files_name:
        add.scan_virus(file)
        size_MB = download.download_file(server_name, file)
        download.record(file, f"{size_MB} MB")

    download.record(mode='display')
    while True: 
        again = download.any_else()
        if not again:
            break

    feed = input('Would you like to rate us? y/n: ')
    if feed == 'y': 
        add.feedback(user)
        print('-'*90)
        print("Thank you for your rate\nAppreciated!")
