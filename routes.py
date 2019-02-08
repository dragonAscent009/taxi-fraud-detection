import pandas
import os

train_df=pandas.read_csv('all-air-to-train-routes-with-500-cells.csv')
air_df=pandas.read_csv('all-train-to-air-routes-with-500-cells.csv')

train_route_ids = train_df['route_number'].unique()
air_route_ids = air_df['route_number'].unique()

print(len(train_route_ids))
print(len(air_route_ids))

routes = []


def find_routes_with_ten_readings(df, route_numbers, min_num_readings=10):
    routes = []

    for number in route_numbers:
        route_df = df[df['route_number'] == number]

        if len(route_df) >= min_num_readings:
            routes.append(route_df)
        else:
            print('Route: ', number, ' only has ', len(route_df), ' readings!')

    print('Found ', len(routes), ' routes that have 10+ readings')

    return pandas.concat(routes)
sample = find_routes_with_ten_readings(train_df, train_route_ids, min_num_readings=10)
sample2 = find_routes_with_ten_readings(air_df, air_route_ids, min_num_readings=10)

#sample.to_csv('long_routes_t2a_500.csv')
#sample2.to_csv('long_routes_a2t_500.csv')
#print(sample)
