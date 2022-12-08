import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
  
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input("\nChoose a city to filter by? New York City, Chicago or Washington?\n").lower().strip()
      if city not in ('new york city', 'chicago', 'washington'):
        print("Sorry, I didn't find a file for your selected city. Try again.")
        continue
      else:
        print("\nYou have chosen {} as your city.".format(city)) 
        break
       
        

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nChoose a month to filter by? January, February, March, April, May, June or type 'all' if you do not          have any preference?\n").lower().strip()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Sorry, you may wrote a wrong month. Try again.")
        continue
      else:
        print("\nYou have chosen {} as your month.".format(month)) 
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nChoose a day to filter by? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you like to retrive all days data.\n").lower().strip()
      if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        print("Sorry, you may wrote a wrong day. Try again.")
        continue
      else:
        print("\nYou have chosen {} as your day.".format(day)) 
        break

        
        
    print("\nYou have chosen {} as your city and {} as month and {} as day .".format(city , month , day)) 
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    
    print("<<<<< LOADING YOUR PRETTY DATA >>>>> ")
    
    city_df = pd.read_csv(CITY_DATA[city])

    city_df['Start Time'] = pd.to_datetime(city_df['Start Time'])
    
    city_df['month'] = city_df['Start Time'].dt.month 
    
    city_df['day'] = city_df['Start Time'].dt.weekday_name
    
    city_df['hour'] = city_df['Start Time'].dt.hour 
    
    # change the month number to month name by using calender library
    city_df['month'] = city_df['month'].apply(lambda x: calendar.month_name[x])   
    
   
    
    # filter by month if applicable
    if month != 'all':
     # filter by month to create the new dataframe
        city_df = city_df[city_df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        city_df = city_df[city_df['day'] == day.title()]

    
#     print(city_df.head())
    print('-'*40)

    return city_df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    frequent_month = df['month'].mode()[0]
 

    # TO DO: display the most common day of week
    frequent_day = df['day'].mode()[0]
 

    # TO DO: display the most common start hour
    frequent_hour = df['hour'].mode()[0]
 
    
    print(f"\n most poplur month is {frequent_month} \nand most poplor day is {frequent_day} \nand most poplur start hour is       {frequent_hour}.\n\n")
#       print("""\nmost poplur month is {} \nand most poplor day is {} \nand most poplur compined start hour is {}.""".format(frequent_month , frequent_day , frequent_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # df.column.mode() 
    frequent_start_st = df['Start Station'].mode()[0]
 
    # TO DO: display most commonly used end station

    frequent_end_st = df['End Station'].mode()[0]
 

    # TO DO: display most frequent combination of start station and end station trip

    df["way"] = df['Start Station'].astype(str) +" to "+ df["End Station"]
    
    frequent_start_to_end = df['way'].mode()[0]
    

    
    print("""\nmost poplur start statoin is {} \nand most popluar end statioin is {} \nand most poplur compined start and end station is {}.""".format (frequent_start_st , frequent_end_st , frequent_start_to_end))

    print("\n\n\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()

    # TO DO: display mean travel time

    mean_travel = df['Trip Duration'].mean()
    
    print("""\nthe total travel time  is {} \nthe mean travel time is  {} .""".format (total_travel , mean_travel))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()

    print(f"\n The users type in your selected city  \n\n{user_type}")


    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(f"\n The number of female and male in your selected city \n\n{gender}")
    except:
        print("\n we can't find a GENDER column in your selected city .")


    
    try:
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        most_commont = df['Birth Year'].mode()[0]
        recent = df['Birth Year'].max()
        print("""\nthe earliest year of birth  is {} \nthe most common year of birth  is  {} \nthe  most recent year of birth  is               {}.""".format (earliest , most_commont , recent))    
    except:
        print("\n \n no BIRTH YEAR data.")
    
  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
#Function to display the data frame itself as per user request
def display_data(df):
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    
    while (view_data == 'yes'):
      print(df.iloc[start_loc:start_loc+5])
      start_loc += 5
      view_data = input("Do you wish to continue to view new 5 rows ?: ").lower()
      
    print('-'*80)
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
