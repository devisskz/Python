#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# A class to represent calendar dates
#
#Name: Batyr Issabekov

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month = init_month
        self.day = init_day
        self.year = init_year



    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

#### Put your code for problem 2 below. ####

    def advance_one(self):
        """represents one calendar day after the date that it originally
        represented"""

        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.is_leap_year() == True:   #if it is leap year,given from lecture
            days_in_month[2] = 29

        if days_in_month[self.month] == self.day:  #if it is last day of month
            if self.month == 12:                   #if it is last month of year
                self.year+=1                       #add 1 year
                self.month = 1                     # month is 1
                self.day = 1                        #day is 1
            else:
                self.month+=1                       #otherwise, next month
                self.day = 1                           #first day
        else:
            self.day+=1                     #otherwise, just next day


    def advance_n(self,n):
        """ changes the calling object so that it represents n calendar
        days after the date it originally represented.print all of the
        dates from the starting date to the finishing
        date, inclusive of both endpoints."""

        if n == 0:
            print(self)   #if n is 0, return current date
        else:
            for i in range(n):  #else, for each loop in range of n
                print(self)    #prints the date
                self.advance_one()   #advances and loops back
            print(self)       #when done looping, prints the last new date

    def __eq__(self,other):
        """returns true if self and other have the same calendar date"""

        if self.day == other.day:
            if self.month == other.month:
                if self.year == other.year:   #if each element is equal, returns
                    return True                     #true

        return False            #otherwise, False

    def is_before(self,other):
        """returns True if other is before current date, otherwise false"""


        if self.year > other.year: #commpares years first
            return False
        if self.year == other.year and self.month> other.month:  #then months
            return False
        if self.year == other.year and self.month == other.month and self.day > other.day:
            return False   #then compares days
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return False  #if all are equal, it is false
        else:
            return True   #otherwise, true


    def is_after(self,other):
        """returns True if other is after current date, otherwise false"""
        # What I did is copy is_before and change the signs of more than to less

        if self.year < other.year: #commpares years first
            return False
        if self.year == other.year and self.month<other.month:  #then months
            return False
        if self.year == other.year and self.month == other.month and self.day < other.day:
            return False   #then compares days
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return False  #if all are equal, it is false
        else:
            return True   #otherwise, true


    def days_between(self,other):
        """returns an integer that represents the number of days between
        self and other."""
        d1 = self.copy()
        d2 = other.copy()  #copies both to not change inputs
        count = 0
        if d1.is_before(d2) == True:  #if d1 is before d2
            while d1 != d2:
                d1.advance_one()    #advances 1 for until they are equal
                count +=1           #adds count each time it loops
            count *= -1             #because it is before, we negate count
            return count
        elif d1.is_after(d2) == True:
            while d2 != d1:
                d2.advance_one()    #advances 1 until they are equal
                count +=1           #count +1 each loop
            return count           #returns count
        else:
            return 0             #otherwise, dates are equal


    def day_name(self):
        """returns a string that indicates the day of the week"""

        day_names = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

        monday = Date(4,6,2020)
        num_days = self.days_between(monday)

        if num_days == 0:
            return day_names[0]   #if number of days = 0, it is also monday
        else:
            day = num_days%7     #otherwise, mod 7 of the days between, as hinted
            return day_names[day]
