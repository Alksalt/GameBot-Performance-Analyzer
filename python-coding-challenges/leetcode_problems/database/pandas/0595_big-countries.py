"""
Problem: 0595. Big Countries (Pandas)
Link: https://leetcode.com/problems/big-countries/

Description:
    Write a solution to find the name, population, and area of the big countries.
    A country is considered big if:
        - It has an area of at least three million (i.e., 3000000 km2), OR
        - It has a population of at least twenty-five million (i.e., 25000000).

Approach:
    Use pandas boolean indexing with vectorized conditions to select rows where either
    'area' >= 3,000,000 or 'population' >= 25,000,000. Select only the 'name', 'area',
    and 'population' columns for the output.

Time Complexity: O(N)
Space Complexity: O(N)
"""

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[["name", "area", "population"]].loc[
        (world["area"] >= 3000000) | (world["population"] >= 25000000)
    ]

if __name__ == "__main__":
    # Example setup for the World table
    data = {
        "name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
        "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
        "area": [652230, 28748, 2381741, 468, 1246700],
        "population": [25500100, 2831741, 37100000, 78115, 20609294],
        "gdp": [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]
    }
    df = pd.DataFrame(data)
    print(big_countries(df))


