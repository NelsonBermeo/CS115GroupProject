'''
Names: Team 4: Nelson Burmeo, Taygan Gillespie, Angel Velasquez, Samantha York
Pledge: I pledge my honor that I have abided by the Stevens Honor System
CS 115 - Group Project 
'''

import os
import itertools

userDict = {}
artists = []
name_list = []


def starting_function():
  '''This function takes no input and returns no output, the point of the function is to run at the beginning
of every time this program is run. It would check if a file exists and if it does it would correct all the
data in the file. Else this would create the file'''
  if os.path.exists('musicrecplus.txt') == True:
      file = open('musicrecplus.txt', 'r')
      for line in file:
          if ':' not in line:
              pass
          elif '\n' not in line:
              colon_index = line.index(':')
              userName = line[:colon_index]
              userList = line[colon_index+1:].split(',')
              userList2 = list(map(lambda x: x.title(),userList))
              userList3 = list(map(lambda x: x.strip(),userList2))
              userList3.sort()
              userDict[userName] = userList3
          else:
              dash_index = line.index('\n')
              colon_index = line.index(':')
              userName = line[:colon_index]
              userList = line[colon_index+1:dash_index].split(',')
              userList2 = list(map(lambda x: x.title(),userList))
              userList3 = list(map(lambda x: x.strip(),userList2))
              userList3.sort()
              userDict[userName] = userList3                       
      pass
  else:
      file_builder = open('musicrecplus.txt', 'w+')
      file_builder.close()
      pass




def menu():
   '''This function takes no input and returns no output. This function is a part of the starting function
as shows the menu to the user and calls a function based on the user's input'''
   valid = ["e", "r", "p", "h", "m", "q", "d", "s"]
   choice = input('''Enter a letter to choose an option:
e - Enter preferences
r - Get recommendations
p - Show most popular artists
h - How popular is the most popular
m - Which user has the most likes
q - Save and quit
s - Show preferences
d - delete preferences
''')
   if choice in valid:
       if choice == "e":
          enterPreferences()
          menu()
       if choice == "r":
         recs1(reccomendation(name_list[0]))
         menu()
       if choice == "q":
          save_quit()
       if choice == "p":
         getPopular()
         menu()
       if choice == "m":
         GetMostLikes()
         menu()
       if choice == "h":
         howPopular()
         menu()
       if choice == "s":
         showPreferences()
         menu()
       if choice == 'd':
         deletePreferences()
         menu()
   else:
       menu()


       
def initial_prefs():
  '''This function takes in no argument and has no output. The point of this function is to take in prefs from a user
in the very start of program if the user doesn't exist (the existing part is a part of another function but this function is run
if the user does not exist). If the user tries to input a duplicate artist, they will be alerted'''
  newPref = input('Please Enter the name of an artist or band that you like: ' )
  while newPref != '':
      if newPref.strip().title() in artists:
          print("You have already inputted this artist, Please Enter a new artist or press enter to continue")
          newPref = input("Enter Here " )
      else:
          artists.append(newPref.strip().title())
          newPref = input('''Enter an artist that you like (Enter to finish):
''')
  pass




def start():
  '''This is the start of the entire program function and it takes in no input and gives out no output. This function
greets the user and either allows the user to interact with the menu if the user has used the program before (their name
matches one already in the data) or adds their data and then allows the user to interact with the menu if they have
not used the program before'''
  name = input('''Enter your name (put a $ symbol after your name if you wish your preferences to remain private):
''').title() #####
  name_list.append(name)
  starting_function()
  if name in userDict:
      menu()
      pass
  else:
      initial_prefs()
      artists.sort()
      artist_string = ','.join(artists)
      file_builder = open('musicrecplus.txt', 'a')
      file_builder.write('\n' + name + ':' + artist_string)
      file_builder.close()
      userDict[name] = artists
      menu()
      pass




################################################################# Nelson's Functions


def reccomendation(name):
  '''This is the start of the reccomendation function and takes in the name of the user using the program and outputs
the user which has the closest taste to them. There are multiple if, elif and else statements to account for multiple
cases including, same length relations, $ users, comparing the user to themselves and more.'''
  bestuser = None
  bestscore = 0
  for user in userDict.keys():
      if user[-1] == '$':
          pass
      elif userDict[user] == userDict[name]:
          pass
      elif rec_helper(userDict[user], userDict[name]) == True:
          pass
      else:
          score = match_length(userDict[user], userDict[name])
          if score >= bestscore and bestuser != None:
              if score >= bestscore and len(userDict[user]) > len(userDict[bestuser]):
                  bestscore = score
                  bestuser = user
          elif score > bestscore:
              bestscore = score
              bestuser = user
          else:
              pass      
  return bestuser


def rec_helper(one, two):
  '''Helper function for reccomendation which takes in two lists and returns True if the first list has each index
in it also in the other list'''
  count = 0
  for i in one:
      if i in two:
          count += 1
  if count == len(one):
      return True
  return False


   
def match_length(l1,l2):
  '''This is the match length function from the textbook and takes in two lists and returns the count of matching
indexes that the lists share without using the in command'''
  l1.sort()
  l2.sort()
  matches = 0
  x = 0
  y = 0
  while x < len(l1) and y < len(l2):
      if l1[x] == l2[y]:
          matches += 1
          x += 1
          y += 1
      elif l1[x] < l2[y]:
          x += 1
      else:
          y += 1
  return matches




def recs1(other_user):
  '''This function takes the other_user which comes from the reccomendation function and this user has the most similarities
of artists as the actual user and this function returns the list of artists in the other_user's prefs which the actual
user does not have in their prefs (aka the reccomendations'''
  if len(userDict) == 1:
      print("No recommendations available at this time.")
  elif other_user == None:


      print("No recommendations available at this time.")
  else:
      your_list = userDict[name_list[0]]
      their_list = userDict[other_user]
      new_list = []
      x = 0
      y = 0
      while x < len(your_list) and y < len(their_list):
          if your_list[x] == their_list[y]:
              x += 1
              y += 1
          elif your_list[x] < their_list[y]:
              x += 1
          else:
              new_list.append(their_list[y])
              y += 1
      for i in their_list[y:]:
         new_list.append(i)
      for name in new_list:
         print(name) 
    


################################################################# Nelson's Reccomendation
################################################################# Taygan's Functions


def enterPreferences():
  '''This function takes no input or output but it allows the user to change their preferences which affects the file and
dictionary'''
  #userDict[name_list[0]] = []
  newPref = input("Enter your name(put a $ symbol after your name if you wish your preferences to remain private)")
  while newPref != '':
      if newPref.strip().title() in userDict[name_list[0]]:
          print("You have already added this artist, Please Enter a new artist or press enter to continue")
          newPref = input("Enter Here " )
      else:
          userDict[name_list[0]].append(newPref.strip().title())
          newPref = input('''Enter an artist that you like (Enter to finish):
''')
  save_preferences_to_file()
  pass




def save_preferences_to_file():
  '''This function takes no input or gives an output, but it writes the some update to the file'''
  global userDict
  with open("musicrecplus.txt", "w") as file:
      for user, preferences in userDict.items():
          file.write(f"{user}: {', '.join(preferences)}\n")




def save_quit():
  '''This function takes no input or gives an output, but this function writes the most up to date data into the file
and exits the shell'''
  with open("musicrecplus.txt", "w") as file:
      for user, preferences in userDict.items():
          toSave = f"{user}:{','.join(preferences)}\n"
          file.write(toSave)
  exit()  # Exit the program after saving




def deletePreferences():
  '''Takes in no input and returns no output, but it takes out data in the dictionary and in the file to
delete artist the user wants to from their prefs'''
  global userDict, artists, name_list
  if name_list and name_list[0] in userDict:
       user_preferences = userDict[name_list[0]]
       if user_preferences:
           index = 1 ###Represents index of current preference in user_preferences list###
           while index <= len(user_preferences):
               print(f"{index}. {user_preferences[index - 1]}") ### gets preference at current index ###
               index += 1




           choice = input("Please enter the number of the preference you would like to delete (Press Enter to Continue): ")




           if choice.strip() and choice.isdigit():
                   choice = int(choice)
                   if 1 <= choice <= len(user_preferences):
                       deleted_artist = user_preferences.pop(choice-1)
                       print(f"{deleted_artist} has been deleted from your preferences!")




                       save_preferences_to_file()




################################################################# Taygan's Functions


def sorted_dic():
  '''Takes in no input and returns a dictionary of all the artists and how many times each appeared in the
entire data set'''
  ArtistDump = []
  for i in userDict.keys():
     if i[-1] == "$":
        pass
     else:
        for a in userDict[i]:
           ArtistDump.append(a)                               
  PopularityDic = {}
  Count = 0
  for CurrentCheckingArtist in ArtistDump:
      if CurrentCheckingArtist not in PopularityDic:
          for Copies in ArtistDump:
              if (CurrentCheckingArtist == Copies):
                  Count += 1
          PopularityDic[CurrentCheckingArtist] = Count
          Count = 0
  return dict(sorted(PopularityDic.items(), key=lambda x:x[1]))
  
################################################################# Angel's Functions


def getPopular():
  '''This function takes in no input and outputs nothing but prints the artist who are the most popular'''
  sort_dic = sorted_dic()
  if len(sort_dic) == 0 or list(sort_dic.keys()) == ['']:
      print("Sorry, no artists found")
  elif len(sort_dic) == 1:
      one = list(sort_dic)[0]
      print(one)
  elif len(sort_dic) == 2:
      one = list(sort_dic)[-1]
      two = list(sort_dic)[-2]
      print(one)
      print(two)
  else:
      one = list(sort_dic)[-1]
      two = list(sort_dic)[-2]
      three = list(sort_dic)[-3]
      print(one)
      print(two)
      print(three)
   
def GetMostLikes():
  '''This function takes in no input and outputs nothing but prints the user who has the most items in their prefs'''
  ScrapeList = userDict.items()
  MostLiked = 0
  Users = []
  for CurrentUser in ScrapeList:
      if CurrentUser[0][-1] == "$":
          pass
      elif (len(CurrentUser[1]) > MostLiked):
          MostLiked = len(CurrentUser[1])
          Users = [CurrentUser[0]]
      elif (len(CurrentUser[1]) == MostLiked):
          Users += [CurrentUser[0]]
  for User in Users:
      print(User)
   
############################################### Angel's Functions
      
########################### Samantha #######################


def howPopular():
     '''Takes in no input and outputs nothing, but used the sorted dictionary of all values to print the
number of times the most popular artist appeared in the data (how popular the artist is)'''
     sort_dic = sorted_dic()
     if sort_dic == {}:
        print("Sorry, no artists found")
     elif list(sort_dic.keys()) == ['']:
        print("Sorry, no artists found")
     else:
        last_index = list(sort_dic)[-1]
        print(sort_dic[last_index])
     pass


def showPreferences():
  '''Takes in no input and outputs nothing, but prints the user's preferences'''
  for name in userDict[name_list[0]]:
      print(name)

start()
