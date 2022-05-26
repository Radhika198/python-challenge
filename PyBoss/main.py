import os
import csv

#The State data dictionary for full state name to two-letter abbreviations.
state_abbreviation = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Reading imput data from employee_data.csv file
csv_file_path = os.path.join('Resources', 'employee_data.csv')
with open(csv_file_path, newline='') as csv_input_file:
    csv_reader = csv.reader(csv_input_file, delimiter=',')
    next(csv_reader,None) 

#output of employee data conversion into employee_data_conversion.csv file
    output_path = os.path.join('EmployeeConvertedData', 'employee_data_conversion.csv')
    with open(output_path, 'w', newline='') as csv_output_file:
        csv_output_writer = csv.writer(csv_output_file, delimiter=',')
        #Output file header for converted  employee data
        csv_output_writer.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
        for row in csv_reader:
            emp_name = row[1].split(' ')  #Name value split into two values, then it will become first name and last name
            emp_dob = row[2].split('-')   #DOB split into Date,Month and Year based on "-" symbol
            emp_ssn = row[3].split('-')   #SSN number split based on "-" symbol
            #Output of employee conversion based on the requirements
            output = [row[0],emp_name[0],emp_name[1],f"{emp_dob[1]}/{emp_dob[2]}/{emp_dob[0]}",f"***-**-{emp_ssn[2]}",state_abbreviation[row[4]]]
            csv_output_writer.writerow(output)