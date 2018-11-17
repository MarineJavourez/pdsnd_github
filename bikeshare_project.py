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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('First, please choose a city : chicago, new york city or washington? ')
    flag = True
    while flag:
        if (city == 'chicago') or (city == 'new york city') or (city == 'washington'):
            flag = False
            break
        if ((city != 'chicago') or (city != 'new york city') or (city != 'washington')):
            city = input('You didn\'t enter a correct answer, try again : chicago, new york city or washington? ')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Excellent choice!\nWhich month? all, january, february, march, april, may or june? ')
    flag = True
    while flag:
        if (month == 'all') or (month == 'january') or (month == 'february') or (month == 'march') or (month == 'april') or (month == 'may') or (month == 'june'):
            flag = False
            break
        if(month != 'all') or (month != 'january') or (month != 'february') or (month != 'march') or (month != 'april') or (month != 'may') or (month != 'june'):
            month = input('You didn\'t enter a correct answer, try again : all, january, february, march, april, may or june? ')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Perfect!\nJust one more thing, which day of week? all, monday, tuesday, wednesday, thursday, friday, saturday or sunday? ')
    flag = True
    while flag:
        if (day == 'all') or (day == 'monday') or (day == 'tuesday') or (day == 'wednesday') or (day == 'thursday') or (day == 'friday') or (day == 'saturday') or (day == 'sunday'):
            flag = False
            break
        if (day != 'all') or (day != 'monday') or (day != 'tuesday') or (day != 'wednesday') or (day != 'thursday') or (day != 'friday') or (day != 'saturday') or (day != 'sunday'):
            day = input('You didn\'t enter a correct answer, try again : all, monday, tuesday, wednesday, thursday, friday, saturday or sunday? ')

    print('Thank you very much! Let\'s see what I\'ve got for you...\n')
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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day of week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The month that our riders prefer to cycle is {}.'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day of week'].mode()[0]
    print('The day they prefer is {}.'.format(popular_day))

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The best hour to ride is {}.'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular station to start a ride is {}...'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['Start Station'].mode()[0]
    print('And the best station to finish on a high note is {}.'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station']+' - '+df['End Station']
    popular_trip = df['Trip'].mode()[0]
    print('To conclude, the best trip ever is {}!'.format(popular_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Our riders have cycled a total of {} secondes!'.format(total_travel))

    # TO DO: display mean travel time
    average_travel = df['Trip Duration'].mean()
    print('The time of an average trip is {} seconds.'.format(average_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    suscriber = df['User Type'].value_counts()[0]
    print('{} of our riders are suscribers.'.format(suscriber))

    customer = df['User Type'].value_counts()[1]
    print('And {} are customers without any subscription.\n'.format(customer))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        number_of_men = df['Gender'].value_counts()[0]
        number_of_women = df['Gender'].value_counts()[1]
        if number_of_men > number_of_women:
            print('It seems like men enjoy pedaling more than women!')
        elif number_of_men < number_of_women:
            print('It seems like women enjoy pedaling more than men!')
        else:
            print('It seems like both women and men enjoy pedaling!')
        print('{} women and {} men borrowed a bike.\n'.format(number_of_women, number_of_men))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        current_year = pd.datetime.now().year
        earliest_year = df['Birth Year'].min()
        oldest = current_year - earliest_year
        print('Our oldest biker is {} years old. Congrats!'.format(oldest))
        recentest_year = df['Birth Year'].max()
        youngest = current_year - recentest_year
        print('Our youngest biker is {} years old.'.format(youngest))
        most_commun_year = df['Birth Year'].mode()[0]
        commun_age = current_year - most_commun_year
        print('The most commun age is {}.'.format(commun_age))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    raw_data = input("Do you want to see raw data? yes or no " )
    i = 0
    if raw_data.lower() == 'yes':
        print(df.iloc[i:i + 5])
        more_raw_data = input("Do you want to see more 5 lines of raw data? yes or no")
        while more_raw_data.lower() == 'yes':
            i += 5
            print(df.iloc[i:i + 5])
            more_raw_data = input("Do you want to see more 5 lines of raw data? yes or no")

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
