import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to hinval
    city = input("Please choose a city: chicago, new york city, or washington ? ").lower()
    while city not in CITY_DATA:
        print("Please enter a valid city")
        city = input("Please choose a city: chicago, new york, or washington ? ").lower()

        # TO DO: get user input for month (all, january, february, ... , june)
    months = ['1', '2', '3', '4', '5', '6', 'all']
    month = input('Please chooes a month from 1 to 6 or use "all" ').lower()
    while month not in months:
        print('Please Enter a valid month')
        month = input('Please chooes a month from 1 to 6 or use "all" ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    day = input('Please enter the day by letters ').lower()
    while day not in days:
        print('Please enter a valid day')
        day = input('Please enter the day by letters ').lower()

    print('-'*100)
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
    #load data for city
    print("\nLoading data....")
    df = pd.read_csv(CITY_DATA[city])
                     
    #Convert start time column to (date and time)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
                                  
    #Extract month and day of wek from start time to create colummns new
    df['month'] =df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
                     
    #filter By month if applicable
    if month !='all':
   
        #Filter by month to create the new dataframe
        df = df[df['month'] == int(month)]
    #Filter by day of week if applicable
    if day != 'all':
    #create the new data ferame day of week
       df = df[df['day_of_week'] == day.title()]                
    
    return df
                     
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("the most common month is ", df['month'].mode(), "\n")

    # TO DO: display the most common day of week
    print("the most common is ", df['day_of_week'].mode(), "]n")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is " +str(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_data = df['Start Station'].mode()[0]
    print("The most commonly used start station is " + str(start_data))
    # TO DO: display most commonly used end station
    end_data = df['End Station'].mode()[0]
    print("The most commonly used end station is " + str(end_data))
   
    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " => " + df['End Station']
    print('the most common comdination: ' + str(df['Trip'].mode()[0]))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is " +  str(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print("The total travel time is " + str(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    preparation = df['User Type'].value_counts()
    print(preparation)
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    else:
        print('Data is not available for chosen city')
        
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('The earliest year: ' + str(df['Birth Year'].min()))
        print('The most recent year: ' + str(df['Birth Year'].max()))
        print('The most common vear: ' + str(df['Birth Year'].mode()))
    else:
        print('Data is nota vailable for city')
        
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()    
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
        start_loc = 0
        while view_data == 'yes':
            print(df.iloc[start_loc:start_loc + 5])
            
            view_data = input(
                "Would you like to view the next 5 rows of individual trip data? Enter yes or no?").lower()
            start_loc += 5
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

        

if __name__ == "__main__":
      main()
