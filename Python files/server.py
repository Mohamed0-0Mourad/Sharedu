#___________________________________________Youssef_______________________________________________________#
def mood():
         print('/'*35,'Mode 1 is for a Sender - Mode 2 is for a Receiver','\\'*40)
         mood=int(input("Please,Enter either 1 or 2 according to purpose of use: "))

         while mood!=1 and mood!=2:
              mood=int(input('Please,Enter only either 1 or 2 according to purpose of use'))
         return mood

def greetings():
    name= input('Enter your Name Please: ')
    print(f'Hi,{name}, Glad To Meet You :-)')
    return name

def getip_port(server_name, mode):
      if mode == 1:
            ipaddress=str(input('Enter the Ip address of host device: '))    
            port_host=str(input('Enter the port number of the app: '))
            file= open(f"{server_name}.txt", 'w')
            file.write(f"ip:{ipaddress},port:{port_host}\n")
            file.close()
            return ipaddress, port_host
      else:
            while True:
                  server= input("Enter the name of the server you want to connect to: ")
                  try:
                        file = open(f"{server}.txt", 'r')
                        break
                  except FileNotFoundError:
                        print("Error, the server you're trying to reach isn't in our database! ")
                        continue
            ip = input("Enter the ip address of the server: ")
            port = input("Enter the port number of the server: ")
            for line in file:
                  det = line.split(',')
                  ser_ip = det[0].split(':')
                  ser_port = det[1].split(':')
                  while ser_ip[1] != ip or int(ser_port[1]) != int(port):
                        print("Error!\nSome of the details you've entered is wrong, contact your server and make sure.")
                        ip = input("Enter the ip address of the server: ")
                        port = input("Enter the port number of the server: ")
                  break                                                #Because we need to iterate only one line !
            return server

def hintaya():
        print('/'*35,'Before Proceeding !!!!!','\\'*35)
        trans_hint=input('Do you want  to learn more about Transport layer protocols ? y/n  :-) ')
        while trans_hint.lower() not in ("y", "n"):
                  trans_hint= input('Inalid Entry!! Do you want  to learn more about Transport layer protocols ? y/n  :-)  ')
        network_hint=input('Do you want  to learn more about Network layer protocols ? y/n  :-) ')
        while network_hint.lower() not in ("y", "n"):
                  trans_hint= input('Inalid Entry!! Do you want  to learn more about Network layer protocols ? y/n  :-)  ')
                  if trans_hint=='y':
                        print(' '*35,'TCP vs. UDP in a Nutshell',' '*35)
                        print(' '*35,'Imagine you are sending a birthday card to a friend',' '*35)
                        print(' '*30,'TCP\n','Carefully checks your address and recipients address',
                        'Makes sure the card arrives in perfect order, page by page data packets.'
                        'If a page gets lost, the postman goes back and re-delivers it.'
                        'Takes a bit longer due to all the checking and re-sending.'
                              'Great for important messages like emails, bank transfers, or downloading files.\n\n')
                        print(' '*30,'UDP\n','Throws the card without checking the address too closely.'
                              'Just hurls it over the fence and hopes it gets there (sends data packets quickly).'
                              'Doesnt bother checking if it arrives or is in order.'
                              'Super fast, but you may not get the card at all, or it might be missing pages.'
                              'Perfect for things where speed matters more than perfect delivery, like streaming videos, online games, or live broadcasts.\n\n')
                        
                  elif network_hint=='y':
                        print('Imagine the internet is a giant city! Every house in the city has a unique address to help people and packages find them. \nIn the internet world, these addresses are called IP addresses.\n\n')
                        print(' '*20,'IPV4','\nThink of IPV4 like the older houses in the city. They have addresses like 123.45.67.89. These addresses work well, but the city is growing fast! There are just not enough unique 4-digit addresses for all the new houses (websites and devices).\n\n')
                        print('\n '*20,'IPV6','IPV6 is like the new part of the city, with modern apartment buildings. These addresses are longer and more complex, like 2001:0db8:85a3:0000:0000:8a2e:0370:7334. They may seem confusing, but they have space for many, many more new homes, so nobody gets lost!')   

def sendr(mode, server_name , filenames=None, ipaddress= None, port_host=None, user= None):
    if mode == 1:
            transportlayer= input('Choose Either using,''TCP'',or ,''UDP'',Protocol: ')
            while  transportlayer.lower() not in ("tcp", "udp"):
                  transportlayer= input('Inalid Entry!! Please,Choose Either using,''TCP'',or ,''UDP'',Protocol: ')
            networklayer= input('Choose Either using,''IPV4'',or ,''IPV6'',Protocol: ')
            while  networklayer.lower() not in ("ipv4", "ipv6"):
                  networklayer= input('Inalid Entry!! Please,Choose Either using,''IPV4'',or ,''IPV6'',Protocol: ')
            print('-'*90)
            print(f'Creating Socket with {ipaddress} and {port_host}')   
            print(f'Slicing {filenames} and decoding them.....................')      
            print('-'*90)
            recepints= input('Please Enter the  authorized Receivers list who can receive files\nFor example "youssef mohamed, mohamed sherbini" : ').split(', ')
            file= open(f'authorized_users_{server_name}.txt', 'a')
            for uu in recepints:
                file.write(f'{uu}\n')
            file.close()
            print('\n',' '*100)
    else:
          authorized = False
          file = open(f"authorized_users_{server_name}.txt", 'r')
          while authorized == False:
                  for line in file:
                        auth_users = line.strip()
                        if user.lower() == auth_users.lower():
                              authorized = True
                              break
                  
                  if authorized == False:
                        user = input("Sorry you're not authorised to enter this server!.\n"
                                     "Please Re-enter your authorized username by sender correctly: ")
          file.close()

def getfilename(server_name):
     filenames= input('Seperated by commas and with thier extensions. Please Enter Your fileS name like for example (sheet programming.pdf, lecture 2.mp4)\n(Please make sure that the file you are sharing is in the same directory of the app)\n').split(', ')
     filesizes= input("Enter the file sizes with the unit beside \nFor example '43.5 MB, 2.4 GB': ").split(', ')
     removalfilenames=input('Do you to remove an input from the filenames list before proceeding? y/n: ')
     removalfilesizes=input('Do you to remove an input from the filesizes list before proceeding? y/n: ')
     if removalfilenames=='y':
           filenames.remove(input('Enetr the name to remove: '))
           print(f'Removed')
     if removalfilesizes=='y':
           filesizes.remove(float(input('Enter the size to remove: ')))  
           print(f'Removed')
     file = open(f"{server_name}.txt", "a")
     for i in range (len(filesizes)):
                file.write(f"{filenames[i]},{filesizes[i]}\n")

     return filenames
