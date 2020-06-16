import bigjson
import csv

# Recursively compile records from json into a single non nested dictionary 
# key - CSV column name
# value - raw value from reading json
# compiled_data - dictionary in which to store all data
def parse_data(key, value, compiled_data):
    # bigjson returns unicode strings so keys and values must be utf-8 encoded
    parsed_key = key.encode('utf-8')
    if isinstance(value, unicode):
        compiled_data[parsed_key] = value.encode('utf-8')
    elif isinstance(value, dict):
        # If value is a dictionary, recursively parse and add each key of the
        # dictionary to compiled_data, prefixed with the key for the original value
        for innerkey in value.keys():
            parse_data(parsed_key+"_"+innerkey, value[innerkey], compiled_data)
    elif isinstance(value, list):
        # If value is a list then combine list values into single comma-separated string
        compiled_data[parsed_key] = ', '.join(list(map(lambda x:x.encode('utf-8'), value)))
    else:
        compiled_data[parsed_key] = value

# Convert json file into csv file
# infile - relative path of file to input
# outfile - relative path of file to output
# sorted_file_keys - keys to search for in json to output into csv
def json_to_csv(infile, outfile, sorted_file_keys=None):
    with open(infile, 'rb') as f, open(outfile,"a") as csvfile:
        # Read infile with bigjson and init csv writer
        data = bigjson.load(f)
        writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
        # Counter for tracking number of completed rows
        completed_row_count = 0
        for json_row in data:
            # Convert bigjson object to python dictionary 
            row = json_row.to_python()
            compiled_data = {}
            # Parse each key and add to compiled_data
            for key in row.keys():
                parse_data(key, row[key], compiled_data)
            # If no sorted_file_keys are provided, then the keys of the first row are selected
            if sorted_file_keys is None:
                sorted_file_keys = list(sorted(compiled_data.keys()))
            # Print column headers to file
            if completed_row_count == 0:
                writer.writerow(sorted_file_keys)
            # Sort compiled data and print to csv
            sorted_compiled_data = [compiled_data.get(key,'') for key in sorted_file_keys]
            writer.writerow(sorted_compiled_data)
            completed_row_count += 1


            


# json_to_csv('device-510k-0001-of-0001.json', 'device-510k-0001-of-0001.csv',
# ['address_1','address2','advisory_committee','advisory_committee_description','applicant',
# 'city','clearance_type','contact','country_code','date_received','decision_code','decision_date','decision_description',
# 'device_name','expedited_review_flag','k_number','openfda_device_class','openfda_device_name','openfda_fei_number',
# 'openfda_medical_specialty_description','openfda_registration_number','openfda_regulation_number','postal_code',
# 'review_adivsory_committee','state','statement_or_summary','third_party_flag','zip_code'])
json_to_csv('sample_med.json', 'sample_med.csv')
