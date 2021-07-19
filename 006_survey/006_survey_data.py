import pandas as pd

def user_menu():
    df = pd.read_csv('survey_results_public.csv')
    user_choice = input('Please choose\n'
          '1.Number of prof and hobby developers\n'
          '2.The age of developers\n'
          '3.Developers by country\n'
          '4.By currency\n'      
          '0.Exit\n'
          '-->')
    if user_choice == '1':
        print_prof_hobby(df)
    elif user_choice == '2':
        print_age(df)
    elif user_choice == '3':
        print_countries(df)
    elif user_choice == '4':
        print_currency(df)
    elif user_choice == '0':
        print('Good bye!')
        exit()
    else:
        print('Print choice out of range')
        user_menu()


def print_prof_hobby(df):
    new_df = df['Hobbyist'].value_counts()
    print(f'There are {new_df.iloc[0]} developers by profession and {new_df.iloc[1]}/'
          f' code as a hobby of {df.shape[0]} respondets in total.')


def print_age(df):
    min_age = int(df['Age'].min())
    max_age = int(df['Age'].max())
    average_age = int(df['Age'].mean())
    print(f'The maximum age is {max_age}\n'
          f'The minimum age is {min_age}\n'
          f'The average age is {average_age}')


def print_countries(df):
    print(df['Country'].value_counts())


def print_currency(df):
    print(df['CurrencyDesc'].value_counts())


user_menu()