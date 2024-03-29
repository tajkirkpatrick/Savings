import datetime
import calendar
from decimal import Decimal

class SavingsGoal(object):

    def __init__(self, name, amount):
        """
        Initilization Method - asks user for name and amount, then init-s the other data structures need by the object, all initialized to {None} or {0}
        
        Arguments:
            name {string} -- The name of the SavingsGoal, initialized with the object
            amount {int} -- The total amount of money to be saved up
        """
        self.SavingsName = name
        self.TotalPaymentAmount = amount
        self.DownPaymentAmount = None
        self.userStartDate = None
        self.paymentPlan = [[None, None, None, None, None],
                            [None, None, None, None, None],
                            [None, None, None, None, None]]

        self.Phase1Tot_TotalPaymentAmount = None 
        self.Phase2Tot_TotalPaymentAmount = None  
        self.Phase3Tot_TotalPaymentAmount = None  
        self.Phase_Payments =  [[0,0,0,0,0], 
                                [0,0,0,0,0], 
                                [0,0,0,0,0]]

        self.Phase_Dates = [[0,0,0,0,0], 
                            [0,0,0,0,0], 
                            [0,0,0,0,0]]
        self.userStartDate = None
        self.ranStartOnce = False
        self.longTermGoal = False

    def start(self):
        validStartDate = False
        user_input = ''
        downPaymentAmt = 0
        choice_A = None
        choice_B = None
        choice_C = None
        choice_D = None
        user_choice_letter = None


        if self.ranStartOnce == False:
            if not(validStartDate):
                return_val = self.setStartDate()
                while return_val != 0:
                    return_val = self.setStartDate()
                self.divyAllPhases()
            else:
                print("----------------------------------------\nStart of start()")

            while True:
                user_input = (
                    input("\nWould you like to plan a down payment (y/N): "))

                if user_input != 'y' and user_input != 'N':
                    print("Invalid Input\n")

                if user_input == 'y':
                    for amount in range(0,3):
                        downPaymentAmt += self.Phase_Payments[0][amount]
                    self.DownPaymentAmount = downPaymentAmt
                    print(f'The down payment amt is: ${downPaymentAmt}\t(Due on: {self.userStartDate.strftime("%x")})\n\n')
                    break
                elif user_input == 'N':
                    print("Alrighty, Moving on!\n")
                    break

            while True:
                pass_loop = False

                user_input = (
                    input("Is this a long-term goal? 3+ Years to Complete? (y/N): "))

                if user_input != 'y' and user_input != 'N':
                    print("Invalid Input\n")
                    continue
                elif user_input == 'y' or user_input == 'N':
                    pass_loop = True
                
                if pass_loop == False:
                    continue


                if user_input == 'N':
                    print(
                        "I will create a (A) 3-month, (B) 6-month, (C) 12-month, and (D) 24-month plans!\n\n")
                elif user_input == 'y':
                    self.longTermGoal = True
                    print("I will create a (A) 3-year, (B) 5-year, and (C) 10-year plan\n\n")

                # * This is assuming that the goal is short term. User answers was N
                if self.longTermGoal == False:
                    print("The User Start Date is: " +
                        str((self.userStartDate.strftime("%x"))))
                    print(f"The User Goal Amount is: ${self.TotalPaymentAmount}\n")

                    choice_A = self.breakdown(3)
                    choice_B = self.breakdown(6)
                    choice_C = self.breakdown(12)
                    choice_D = self.breakdown(24)

                    while True:
                        user_choice_letter = input("Which plan would you like? (A) : 3 mo, (B) : 6 mo, (C) : 12 mo, (D) : 24 mo\n")

                        if user_choice_letter != 'A' and user_choice_letter != 'B' and user_choice_letter != 'C' and user_choice_letter != 'D':
                            print("Invalid Input\n")
                            continue
                        else:
                            print(f"Thank you! You've selected {user_choice_letter}")
                            break;

                    self.payment_plan_choice(choice_A, choice_B, choice_C, choice_D, user_choice_letter)
                    break
                elif self.longTermGoal == True:
                    print("The User Start Date is: " + str((self.userStartDate.strftime("%x"))))
                    print(f"The User Goal Amount is: ${self.TotalPaymentAmount}\n")

                    choice_A = self.breakdown(36)
                    choice_B = self.breakdown(60)
                    choice_C = self.breakdown(120)

                    while True:
                        user_choice_letter = input("Which plan would you like? (A) : 3 year, (B) : 5 year, (C) : 10 year\n")

                        if user_choice_letter != 'A' and user_choice_letter != 'B' and user_choice_letter != 'C':
                            print("Invalid Input\n")
                            continue
                        else:
                            print(f"Thank you! You've selected {user_choice_letter}")
                            break;

                    self.payment_plan_choice(choice_A, choice_B, choice_C, choice_D, user_choice_letter)
                    self.construct_payment_plan(self.Phase_Dates, self.Phase_Payments)
                    break
        else:
            self.construct_payment_plan(self.Phase_Dates, self.Phase_Payments)
            

        self.ranStartOnce = True
        print("\nEnd of start()\n----------------------------------------")
        return 0

    def construct_payment_plan(self, Phase_Dates, Phase_Payments):

        for element in range(0,5):
            self.paymentPlan[0][element] = (self.Phase_Dates[0][element], Phase_Payments[0][element])

        for element in range(0,5):
            self.paymentPlan[1][element] = (self.Phase_Dates[1][element], Phase_Payments[1][element])

        for element in range(0,5):
            self.paymentPlan[2][element] = (self.Phase_Dates[2][element], Phase_Payments[2][element])

        return 0

    def payment_plan_choice(self, choice_A, choice_B, choice_C, choice_D, user_choice_letter):

        selected_A = 'A'
        selected_B = 'B'
        selected_C = 'C'
        selected_D = 'D'
        exclude_D = False

        # TODO : PLEASE SHORTEN THIS TRANSFER FOR LOOP INTO A FUNCTION!

        if choice_D is None:
            exclude_D = True
        elif choice_D is not None:
            pass

        if exclude_D:
            if user_choice_letter == selected_A:
                for element in range(0,5):
                    temp = choice_A[element]
                    self.Phase_Dates[0][element] = temp

                for element in range(5,10):
                    temp = choice_A[element]
                    self.Phase_Dates[1][element-5] = temp

                for element in range(10,15):
                    temp = choice_A[element]
                    self.Phase_Dates[2][element-10] = temp

            if user_choice_letter == selected_B:
                for element in range(0,5):
                    temp = choice_B[element]
                    self.Phase_Dates[0][element] = temp

                for element in range(5,10):
                    temp = choice_B[element]
                    self.Phase_Dates[1][element-5] = temp

                for element in range(10,15):
                    temp = choice_B[element]
                    self.Phase_Dates[2][element-10] = temp
            if user_choice_letter == selected_C:
                for element in range(0,5):
                    temp = choice_C[element]
                    self.Phase_Dates[0][element] = temp

                for element in range(5,10):
                    temp = choice_C[element]
                    self.Phase_Dates[1][element-5] = temp

                for element in range(10,15):
                    temp = choice_C[element]
                    self.Phase_Dates[2][element-10] = temp
        else:
            if user_choice_letter == selected_A:
                for element in range(0,5):
                    temp = choice_A[element]
                    self.Phase_Dates[0][element] = temp

                for element in range(5,10):
                    temp = choice_A[element]
                    self.Phase_Dates[1][element-5] = temp

                for element in range(10,15):
                    temp = choice_A[element]
                    self.Phase_Dates[2][element-10] = temp
            if user_choice_letter == selected_B:
                for element in range(0,5):
                    temp = choice_B[element]
                    self.Phase_Dates[0][element] = temp

                for element in range(5,10):
                    temp = choice_B[element]
                    self.Phase_Dates[1][element-5] = temp

                for element in range(10,15):
                    temp = choice_B[element]
                    self.Phase_Dates[2][element-10] = temp
            if user_choice_letter == selected_C:
                for element in range(0,5):
                    temp = choice_C[element]
                    self.Phase_Dates[0][element] = temp

                for element in range(5,10):
                    temp = choice_C[element]
                    self.Phase_Dates[1][element-5] = temp

                for element in range(10,15):
                    temp = choice_C[element]
                    self.Phase_Dates[2][element-10] = temp
            if user_choice_letter == selected_D:
                for element in range(0,5):
                    temp = choice_D[element]
                    self.Phase_Dates[0][element] = temp

                for element in range(5,10):
                    temp = choice_D[element]
                    self.Phase_Dates[1][element-5] = temp

                for element in range(10,15):
                    temp = choice_D[element]
                    self.Phase_Dates[2][element-10] = temp
        return 0

    def breakdown(self, monthsToAdd):
        planEndDate = self.add_months(self.userStartDate, monthsToAdd)
        diff = planEndDate - self.userStartDate
        return_array = []

        if monthsToAdd > 30:
            monthsToAdd = int(monthsToAdd/12)
            print("The {}-Year End Date is: ".format(monthsToAdd) +
                str(planEndDate.strftime("%x")) + " ({} months)\n".format(int(diff.days/30)))
        else:
            print("The {}-Month End Date is: ".format(monthsToAdd) +
                str(planEndDate.strftime("%x")) + " ({} days)\n".format(int(diff.days)))

        totalDays = round(float(diff.days))
        daysPerPhase_Interval = round(float(totalDays/3))
        daysBetweenPayments_Interval = round(float(totalDays/15))

        print("Format: Phase 1 Dates\t-\tPhase 2 Dates\t-\tPhase 3 Dates")

        return_array = self.phaseDatesPreview(totalDays)
        return return_array

    def phaseDatesPreview(self, totalDays):
        paymentPlanPreviewArray = []

        start = self.userStartDate
        end = start + datetime.timedelta(totalDays)
        diff = end - start
        daysTillNextPayment = diff.days/15

        nextPaymentDate = start
        for paymentDueDate in range(0, 15):
            nextPaymentDate += datetime.timedelta(daysTillNextPayment)
            paymentPlanPreviewArray.append(nextPaymentDate)

        for element in range(0,5):
            print(f"\t{paymentPlanPreviewArray[element]} (${self.Phase_Payments[0][element]})\t\t|\t{paymentPlanPreviewArray[element+5]} (${self.Phase_Payments[1][element]})\t|\t{paymentPlanPreviewArray[element+10]} (${self.Phase_Payments[2][element]})")
            

        print("")
        return paymentPlanPreviewArray

    def add_months(self, sourcedate, months):
        month = sourcedate.month - 1 + months
        year = sourcedate.year + month // 12
        month = month % 12 + 1
        day = min(sourcedate.day, calendar.monthrange(year, month)[1])
        return datetime.date(year, month, day)

    def setStartDate(self):
        monthsWithout31 = [2, 4, 6, 9, 11]
        userYear = None
        userMonth = None
        userDay = None

        print(
            "\n----------------------------------------\nStart of setStartDate()\n\n")

        # * Take the user's year, it can't be less than the current year
        user_input = input("What is the Year of the start date?\n")
        try:
            val = int(user_input)
            if len(user_input) != 4 or val < datetime.datetime.now().year:
                raise ValueError
            else:
                userYear = val
        except (UnboundLocalError, ValueError) as error:
            print('Your value is not an acceptable year\nNo values were saved.')
            return 1

        # * Month
        user_input = input("What is the Month of the start date?\n")
        try:
            val = int(user_input)
            if val < 1 or val > 12:
                raise ValueError

            if (userYear == datetime.datetime.now().year and val <= datetime.datetime.now().month):
                raise ValueError
            else:
                userMonth = val
        except (UnboundLocalError, ValueError) as error:
            print('Your value is not an acceptable month')
            return 2

        # * Day
        user_input = input("What is the Day of the start date?\n")
        try:
            val = int(user_input)
            if val < 1 or val > 31:
                raise ValueError

            if val == 31 and userMonth in monthsWithout31:
                raise ValueError
            else:
                userDay = val
        except (UnboundLocalError, ValueError) as error:
            print('Your value is not an acceptable month \ day combination')
            return 3

        self.userStartDate = datetime.date(userYear, userMonth, userDay)
        self.validStartDate = True
        print("User Start Date Saved!")
        print(
            "\nEnd of setStartDate() - SUCCESS\n----------------------------------------")

        return 0

    def divyPhase1Amount(self):
        for element in range(0,5):
            if element != 3 and element != 4:
                self.Phase_Payments[0][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.20)
            elif element == 3:
                self.Phase_Payments[0][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.15)
            else:
                self.Phase_Payments[0][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.25)
        return

    def divyPhase2Amount(self):
        for element in range(0,5):
            if element == 0:
                self.Phase_Payments[1][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.10)
            elif element == 1:
                self.Phase_Payments[1][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.15)
            elif element == 2:
                self.Phase_Payments[1][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.25)
            elif element == 3:
                self.Phase_Payments[1][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.30)
            elif element == 4:
                self.Phase_Payments[1][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.20)
        return

    def divyPhase3Amount(self):

        for element in range(0,5):
            if element == 0:
                self.Phase_Payments[2][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.30)
            elif element == 1:
                self.Phase_Payments[2][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.25)
            elif element == 2:
                self.Phase_Payments[2][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.20)
            elif element == 3:
                self.Phase_Payments[2][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.15)
            elif element == 4:
                self.Phase_Payments[2][element] = round((float((self.Phase1Tot_TotalPaymentAmount)))*.10)
        return

    def divyAllPhases(self):
        if self.Phase1Tot_TotalPaymentAmount == None:
            self.Phase1Tot_TotalPaymentAmount = self.TotalPaymentAmount*.33
            self.Phase2Tot_TotalPaymentAmount = self.TotalPaymentAmount*.50
            self.Phase3Tot_TotalPaymentAmount = self.TotalPaymentAmount*.17

        self.divyPhase1Amount()
        self.divyPhase2Amount()
        self.divyPhase3Amount()
        return

    def setNewTotalAmount(self, newAmount):
        print(
            "\n----------------------------------------\nStart of setTotalAmount()")

        self.TotalPaymentAmount = newAmount
        self.reCalibrateAmounts()

        print(
            "\nEnd of setTotalAmount() - SUCCESS - New Amount: " + str(self.TotalPaymentAmount) + "\n----------------------------------------")
        return

    def reCalibrateAmounts(self):
        self.Phase1Tot_TotalPaymentAmount = self.TotalPaymentAmount*.33
        self.Phase2Tot_TotalPaymentAmount = self.TotalPaymentAmount*.50
        self.Phase3Tot_TotalPaymentAmount = self.TotalPaymentAmount*.17

        self.divyAllPhases()
        self.construct_payment_plan(self.Phase_Dates, self.Phase_Payments)
        return

    def getAmount(self):
        return self.TotalPaymentAmount

    def getName(self):
        return self.SavingsName
