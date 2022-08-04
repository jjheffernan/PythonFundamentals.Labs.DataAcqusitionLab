# import urllib.request
from urllib import request
import json
# using urllib make rest calls to NOAA's API and save the results to json files

# once executed, there should be 39 files.
# JSON objects named 'locations_x.json' numbered 0-38

# Be careful not to overexhaust the allotted calls due to bugs

# URL for calls
url_string = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/'

json_list = []  # global list of json objects
spec_path = ''  # filepath for saving objects

# get URL from input or from file
def call_url(url_string: str):
    # opened specified URL
    # noaa_url = url_string
    request.urlopen(url=url_string)
    # store the url as object


# store json files from specified url
def load_page():
    # load HTML body into list of json objects
    web_data = []  # list of json objects within body


# save resultant json list to appropriately named files
def handle_json():
    print('handling json files...')
    # iterate through json list, to develop objects
    for item in json_list:
        # get string for json file locations_x.json
        # use the item iterable as the number for locations_x
        filename = 'locations_' + item  # iterated final string of filename appended with .json
        # create new json file in specific path using string
        print(f'creating json file {filename} at {spec_path}')
        # open json file
        f = open(file=filename)
        # dump contents of URL into JSON file
        data = json.loads(f.read())
        print(type(data), data) # debug status, to confirm all JSON files within json list
        # save json file
        output_filename = filename + '.json'
        print(f'saving file {filename} at {spec_path}')
        file_out = open(output_filename, "w")  # opening output file for modification
        file_out.write(json.dumps(data))  # writing output to file
        # close json file
        f.close()
        file_out.close()
    # close all files.
    #
    print('done with json.')
    # pass # escape pass

def main():
    # call everything here. This will be accessible via CLI
    # call_url # DO NOT UNCOMMENT UNLESS NO BUGS
    pass


if __name__ == "__main__":
    # CLI call `python3 make_requests.py`
    main()
