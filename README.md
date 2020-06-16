# CSV generator

### `json_to_csv.py`
```python
# json_to_csv(infile, outfile, sorted_file_keys=None)
# If no sorted_file_keys are provided then csv columns will be 
# based off of first row of data
json_to_csv('sample_med.json', 'sample_med.csv') 

# If sorted_file_keys are provided (list of columns), then 
# those will be the columns which appear in the output csv. 
# Nested columns must be prefixed with the parent key 
# (ex. open_fda -> device_class = open_fda_device_class)
 json_to_csv('device-510k-0001-of-0001.json', 'device-510k-0001-of-0001.csv',
['address_1','address2','advisory_committee','advisory_committee_description','applicant','city','clearance_type','contact','country_code','date_received','decision_code','decision_date','decision_description','device_name','expedited_review_flag','k_number','openfda_device_class','openfda_device_name','openfda_fei_number','openfda_medical_specialty_description','openfda_registration_number','openfda_regulation_number','postal_code','review_adivsory_committee','state','statement_or_summary','third_party_flag','zip_code'])
```