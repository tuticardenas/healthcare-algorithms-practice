"""
EXERCISE 1: Basic vital signs filtering

An hospital gathers cardiac freqeuncy lectures from a patient every minute.
However, some sensors are not working properly and they can give wrong values.

Possibles physological values:
- min: 40 bpm
- max: 180 bpm

Given the following lectures: [72, 75, 300, 74, 73, 20, 76, 78]
Write an algorithm that:
1. Remove the wrong values outisde the physiological range.
2. Calculate the average of cardiac frequency
3. Get the maximun value of cardiac frequency
4. Get the minimum value of cardiac frequency

Expected output:
{
  "clean_readings": [...],
  "average_bpm": ...,
  "max_bpm": ...,
  "min_bpm": ...
}
"""

import pprint

def filter_vital_signs(readings: list[int]) -> dict:
    # Step 1: Remove wrong values outside the physilogical range
    clean_readings = [frequency for frequency in readings if 40 <= frequency <= 180]
    return {"clean_readings": clean_readings}

def calculate_average_bpm(clean_readings: list[int]) -> dict:
    # Step 2: Calculate the average of cardiac frequency

    if not clean_readings:
        return {"average_bpm": 0.0}
    
    average_bpm = sum(clean_readings) / len(clean_readings)
    return {"average_bpm": average_bpm}

def calculate_max_bpm(clean_readings: list[int]) -> dict:
    # Step 3: Get the maximum value of cardiac frequency
    if not clean_readings:
        return {"max_bpm": 0}
    max_bpm = max(clean_readings)
    return {"max_bpm": max_bpm}

def calculate_min_bpm(clean_readings: list[int]) -> dict:
    # Step 4: Get the minimum value of cardiac frequency
    if not clean_readings:
        return {"min_bpm": 0}
    min_bpm = min(clean_readings)
    return {"min_bpm": min_bpm}

def solve(readings: list[int]) -> dict:
    clean_data = filter_vital_signs(readings)
    average_data = calculate_average_bpm(clean_data["clean_readings"])
    max_data = calculate_max_bpm(clean_data["clean_readings"])
    min_data = calculate_min_bpm(clean_data["clean_readings"])

    return {
        **clean_data,
        **average_data,
        **max_data,
        **min_data
    }

if __name__ == "__main__":
    readings = [72, 75, 300, 74, 73, 20, 76, 78]
    result = solve(readings)
    pprint.pprint(result, sort_dicts=False)
