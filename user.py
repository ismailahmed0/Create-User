'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ismail A Ahmed
user.py
Version 4.0
'''


from tkinter import *
from tkinter import ttk


def success():
    if (usern.get() == '' or pasw.get() == '' or gender.get() == '' or type.get() == '0' or departs.get() == ''):
        # makes sure there is entry in both username/password as well as checkbox and radiobutton
        result.set("       Error") #prints to tkinter
        usern.set('') #makes username empty
        pasw.set('') #makes password empty
        departs.set('')  #makes departments empty
        gender.set('') #makes gender empty
        type.set('0') #sets usertype to offvalue, clears


    else:
        outfile = open('info.txt', 'a')
        infile = open('info.txt', 'r') # cant read a file that doesnt exist
        content = infile.readlines()
        content = [x.strip() for x in content]
        #creates a list with the users in differnet elements(have commas seperating)
        z = [i.split(' ', 1)[0] for i in content]  # gets the usernames from the "content" list and puts in a new list
        if usern.get() in z:  #checks to see if username user put in is in username list(z)
            result.set("   User exists")
            infile.close()
            usern.set('')  # makes username empty
            pasw.set('')  # makes password empty
            departs.set('')  # makes departments empty
            gender.set('')  # makes gender empty
            type.set('0')  # sets usertype to offvalue, clears
        else:
            result.set("User created")
            file = (usern.get()+' '+pasw.get()+' '+gender.get()+' '+type.get()+' '+departs.get()+'\n')
            outfile.write(file) #file will show up/update with ALL of the informaton after you close/minus the window
            outfile.close()
            usern.set('') #makes username empty
            pasw.set('') #makes password empty
            departs.set('') #makes departments empty
            gender.set('') #makes gender empty
            type.set('0') #sets usertype to offvalue, clears


def rd():
    infile = open("info.txt", 'r')
    content = infile.readlines()
    content = [x.strip() for x in content] # creates a list with the users in differnet elements(have commas seperating)
    z = [i.split(' ', 1)[0] for i in content] # gets the usernames from the "content" list and puts in a new list
    for x in z: #goes through each element(user) and prints them on seperate lines without the junk(, [] '')
        if x == usern.get(): #as it goes through each element, it checks to see if that is the username entered
            result.set(" ") #Get_s rid of NOT FOUND
            a = z.index(x) #locates the INDEX of the username(x) which has PASSWORD AND OTHER info from the "z" list
            b = [content[a]] #prints everything that is located in the username(x) index from the "content" list as list
            l = [words for segments in b for words in segments.split()]
            # this splits the string/element(has only 1) in list. before:['username999 zassword male admin Maintenance']
            # after: ['username999', 'zassword', 'male', 'admin', 'Maintenance']

            pasw.set(l[1]) # uploads the password from the 1st index which is zassword
            gender.set(l[2])
            type.set(l[3])
            departs.set(l[4])
            break # look at the for loop that doesnt have the list. if 5 users and the 2nd one is the users, three...
            # ...others are not the ones requested. if dont have break it will say NOT FOUND under the else. this...
            # ...breaks it after the user is found and doesn't go any further
        else: # look at foor loop that deosnt have the list(for x in z). this is what happens if the "x" is not the one
            result.set("NOT FOUND")
    infile.close()
root = Tk()
root.title("New User")

mainframe = ttk.Frame(root, padding="5 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

usern = StringVar()
pasw = StringVar()
gender = StringVar()
type = StringVar()
result = StringVar()
departs = StringVar()


userna = ttk.Entry(mainframe, width=10, textvariable=usern)
userna.grid(column=1, row=2, sticky=(W, E))
paswo = ttk.Entry(mainframe, width=10, textvariable=pasw, show="*")
paswo.grid(column=1, row=3, sticky=(W, E))

male = ttk.Radiobutton(mainframe, text='Male', variable=gender, value='male')
male.grid(column=1, row=4, sticky=(W,E))
female = ttk.Radiobutton(mainframe, text='Female', variable=gender, value='female')
female.grid(column=1, row=5, sticky=(W,E))

admin = ttk.Checkbutton(mainframe, text='Admin',variable=type, onvalue='admin', offvalue='0')
admin.grid(column=1, row=7, sticky=(W,E))
user = ttk.Checkbutton(mainframe, text='User',variable=type, onvalue='user', offvalue='0')
user.grid(column=1, row=8, sticky=(W,E))
guest = ttk.Checkbutton(mainframe, text='Guest', variable=type, onvalue='guest', offvalue='0')
guest.grid(column=1, row=9, sticky=(W,E))
# think of onvalue and value as kind of the same thing to understand it

nameu = ttk.Label(mainframe, text="Create User", font = ("", 15)).grid(column=1, row=1, sticky=W)
wordp = ttk.Label(mainframe, text="Username").grid(column=2, row=2, sticky=E)
ttk.Label(mainframe, text="Password").grid(column=2, row=3, sticky=E)
ttk.Label(mainframe, text="User type", font = ("", 10)).grid(column=1, row=6, sticky=W)
ttk.Button(mainframe, text="Submit", command = success).grid(column=3, row=10, sticky=W)
ttk.Button(mainframe, text="Search", command = rd).grid(column=3, row=11, sticky=W)

depar = ttk.Combobox(mainframe, textvariable=departs, state = 'readonly')
depar.grid(column=1, row=10, sticky=(W,E))
depar['values'] = ('IT', 'HR', 'Sales', 'Maintenance', 'Other')
depar.selection_clear()

ttk.Label(mainframe, textvariable=result).grid(column=3, row=9, sticky=(W,E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

userna.focus()
paswo.focus()

root.mainloop()