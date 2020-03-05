# User can find out how many days in a month.

month = (input('Input 3 letter month abbreviation: ')).lower()
month_dict = {'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30, 'may': 31, 'jun': 30, 'jul': 31, 'aug': 31, 'sep': 30,
              'oct': 31, 'nov': 30, 'dec': 31}


def num_days(item):
    for key in month_dict:
        if key == item:
            print('Number of days in', item.title(), 'is', month_dict[month])


num_days(month.lower())
