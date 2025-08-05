"""
Problem: 0611. Valid Trip Cancellations (Pandas)
Link: https://leetcode.com/problems/valid-trip-cancellations/

Description:
    Write a solution to find the cancellation rate for each day, excluding trips with banned clients or drivers.

Approach:
    Merge trips and users, filter out banned users, flag cancellations, and aggregate by day.

Time Complexity: O(N)
Space Complexity: O(N)
"""

import pandas as pd

def trips_and_users_two(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    clients = users.loc[users['role'] == "client"]
    drivers = users.loc[users['role'] == "driver"]
    merged_with_clients = pd.merge(trips, clients[['users_id', 'banned']], left_on='client_id', right_on='users_id')
    merged_with_drivers_clients = pd.merge(
        merged_with_clients,
        drivers[['users_id', 'banned']],
        left_on='driver_id', right_on='users_id',
        suffixes=('_clients', '_drivers')
    )
    merged = merged_with_drivers_clients[['client_id', 'driver_id', 'status', 'request_at', 'banned_clients', 'banned_drivers']].copy()
    merged = merged.loc[(merged['banned_clients'] != 'Yes') & (merged['banned_drivers'] != 'Yes')][[
        'client_id', 'driver_id', 'status', 'request_at']]
    counts = merged.groupby('request_at')['request_at'].count()
    merged['requests'] = merged['request_at'].map(counts)
    merged['is_canceled'] = merged['status'].map({'completed': False, 'cancelled_by_client': True, 'cancelled_by_driver': True})
    grouped_summed = merged.groupby('request_at')['is_canceled'].sum().reset_index(drop=True)
    grouped_unique = merged.groupby('request_at')['requests'].first().reset_index(drop=True)
    return pd.DataFrame({'Day': merged['request_at'].unique(),
                         'Cancellation Rate': (grouped_summed / grouped_unique).round(2)})

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    users_ok = users[users['banned'] == 'No']
    clients = users_ok[users_ok['role'] == 'client'][['users_id']]
    drivers = users_ok[users_ok['role'] == 'driver'][['users_id']]
    trips_ok = (
        trips
        .merge(clients, left_on='client_id', right_on='users_id')
        .merge(drivers, left_on='driver_id', right_on='users_id', suffixes=('_c', '_d'))
    )
    trips_ok['is_canceled'] = trips_ok['status'].ne('completed')
    daily = (
        trips_ok
        .groupby('request_at')
        .agg(total=('status', 'size'),
             canceled=('is_canceled', 'sum'))
        .assign(Cancellation_Rate=lambda d: (d['canceled'] / d['total']).round(2))
        .reset_index(names=['Day'])
        [['Day', 'Cancellation_Rate']]
        .sort_values('Day', ignore_index=True)
    )
    return daily

if __name__ == "__main__":
    # --- Trips Table ---
    trips_data = {
        "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "client_id": [1, 2, 3, 4, 1, 2, 3, 2, 3, 4],
        "driver_id": [10, 11, 12, 13, 10, 11, 12, 12, 10, 13],
        "city_id": [1, 1, 6, 6, 1, 6, 6, 12, 12, 12],
        "status": [
            "completed", "cancelled_by_driver", "completed", "cancelled_by_client",
            "completed", "completed", "completed", "completed", "completed", "cancelled_by_driver"
        ],
        "request_at": ["2013-10-01", "2013-10-01", "2013-10-01", "2013-10-01",
                       "2013-10-02", "2013-10-02", "2013-10-02", "2013-10-03",
                       "2013-10-03", "2013-10-03"]
    }
    trips = pd.DataFrame(trips_data)

    # --- Users Table ---
    users_data = {
        "users_id": [1, 2, 3, 4, 10, 11, 12, 13],
        "banned": ["No", "Yes", "No", "No", "No", "No", "No", "No"],
        "role": ["client", "client", "client", "client", "driver", "driver", "driver", "driver"]
    }
    users = pd.DataFrame(users_data)
    pd.set_option('display.max_columns', None)
    print(trips_and_users(trips, users))
