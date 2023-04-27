import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    # get user input for city (chicago, new york city, washington)
    while True:
        city = input("Enter city name (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            return city
        print('Invalid city name, please enter a valid city name.')

def get_month():
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter  month (all, january, february, march, april, may, june): ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            return month
        print('Invalid month, please enter a valid month.')

def get_day():
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter  day (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            return day
        print('Invalid day, please enter a valid day.')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = get_city()
    month = get_month()
    day = get_day()
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1
       df = df[df['month'] == month]
    if day != 'all':
       df = df[df['day_of_week'] == day.title()]
    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month :', common_month)
    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most Common Day Of Week :', common_day_of_week)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour :', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print("Most Commonly Used Start Station :", start_station)

    # display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print("Most Commonly Used End Station :", end_station)

    # display most frequent combination of start station and end station trip
    start_end_station = (df['Start Station'] + ' to ' + df['End Station']).value_counts().idxmax()
    print("Most Frequent Combination Of Start Station And End Station Trip :", start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time :", total_travel_time, "seconds")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time :", mean_travel_time, "seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts Of User Types :", user_types)

    # Display counts of gender
    if 'Gender' in df:
    # Only access Gender column in this case 
        gender_counts = df['Gender'].value_counts()
        print("Counts Of Gender :", gender_counts)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print("Earliest Birth Year :", earliest_birth_year)
        print("Most Recent Birth Year :", most_recent_birth_year)
        print("Most Common Birth Year :", most_common_birth_year)
    else:
        print('Birth Year cannot be calculated because Birth Year does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start_loc = 0
    while True:
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no: ")
        if view_data.lower() != 'yes':
            break
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        if start_loc >= len(df):
            print("You have reached the end of the data.")
            break

def main():
   
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


