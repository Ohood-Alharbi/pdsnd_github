import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
 def about_dataset():
 print ("The datasets randomly selected data for the first six months of 2017 are provided for all three cities. \
    All three of the data files contain the same core six (6) columns:\
Start Time (e.g., 2017-01-01 00:07:57)\
End Time (e.g., 2017-01-01 00:20:53)\
Trip Duration (in seconds - e.g., 776)\
Start Station (e.g., Broadway & Barry Ave)\
End Station (e.g., Sedgwick St & North Ave)\
User Type (Subscriber or Customer)\
The Chicago and New York City files also have the following two columns:\
Gender\
Birth Year")            

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
        city = input('Enter a city [chicago, new york city or washington]to analyze its data:\n').lower()
        if city not in CITY_DATA:
            print("Sorry, the name of the city unavailable, try again!")
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter a month [all, january, february, march, april, may, june],'all' to analyze all fisrt six months:\n").lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month != 'all' and month not in months:
            print("Sorry, the name of the month unavailable, try again!")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter a day [all, monday, tuesday, wednesday, thursday, friday, saturday, sunday],'all' to analyze all days:\n").lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day != 'all' and day not in days:
            print("Sorry, the name of the day unavailable, try again!")
        else:
            break

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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day) + 1
        # filter by day of week to create the new dataframe
        df = df[df['weekday'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is: ', common_month)
    
    # TO DO: display the most common day of week
    common_day = df['weekday'].mode()[0]
    print('The most common day is: ', common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_start_end_station_combination = (df['Start Station'] + ' : ' + df['End Station']).mode()[0]
    print('most frequent start end station combination is: ', frequent_start_end_station_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    #Extract the duration in minutes and seconds format
    minute, second = divmod(total_duration, 60)
    #Extractthe duration in hour and minutes format
    hour, minute = divmod(minute, 60)
    print("The total trip duration is: {} and in hours is {} hours {} minutes {} seconds.\n".format(total_duration,hour, minute, second))

    # TO DO: display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean())
    #Extract the duration in minutes and seconds format
    avg_minute, avg_second = divmod(mean_travel_time, 60)
    #Extract the duration in hour and minutes format
    avg_hour, avg_minute = divmod(avg_minute, 60)
    print('The average travel time is: {} and in hours is {} hours {} minutes {} seconds.\n'. format(mean_travel_time, avg_hour, avg_minute, avg_second))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types are:\n" + str(user_types))
    print('-'*40)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('The number of male and female are:\n', gender)
        print('-'*40)
    except:
        print('This city does not has a data for Gender')
        print('-'*40)

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()
        print('Earliest birth year is: {}\n'.format(earliest_birth))
        print('Most recent birth year is: {}\n'.format(most_recent_birth))
        print('Most common birth year is: {}\n'.format(most_common_birth))
    except:
        print('This city does not has a data for Birth Year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
Raw data is displayed upon request by the user in the following manner:

Your script should prompt the user if they want to see 5 lines of raw data,
Display that data if the answer is 'yes',
Continue iterating these prompts and displaying the next 5 lines of raw data at each iteration,
Stop the program when the user says 'no' or there is no more raw data to display.

Args:
        df - panda dataframe returned from filtering by city month and/or day
        choice - yes or no based on user decision
    """
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    keep_asking = True
    
    while (keep_asking):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        if view_data == "no":
            keep_asking = False
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
