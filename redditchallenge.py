#I challenge you to write a program that calculates total job years experience.

#You will need to prompt for: company name, start date, end date.

#Compute the total years experience for each company

#Print all companies, start, end date, total experience in years

#And finally add up all the years from all companies to figure out the total number of years.

#Bonus:

#Allow the user to remove entries

#Super bonus :

#Store the entries in a text file or sql-lite db So you save the entries

#Why? (also hints on how to achieve this)

#This will teach you how to use datetime libraries How to use and iterate through dicts and tuples or lists (depending on your approach)

#Converting strings to datetime objects Suming of tuple/list values How to sort dicts by key values

#If you find datetime too complex you can use pendelum. In which case you get introduced to pip as well.

#Estimated time to completion 3 days - 2 weeks Depending on how fast you pick up

# Name of said company
def get_company_name():
    global company_name
    company_name = input('Hello user, please list a company you had worked for:')

# Date started working for said company
def get_start_date():
    import datetime
    global total_start_date
    start_date_year = input(f'Now, please input the YEAR you started working for {company_name} in the following format' + '(YYYY)')
    start_date_month = input(f'Next, please input the MONTH you started working {company_name} in the following format' + '(M)')
    start_date_day = input(f'Next, please input the DAY you started working for {company_name} in the following format' + '(D)')
    users_input_start_date = datetime.date(int(start_date_year),int(start_date_month),int(start_date_day))
    total_start_date = (users_input_start_date)

# Date ended working for said company
def get_end_date():
    import datetime
    global total_end_date
    end_date_year = input(f'Now, please input the YEAR you stopped working for {company_name} in the following format' + '(YYYY)')
    end_date_month = input(f'Next, please input the MONTH you stopped working for {company_name} in the following format' + '(M)')
    end_date_day = input(f'Next, please input the DAY you stopped working for {company_name} in the following format' + '(D)')
    users_input_end_date = datetime.date(int(end_date_year),int(end_date_month),int(end_date_day))
    total_end_date = (users_input_end_date)

file_object = open("companyname.txt","w")
while True:
    get_company_name()
    file_object.write(f'Company you had worked for: {company_name}\n')
    get_start_date()
    file_object.write(f'Date you started working for {company_name}: {total_start_date}\n')
    get_end_date()
    file_object.write(f'Date you stopped working for {company_name}: {total_end_date}\n')
    file_object.write(f'Number of days you worked for {company_name}: {(total_end_date - total_start_date).days}\n')
    add_another_company = input('Would you like to add another company? Type yes or no:')
    if add_another_company == 'no':
        break
file_object.close()



    




