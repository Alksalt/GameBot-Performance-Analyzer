import pandas as pd

def patients_with_condition(patients: pd.DataFrame) -> pd.DataFrame:
    patients = patients.copy()
    return patients.loc[patients["conditions"].str.contains(r'\bDIAB1\b')]

# Example 1
data1 = {
    "patient_id": [1, 2, 3],
    "patient_name": ["Alice", "Bob", "Charlie"],
    "conditions": ["DIAB1", "DIAB1, COPD", "COPD, DIAB1"]
}
patients1 = pd.DataFrame(data1)

# Example 2
data2 = {
    "patient_id": [4, 5, 6],
    "patient_name": ["Diana", "Eve", "Frank"],
    "conditions": ["COPD", "DIAB1A", "asthma, DIAB1"]
}
patients2 = pd.DataFrame(data2)

# Example 3
data3 = {
    "patient_id": [7, 8, 9],
    "patient_name": ["Grace", "Heidi", "Ivan"],
    "conditions": ["DIAB1, asthma", "asthma", "DIAB1B, COPD"]
}
patients3 = pd.DataFrame(data3)

if __name__ == "__main__":
    print(patients_with_condition(patients1.copy()))
    print()
    print(patients_with_condition(patients2.copy()))
    print()
    print(patients_with_condition(patients3.copy()))