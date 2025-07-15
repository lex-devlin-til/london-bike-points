from extract_bike_points import extract_bike_points
from load_bike_points import load_bike_points

print('Extracting Bike Point data from Transport for London Unified API, loading to S3...')
extract_bike_points()
load_bike_points()