
# coding: utf-8

# In[ ]:

# Import Useful Libraries
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities_to_analyse = ['chicago','new york city','washington']
months_to_analyse = ['january','february','march','april','may','june','all']
day_to_analyse = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']


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
    #To check for correct city input
    while True:
        city = input('Which of the cities would you like to analyse:(Please make sure you type in the correct name of the city): ').lower()
        if city in cities_to_analyse:
            break
        else:
            print('Incorrect city inputted, Please try again by typing "chicago","new york city" or "washington"')


    # TO DO: get user input for month (all, january, february, ... , june)
    #Get input for month
    #To check for correct month input
    print('\n')
    while True:
        month = input('Now, which of the months would you like to analyse? or if you will like to analyse all,Please type "All":(Please make sure you type in the correct name of the month): ').lower()
        if month in months_to_analyse:
            break
        else:
            print('Incorrect month inputted, Please type a correct month or choose "All"')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #Get input for day of week
    #To check for correct day input
    print('\n')
    while True:
        day = input('Also, which of the day would you like to analyse? or if you will like to analyse all,Please type "All":(Please make sure you type in the correct day of the week): ').lower()
        if day in day_to_analyse:
            break
        else:
            print('Incorrect day inputted, Please type a correct day of the week or choose "All"')

    print('-'*40)

    #Displaying the inputs of the User
    if month != 'all' and day != 'all':
        print('You have selected to analyse the City of {0},for the Month of {1} for the days of {2}'.format(city.title(),month.title(),day.title()))
    elif month == 'all' and day != 'all':
        print('You have selected to analyse the City of {0},for All the Months and for the days of {1}'.format(city.title(),day.title()))
    elif month != 'all' and day == 'all':
        print('You have selected to analyse the City of {0},for the Month of {1} and for All the days'.format(city.title(),month.title()))
    elif month == 'all' and day == 'all':
        print('You have selected to analyse the City of {0},for All the Months and for All the days'.format(city.title()))
    return city.lower(), month.title(), day.title()


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

    #Extract month and day of the week from start time into different columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour

    # filter by month or all if applicable
    if month != 'All':
        df = df[df.month== month]
        result = df
    else:
        result = df
    # filter by day or all if applicable
    if day != 'All':
        df = df[df.day == day]
        result = df
    else:
        result = df
    df = result

    # Give the user the option of viewing a chunk or all of the available data

    while True:
        user_response = input('If you will like to view ALL of the information available for the selected city({0}),month({1}) and day({2}), type "ALL"         \nELSE, type "FIVE" to view the FIRST FIVE ROWS                  \nELSE, type "NONE" to continue:  '.format(city.title(),month,day))
        if user_response.lower() == 'all' or 'five' or 'none':
            break
        else:
            print('***********Incorrect input, Please type "All" or "Five" or "None"****************')
    start_location = 0
    if user_response.lower() == 'all':
        print(df)
    elif user_response.lower() == 'five':
        while user_response.lower() == 'five':
            print(df.iloc[start_location:(start_location + 5)])
            start_location += 5
            while True:

#Give the user the option of viewing more rows of data or continuing with the program
                view_display = input("Do you wish to continue with the rest of the code, Type 'CONTINUE' \nOR \nIf you want to view the next 5 Rows of information available for the selected city({0}),month({1}) and day({2}), type 'FIVE'".format(city.title(),month,day))
                if view_display.lower() =='continue':
                    break
                elif view_display.lower() =='five':
                    print('Displaying Rows {0} to {1}'.format(start_location,start_location + 5))
                    print(df.iloc[start_location:(start_location + 5)])
                    start_location += 5
                else:
                    print('**********Incorrect input, Please type "Continue" or "Five"********************')
            break
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\n')
    print('\nCALCULATING THE MOST FREQUENT TIME OF TRAVEL...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    most_common_month = 'The most common Month for {0} during the specified month ({1}) and specified day ({2}) is {3}: '.format(city.title(),month,day,most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day'].mode()[0]
    most_common_day_of_week = 'The most common Day of Week for {0} during the specified month ({1}) and specified day ({2}) is {3}: '.format(city.title(),month,day,most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hour = df['start_hour'].mode()[0]
    most_common_start_hour = 'The most common Start Hour for {0} during the specified month ({1}) and specified day ({2}) is {3}: '.format(city.title(),month,day,most_common_start_hour)

    print(most_common_month)
    print('\n{0}'.format(most_common_day_of_week))
    print('\n{0}'.format(most_common_start_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\n')
    print('\nCALCULATING THE MOST POPULAR STATION AND TRIP...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    most_used_start_station = 'The most commonly used Start Station for {0} during the specified month ({1}) and specified day ({2}) is {3}: '. format(city.title(),month,day,most_used_start_station)

    # TO DO: display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]
    most_used_end_station = 'The most commonly used End Station for {0} during the specified month ({1}) and specified day ({2}) is {3}: '. format(city.title(),month,day,most_used_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_used_start_and_end_station = (df['Start Station'] + ' ' + df['End Station']).mode()[0]
    most_used_start_and_end_station = 'The most commonly used Start and End Station for {0} during the specified month ({1}) and specified day ({2}) is {3}: '. format(city.title(),month,day,most_used_start_and_end_station)
    print(most_used_start_station)
    print('\n{0}'.format(most_used_end_station))
    print('\n{0}'.format(most_used_start_and_end_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCALCULATING TRIP DURATION...\n')
    start_time = time.time()

    # To fill up the NaN values with the mean of the values
    df = df.fillna(df['Trip Duration'].mean())

    # TO DO: display total travel time
    total_time_travel = df['Trip Duration'].sum()
    ttm, tts = divmod(total_time_travel, 60)
    tth, ttm = divmod(ttm, 60)


    # TO DO: display mean travel time
    average_time_travel = df['Trip Duration'].mean()
    atm, ats = divmod(average_time_travel, 60)
    ath, atm = divmod(atm, 60)
    print('The Total Travel Time for {0} during the specified month ({1}) and specified day ({2}) is {3} hours,{4} minutes: '. format(city.title(),month,day,tth,ttm))
    print('\nThe Average Travel Time for {0} during the specified month ({1}) and specified day ({2}) is {3} hours,{4} minutes: '. format(city.title(),month,day,ath,atm))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_types = df['User Type'].value_counts()
        user_types = 'The Count for the Several User Types for {0} during the specified month ({1}) and specified day ({2}) are \n{3}: '.format(city.title(),month,day,user_types)
    except:
        user_types = 'There is no information about User Type in the city of {0}'.format(city.title())


    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        gender_count = 'The Count of the Several Gender for {0} during the specified month ({1}) and specified day ({2}) are \n{3}: '.format(city.title(),month,day,gender_count)
    except:
        gender_count = 'There is no information about Gender in the city of {0}'.format(city.title())


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        result = 'For {0}, during the specified month ({1}) and specified day ({2}) \nThe Earliest Birth Year is: {3} \nThe Most Recent Birth Year is: {4} and \nThe Most Common Birth Year is: {5} '.format(city.title(),month,day,earliest_birth_year,most_recent_birth_year,most_common_birth_year)
    except:
        result = 'There is no information about Birth Year in the city of {0}'.format(city.title())


    print(user_types)
    print('\n{0}'.format(gender_count))
    print('\n{0}'.format(result))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


while True:
    city,month,day = get_filters()
    df = load_data(city,month,day)

    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
        break
