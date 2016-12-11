'''
Introduction to Software Engineering, Team 3 | Project 3
@Team_Members: Team Members: Jonathan Sanchez
Date: December 9th, 2016
'''

''' IMPORTS '''
from tkinter import *
import random
import datetime
import sys
import math
from database import cursor, conn
''' IMPORTS '''

# DEFINE COLORS
bgclr="#282828"
fgclr="#cecece"
clr='#004a95'

''' BUTTON FUNCTIONS '''
def validateTicketEntry_BUTTON(ticket_id):
    # Check to see if the ticket ID is in the database
    cursor.execute('SELECT ticket_id FROM ticket WHERE ticket_id LIKE {}'.format(ticket_id))
    check = str(cursor.fetchall())
    
    # Get validated status from database
    cursor.execute("""
                   SELECT validated from denton.ticket
                   WHERE ticket_id = %s
                   """, (ticket_id,))
    row = cursor.fetchone()
    validation = (row[0])
    
    # If the ticket EXISTS in the database
    if (validation == 'Y' ):
        print('Ticket ID Invalid.')
        ticket_id_invalid_label = Label(root, text='Status: INVALID', bg='red')
        ticket_id_invalid_label.place(x=0, y=160, anchor="w")
        ticket_id_invalid_label.config(font=("Courier", 10))
        ticket_id_invalid_label.after(10000, ticket_id_invalid_label.destroy)
        
    elif (check != '[]'):
        print('\nTicket ID Valid.\n')
        ticket_id_valid_label = Label(root, text='Status: VALID  ', bg='green')
        ticket_id_valid_label.place(x=0, y=160, anchor="w")
        ticket_id_valid_label.config(font=("Courier", 10))
        ticket_id_valid_label.after(10000, ticket_id_valid_label.destroy)
    
        # Update time out to database
        timeOut(ticket_id)
            
        # Calculate cost
        cost(ticket_id)
        
    # If the ticket ID is NOT in the system, create new ticket.
    else:
        print('Ticket ID Invalid.')
        ticket_id_invalid_label = Label(root, text='Status: INVALID', bg='red')
        ticket_id_invalid_label.place(x=0, y=160, anchor="w")
        ticket_id_invalid_label.config(font=("Courier", 10))
        ticket_id_invalid_label.after(10000, ticket_id_valid_label.destroy)
        
def createTicket_BUTTON():
    print("Creating Ticket")
    createValidID()
    
def displayTicketInformation(ticket_id, date, time):
    # Print Ticket Information onto the system
    ticket_id_label = Label(root, text='Ticket ID: {}'.format(ticket_id))
    ticket_id_label.place(x=0, y=60, anchor="w")
    ticket_id_label.config(font=("Courier", 10))
    ticket_id_label.after(10000, ticket_id_label.destroy)
    
    time_entered_label = Label(root, text='Entered Time: {}'.format(time))
    time_entered_label.place(x=300, y=60, anchor="center")
    time_entered_label.config(font=("Courier", 10))
    time_entered_label.after(10000,time_entered_label.destroy)
    
    date_label = Label(root, text='Date: {}'.format(date))
    date_label.place(x=450, y=60, anchor="w")
    date_label.config(font=("Courier", 10))
    date_label.after(10000, date_label.destroy)
    
def validateMembershipID_BUTTON(membership_id):
    cursor.execute('SELECT membership_id FROM subscription WHERE membership_id LIKE {}'.format(membership_id))
    check = str(cursor.fetchall())
    
    # If the ticket EXISTS in the database
    if(check != '[]'):
        print("Membership Found")
        # Member Status
        member_status_label = Label(root, text="Status: Member Found    ", bg='green')
        member_status_label.place(x=0, y=200, anchor="w")
        member_status_label.config(font=("Courier", 10))
        member_status_label.after(10000, member_status_label.destroy)
        
        checkMembership(membership_id)
        
    else:
        print("Invalid Membership ID")
        member_status_label = Label(root, text="Status: Member Not Found", bg='red')
        member_status_label.place(x=0, y=200, anchor="w")
        member_status_label.config(font=("Courier", 10))
        
        name_label = Label(root, text="                      ")
        name_label.place(x=0, y=270, anchor="w")
        name_label.config(font=("Courier", 10))
        
        # Subscription Type
        subscriber_validation_label = Label(root, text="                      ")
        subscriber_validation_label.place(x=300, y=360, anchor="center")
        subscriber_validation_label.config(font=("Courier", 10))
        
        # Membership Date
        membership_date_label = Label(root, text="                                 ")
        membership_date_label.place(x=0, y=320, anchor="w")
        membership_date_label.config(font=("Courier", 8))
        
        # Membership Expiration Date
        membership_expired_label = Label(root, text="                              ")
        membership_expired_label.place(x=320, y=320, anchor="center")
        membership_expired_label.config(font=("Courier", 8))
        
        # Renewal
        renewal_label = Label(root, text="                      ")
        renewal_label.place(x=450, y=320, anchor="w")
        renewal_label.config(font=("Courier", 10))
        
        # License Plate Number
        renewal_label = Label(root, text="                      ")
        renewal_label.place(x=420, y=270, anchor="w")
        renewal_label.config(font=("Courier", 10))
        
        # State
        state_label = Label(root, text="                      ")
        state_label.place(x=300, y=270, anchor="center")
        state_label.config(font=("Courier", 10))
        
# Print Member Information onto the system
def displayMemberInformation(name, membership_type, membership_date, membership_expired, renew, license_plate, state):
    
    # -------- SUBSCRIBER INFORMATION -------- #

    name_label = Label(root, text="Name: {}".format(name))
    name_label.place(x=0, y=270, anchor="w")
    name_label.config(font=("Courier", 10))
    name_label.after(10000, name_label.destroy)
    
    # Subscription Type
    subscriber_validation_label = Label(root, text="Subscription Type: {}".format(membership_type))
    subscriber_validation_label.place(x=300, y=360, anchor="center")
    subscriber_validation_label.config(font=("Courier", 10))
    subscriber_validation_label.after(10000, subscriber_validation_label.destroy)
    
    # Membership Date
    membership_date_label = Label(root, text="Membership Start: {}".format(membership_date))
    membership_date_label.place(x=0, y=320, anchor="w")
    membership_date_label.config(font=("Courier", 8))
    membership_date_label.after(10000, membership_date_label.destroy)
    
    # Membership Expiration Date
    membership_expired_label = Label(root, text="Membership Expired: {}".format(membership_expired))
    membership_expired_label.place(x=320, y=320, anchor="center")
    membership_expired_label.config(font=("Courier", 8))
    membership_expired_label.after(10000, membership_expired_label.destroy)
    
    # Renewal
    renewal_label = Label(root, text="Renewal: {}".format(renew))
    renewal_label.place(x=450, y=320, anchor="w")
    renewal_label.config(font=("Courier", 10))
    renewal_label.after(10000, renewal_label.destroy)
    
    # License Plate Number
    renewal_label = Label(root, text="License Plate: {}".format(license_plate))
    renewal_label.place(x=420, y=270, anchor="w")
    renewal_label.config(font=("Courier", 10))
    renewal_label.after(10000, renewal_label.destroy)
    
    # State
    state_label = Label(root, text="State: {}".format(state))
    state_label.place(x=300, y=270, anchor="center")
    state_label.config(font=("Courier", 10))
    state_label.after(10000, state_label.destroy)

    # -------- SUBSCRIBER INFORMATION -------- #
    
''' BUTTON FUNCTIONS '''
    
#----------------------------------------------------------------------#
        
#CONSTANTS
WIDTH = 655
HEIGHT = 400

#Create the window
root = Tk()

#Modify root window
root.title("Denton Ticketing System")
root.geometry("{}x{}".format(WIDTH, HEIGHT))

#----------------------------------------------------------------------#

'''CREATE TICKET'''
# Create Ticket Button
create_ticket_button = Button(root, text='Create Ticket', command = lambda: createTicket_BUTTON())
create_ticket_button.place(x=WIDTH/2-10, y=20, anchor="center")

# Bottom Line
f = Frame(root, height=1, width=WIDTH+HEIGHT, bg="black")
f.place(x=WIDTH/2-10, y=40, anchor="center")
'''CREATE TICKET'''

#----------------------------------------------------------------------#

'''Ticket Information'''
ticket_id_label = Label(root, text='Ticket ID:')
ticket_id_label.place(x=0, y=60, anchor="w")
ticket_id_label.config(font=("Courier", 10))

time_entered_label = Label(root, text='Time Entered:')
time_entered_label.place(x=300, y=60, anchor="center")
time_entered_label.config(font=("Courier", 10))

date_label = Label(root, text='Date:')
date_label.place(x=450, y=60, anchor="w")
date_label.config(font=("Courier", 10))

'''Ticket Information'''

#----------------------------------------------------------------------#

'''Ticket Validation'''
# Ticket Entry Label
ticket_validation_label = Label(root, text="Enter Ticket ID")
ticket_validation_label.place(x=300, y=90, anchor="center")
ticket_validation_label.config(font=("Courier", 10))


# Button Between Lines
submit_ticket_button = Button(root, text='Submit Ticket', command = lambda: validateTicketEntry_BUTTON(ticket_validation_entry.get()))
submit_ticket_button.place(x=420, y=115, anchor="center")

# Bottom Line
f_validation_bottom = Frame(root, height=1, width=WIDTH+HEIGHT, bg="black")
f_validation_bottom.place(x=300, y=130, anchor="center")

# Text Field
ticket_validation_entry = Entry(root)
ticket_validation_entry.place(x=300, y=115, anchor="center")

'''Ticket Validation'''

#----------------------------------------------------------------------#

'''Ticket Verification Information'''
ticket_id_label = Label(root, text='Status:')
ticket_id_label.place(x=0, y=160, anchor="w")
ticket_id_label.config(font=("Courier", 10))

date_in_label = Label(root, text='Date In: ')
date_in_label.place(x=125, y=145, anchor="w")
date_in_label.config(font=("Courier", 10))

date_out_label = Label(root, text='Date Out: ')
date_out_label.place(x=125, y=165, anchor="w")
date_out_label.config(font=("Courier", 10))

time_in_label = Label(root, text='Time In: ')
time_in_label.place(x=295, y=145, anchor="w")
time_in_label.config(font=("Courier", 10))

time_out_label = Label(root, text='Time Out: ')
time_out_label.place(x=295, y=165, anchor="w")
time_out_label.config(font=("Courier", 10))

cost_label = Label(root, text='Cost: $')
cost_label.place(x=450, y=145, anchor="w")
cost_label.config(font=("Courier", 10))

delta_label = Label(root, text='Duration: ')
delta_label.place(x=450, y=165, anchor="w")
delta_label.config(font=("Courier", 10))

'''Ticket Verification Information'''

#----------------------------------------------------------------------#

''' Subscriber Validation'''
# Top Line
f_subscriberValidation_top = Frame(root, height=1, width=WIDTH+HEIGHT, bg="black")
f_subscriberValidation_top.place(x=300, y=180, anchor="center")

# Subscriber Entry Label
subscriber_validation_label = Label(root, text="Enter Membership ID")
subscriber_validation_label.place(x=300, y=200, anchor="center")
subscriber_validation_label.config(font=("Courier", 10))

# Text Field for Membership
subscriber_validation_entry = Entry(root)
subscriber_validation_entry.place(x=300, y=225, anchor="center")

# Button to Validate Subscriber
submit_ticket_button = Button(root, text='Submit', command = lambda: validateMembershipID_BUTTON(subscriber_validation_entry.get()))
submit_ticket_button.place(x=400, y=225, anchor="center")

''' Subscriber Validation'''

'''CREATED BY'''
propertyOf_label = Label(root, text='PROPERTY OF DENTON PARKING GARAGES')
propertyOf_label.place(x=290, y=HEIGHT-10, anchor="center")
propertyOf_label.config(font=("Courier", 10))
'''CREATED BY'''


#----------------------------------------------------------------------#
#                            GUI BACKEND                               #
#----------------------------------------------------------------------#
def createValidID():
    
    print(check_lot())
    if (check_lot() == 'full'):

        full_label = Label(root, text='Lot is Full: ', bg='red')
        full_label.place(x=0, y=100, anchor="w")
        full_label.config(font=("Courier", 10))
        full_label.after(10000, full_label.destroy)

    else:       
        
        # Create random ticket ID
        ticket_id = random.randint(11111111, 99999999)
        
        # Check to see if the ID already exists in the database
        cursor.execute('SELECT ticket_id FROM ticket WHERE ticket_id LIKE {}'.format(ticket_id))
        check = str(cursor.fetchall())
        
        # If the ticket EXISTS in the database
        if(check != '[]'):
            print('\nTicket ID currently in use, generating new ID...\n')
            ticket_id = generate_new_ticket_id()
            create_ticket(ticket_id)
        # If the ticket ID is NOT in the system, create new ticket.
        else:
            create_ticket(ticket_id)

# This function will generate a ticket ID from 11111111 --> 99999999        
def generate_new_ticket_id():
    return random.randint(11111111, 99999999)

# This function will generate a dictionary called 'Ticket' which will carry the following
# Ticket ID, Date, Time In, Time Out, Lot #
def create_ticket(ticket_id):
    
    # Capture current date for receipt
    date = str(datetime.datetime.now())
    date = date[:10]
    
    # Capture current time for receipt
    time = str(datetime.datetime.now())
    time = time[11:19]
    
    # Create ticket dictionary 
    ticket = {
        'ticket_id' : ticket_id,
        'lot_no' : 'L1',
        'date' : date,
        'time_in' : time
        }
    
    # Push ticket information to database
    try:
        cursor.execute("""
                       INSERT INTO denton.ticket (ticket_id, date, date_out, time, time_out, validated)
                       VALUES (%s, %s, %s, %s, %s, %s)
                       """, (ticket_id, date, 'In Lot', time, 'In Lot', 'N'))
        conn.commit()
    except:
        conn.rollback()
    
    # Display updated ticket information in the system
    displayTicketInformation(ticket_id, date, time)
    
    # Push ticket object to print ticket function to print ticket
    print_ticket(ticket)

# This function update time out to database
def timeOut(ticket_id):
    
    #Capture current date for receipt
    dateOut = str(datetime.datetime.now())
    dateOut = dateOut[:10]
    
    # Capture current time for receipt
    timeOut = str(datetime.datetime.now())
    timeOut = timeOut[11:19]
    
    # Update time out to database
    try:
        cursor.execute("""
                       UPDATE denton.ticket
                       SET date_out=%s, time_out=%s
                       WHERE ticket_id=%s
                       """, (dateOut, timeOut, ticket_id))
        conn.commit()
    except:
        conn.rollback()       

# This function calculates the cost and update the information to the database
def cost(ticket_id):
    
    # Capture current time for receipt
    timeOut = str(datetime.datetime.now())
    timeOut = timeOut[11:19]
    
    # Get date in from database
    cursor.execute("""
                   SELECT date from denton.ticket
                   WHERE ticket_id = %s
                   """, (ticket_id,))
    row = cursor.fetchone()
    inDate = row[0]
    
    # Get date out from database
    cursor.execute("""
                   SELECT date_out from denton.ticket
                   WHERE ticket_id = %s
                   """, (ticket_id,))
    row = cursor.fetchone()
    outDate = row[0]

    # Get time in from database
    cursor.execute("""
                   SELECT time from denton.ticket
                   WHERE ticket_id = %s
                   """, (ticket_id,))
    row = cursor.fetchone()
    inTime = row[0]
    
    # Get time out from database
    cursor.execute("""
                   SELECT time_out from denton.ticket
                   WHERE ticket_id = %s
                   """, (ticket_id,))
    row = cursor.fetchone()
    outTime = row[0]
    
    # Calculate total time
    inDateTime = inDate + " " +inTime
    inDateTime = datetime.datetime.strptime(inDateTime, "%Y-%m-%d %H:%M:%S")
    outDateTime = outDate + " " + outTime
    outDateTime = datetime.datetime.strptime(outDateTime, "%Y-%m-%d %H:%M:%S")
    timeDelta = outDateTime - inDateTime
    duration = datetime.timedelta.total_seconds(timeDelta)
#    
#    # Calculate cost ($2.50 per 15 mins)
    cost = 1.50 * math.ceil(duration / 900);
    
    # Update cost in database
    try:
        cursor.execute("""
                       UPDATE denton.ticket
                       SET cost=%s
                       WHERE ticket_id=%s
                       """, (cost, ticket_id))
        conn.commit()
    except:
        conn.rollback()
        
    # Update validated field in database
    try:
        cursor.execute("""
                       UPDATE denton.ticket
                       SET validated=%s
                       WHERE ticket_id=%s
                       """, ('Y', ticket_id))
        conn.commit()
    except:
        conn.rollback()
        
            
    # Update console
    date_in_label = Label(root, text='Date In: ' + inDate)
    date_in_label.place(x=125, y=145, anchor="w")
    date_in_label.config(font=("Courier", 10))
    date_in_label.after(10000, date_in_label.destroy)
    
    date_out_label = Label(root, text='Date Out: ' + outDate)
    date_out_label.place(x=125, y=165, anchor="w")
    date_out_label.config(font=("Courier", 10))
    date_out_label.after(10000, date_out_label.destroy)
    
    time_in_label = Label(root, text='Time In: ' + inTime)
    time_in_label.place(x=295, y=145, anchor="w")
    time_in_label.config(font=("Courier", 10))
    time_in_label.after(10000, time_in_label.destroy)

    time_out_label = Label(root, text='Time Out: ' + timeOut )
    time_out_label.place(x=295, y=165, anchor="w")
    time_out_label.config(font=("Courier", 10))
    time_out_label.after(10000, time_out_label.destroy)
    
    cost_label = Label(root, text='Cost: $ ' + str(cost))
    cost_label.place(x=450, y=145, anchor="w")
    cost_label.config(font=("Courier", 10))
    cost_label.after(10000, cost_label.destroy)
    
    delta_label = Label(root, text='Duration: ' + str(timeDelta))
    delta_label.place(x=450, y=165, anchor="w")
    delta_label.config(font=("Courier", 10))
    delta_label.after(10000, delta_label.destroy)

    
# When the ticket is fully created, this function prints out the contents
def print_ticket(ticket):
    
    print("Thank you for choosing Denton Parking Garages\n123 Broadway, New York, NY 10023\n" +
          "\nTicket ID: {} \n".format(ticket['ticket_id']) +
          "Lot No: {} \n".format(ticket['lot_no'])+ 
          "Date: {} \n".format(ticket['date']) + 
          "Time Created: {}\n".format(ticket['time_in']))

def check_lot():
    
    lot_status = 'empty'
    
    cursor.execute("""
                   SELECT date_out from denton.ticket
                   WHERE time_out = %s
                   """, ('In Lot',))
    inLotH = len(cursor.fetchall())
    print(inLotH)

    cursor.execute("""
                   SELECT in_lot from denton.subscription
                   WHERE in_lot = %s
                   """, ('Y',))
    inLotS = len(cursor.fetchall())
    print(inLotS)

    if ((inLotH + inLotS) >= 26):
        lot_status = 'full'
        print(lot_status)
    
    return lot_status
    
# Check to see if a customer has a membership ID
def checkMembership(membership_id):
    
    # Check to see if the membership ID already exists in the database
    cursor.execute('SELECT membership_id FROM subscription WHERE membership_id LIKE {}'.format(membership_id))
    check = str(cursor.fetchall())
    
    # If the membership ID EXISTS in the database
    if(check != '[]'):
        print('\nMembership ID Exists\n')
        
        # Update in lot status of subscriber
        try:
            cursor.execute("""
                           SELECT denton.ticket
                           SET in_lot=%s
                           WHERE membership_id=%s
                           """, ('Y', membership_id))
            conn.commit()
        except:
            conn.rollback()
        
        # ------ Create variables to push to the button object ------ #
        
        # Fetch Name 
        cursor.execute('SELECT name FROM subscription WHERE membership_id LIKE {}'.format(membership_id))
        check = str(cursor.fetchall())
        name = (check.strip('[] () ,'))
        name = str(name.replace("'", ""))
                
        # Fetch Subscription Type
        cursor.execute('SELECT subscription_type FROM subscription WHERE membership_id LIKE {}'.format(membership_id))
        check = str(cursor.fetchall())
        membership_type = (check.strip('[] () ,'))
        membership_type = str(membership_type.replace("'", ""))
        
        # Fix this
        # Fetch Subscription Start Date
        cursor.execute('SELECT subscription_date FROM subscription WHERE membership_id LIKE {}'.format(membership_id))
        check = str(cursor.fetchall())
        subscription_date = (check.strip('[] () ,'))
        subscription_date = str(subscription_date.replace("'", ""))
        
        # Fetch Subscription Expiration Date
        cursor.execute('SELECT subscription_expired FROM subscription WHERE membership_id LIKE {}'.format(membership_id))
        check = str(cursor.fetchall())
        subscription_expired = (check.strip('[] () ,'))
        subscription_expired = str(subscription_expired.replace("'", ""))
        
         # Fetch Renewal Status
        cursor.execute('SELECT renew FROM subscription WHERE membership_id LIKE {}'.format(membership_id))
        check = str(cursor.fetchall())
        renew = (check.strip('[] () ,'))
        renew = str(renew.replace("'", ""))
        
         # Fetch License Plate
        cursor.execute('SELECT license_plate FROM subscription WHERE membership_id LIKE {}'.format(membership_id))
        check = str(cursor.fetchall())
        license_plate = (check.strip('[] () ,'))
        license_plate = str(license_plate.replace("'", ""))
        
         # Fetch State
        cursor.execute('SELECT state FROM subscription WHERE membership_id LIKE {}'.format(membership_id))
        check = str(cursor.fetchall())
        state = (check.strip('[] () ,'))
        state = str(state.replace("'", ""))
        
        # Push variables to function that prints it on the system
        displayMemberInformation(name, membership_type, subscription_date, subscription_expired, renew, license_plate, state)
        
    # If the membership ID is NOT in the system, create new ticket.
    else:
        print('\nMembership ID Does Not Exist')
        
#--------------------#
#    BEGIN SCRIPT    #
root.mainloop()
#    BEGIN SCRIPT    #
#--------------------#