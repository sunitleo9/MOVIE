x = 20
booked_seat=0
price_of_ticket=0
total_income=0
row=int(input('Enter no of rows: \n'))
seats = int(input('Enter no of seats in a row: \n'))
total_seat=row*seats
booked_ticket_person=[[None for j in range(seats)] for i in range(row)]

class chart:
    
    @staticmethod
    def chart_maker():
        seats_chart={}
        for i in range(row):
            seats_in_row={}
            for j in range(seats):
                seats_in_row[str(j+1)]='S'
            seats_chart[str(i)]=seats_in_row
        return seats_chart

    @staticmethod
    def find_percentage():
        percentage=(booked_seat/total_seat)*100
        return percentage

class_call=chart
table_of_chart=class_call.chart_maker()

while x!=0:
    print('1 for show the seats \n2 for buy a ticket \n3 for statistics', '\n4 for show booked tickets user info \n0 for exit')

    x=int(input('select option : '))
    if x==1:
        if seats<10:
            for seat in range(seats):
                print(seat,end=' ')
            print(seats)
        else:
            for seat in range(10):
                print(seat, end = ' ')
            for seat in range(10, seats):
                print(seat, end= ' ')
            print(seats)
        if seats < 10:
            for num in table_of_chart.keys():
                print(int(num)+1, end= ' ')
                for no in table_of_chart[num].values():
                    print(no, end= ' ')
                print()
        else:
            count_num=0
            for num in table_of_chart.keys():
                if int(list(table_of_chart.keys())[count_num])<9:
                    print(int(num)+1, end = ' ')
                else:
                    print(int(num)+1, end = ' ')
                count_key = 0
                for no in table_of_chart[num].values():
                    if int(list(table_of_chart[num].keys())[count_key])<=10:
                        print(no, end=' ')
                    else:
                        print(no, end=' ')
                    count_key += 1
                count_num +=1
                print()
        print('Vacent seats = ',total_seat - booked_seat)
        print()
    
    elif x == 2:
        row_number= int(input('Enter row number: \n'))
        column_number=int(input('Enter column number: \n'))
        if row_number in range (1,row+1) and column_number in range(1, seats+1):
            if table_of_chart[str(row_number-1)][str(column_number)]=='S':
                if row*seats<60:
                    price_of_ticket=10
                elif row_number <= int(row/2):
                    price_of_ticket=10
                else:
                    price_of_ticket=8
                print('Price of ticket -','$',price_of_ticket)
                confirm = input('yes for booking and no for stop booking -')
                person_detail={}
                if confirm=='yes':
                    person_detail['Name']=input('Enter name -')
                    person_detail['Gender']=input('Enter Gender -')
                    person_detail['Age']=input('Enter age-')
                    person_detail['Phone_no']=input('Enter phone number-')
                    person_detail['Ticket_price']=price_of_ticket
                    table_of_chart[str(row_number-1)][str(column_number)]='B'
                    booked_seat+=1
                    total_income += price_of_ticket
                    print('Booked succesfull')
                else:
                    booked_ticket_person[row_number-1][column_number-1]=person_detail
                    print('booked-successfully \n')
                    continue                    
            else:
                print('seat already booked \n')
        else:
            print()
            print('*** Invalid input ***')
        print()
    elif x == 3:
        print('Number of purchased ticket-',booked_seat)
        print('Percentage-', '$',class_call.find_percentage())
        print('Total income -', '$', price_of_ticket)
        print('Total income -', '$', total_income)
        print()

    elif x == 4:
        enter_row = int(input('Enter row number - \n'))
        enter_column=int(input('Enter column number - \n'))
        if enter_row in range(1,row+1) and enter_column in range(1, seats+1):
            if table_of_chart[str(enter_row - 1)][str(enter_column)]=='B':
                person=booked_ticket_person[enter_row-1][enter_column-1]
                print('Name-', person_detail['Name'])
                print('Gender-', person_detail['Gender'])
                print('Age-', person_detail['Age'])
                print('Phone number -', person_detail['Phone_no'])
                print('Ticket price-','$',person_detail['Ticket_price'])
            else:
                print()
                print('**** VACENT SEAT ****')
        else:
            print()
            print('*** Invalid input')
        print()
    else:
        print()
        print('*** Invalid input')
        print()
