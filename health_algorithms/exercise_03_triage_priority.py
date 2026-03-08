"""
EXERCISE: Hospital triage priority

In an emergency deparment, patiens are assigned priority based on the following rules
Conditions  |   Points
BPM > 130   |   +3
SpO2 < 90   |   +4
Temp > 39   |   +2
Age > 70    |   +1

Patient data:
[
 { "name": "Ana", "bpm": 120, "spo2": 88, "temp": 37, "age": 45 },
 { "name": "Luis", "bpm": 140, "spo2": 95, "temp": 40, "age": 72 },
 { "name": "Carlos", "bpm": 85, "spo2": 92, "temp": 36, "age": 30 }
]

Problem
Create an algorithm that:
1. Calculates the triage score for each patient
2. Sorts the patients by priority (highest score first)
3. Return the sorted list
"""

import pprint

def calculate_triage_score_efficient(patient_data: dict) -> int:

    bpm = patient_data.get('bpm')
    spo2 = patient_data.get('spo2')
    temp = patient_data.get('temp')
    age = patient_data.get('age')

    return (
        3 * (bpm > 130)
        + 4 * (spo2 < 90)
        + 2 * (temp > 39)
        + 1 * (age > 70)
    )


def add_triage_to_patient_data(patients_data: list[dict]) -> list[dict]:
    
    return [
        {**patient, "triage": calculate_triage_score_efficient(patient)}
        for patient in patients_data
    ]

def order_by_triage_priority(patients_data: list[dict]) -> list[dict]:
    sorted_patients_list_desc = sorted(patients_data, key = lambda patient: patient['triage'], reverse=True)
    return sorted_patients_list_desc

def solve(patients_data: list[dict]) -> list[dict]:
    triage_patient_data = add_triage_to_patient_data(patients_data)
    patients_data_sorted = order_by_triage_priority(triage_patient_data)
    return patients_data_sorted


if __name__ == '__main__':
    patients_data = [
        { "name": "Ana", "bpm": 120, "spo2": 88, "temp": 37, "age": 45 },
        { "name": "Luis", "bpm": 140, "spo2": 95, "temp": 40, "age": 72 },
        { "name": "Carlos", "bpm": 85, "spo2": 92, "temp": 36, "age": 30 }
    ]
    patients_data_sorted = solve(patients_data)
    pprint.pprint(patients_data_sorted, sort_dicts=False)



    



    