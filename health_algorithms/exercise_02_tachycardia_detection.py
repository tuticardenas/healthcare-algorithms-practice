"""
EXERCISE 2: Tachycardia Detection
A patient has a heart rate readings recorded every minute for oe hour.

Simplified medical rule:
Tachycardis occurs when BPM > 100 for at least 5 consecutiveminutes.

Example data:
[80, 85, 90, 105, 110, 115, 108, 102, 95, 88]

Create an algorithm that detects:
- Wheter tachycardia occurred
- The minute when it started
- How long it lasted

Expected output:
{
  "tachycardia_detected": True,
  "start_minute": 3,
  "duration": 5
}



"""
import pprint

def solve(readings: list[int]) -> dict:
    start_minute: int = None
    duration = 0

    for i, bpm in enumerate(readings):
        
        if bpm > 100:
            if duration == 0:
                start_minute = i
            duration += 1
            continue

        if duration >= 5:
            return {
                "tachycardia_detected": True,
                "start_minute": start_minute,
                "duration": duration
            }
        
        duration = 0
    
    # If the streaks ends at the end of the list
    if duration >= 5:
        return {
            "tachycardia_detected": True,
            "start_minute": start_minute,
            "duration": duration
        }
    
    return {
        "tachycardia_detected": False,
        "start_minute": None,
        "duration": 0
    }


if __name__ == '__main__':
    heart_rate_readings = [80, 85, 90, 105, 110, 115, 108, 102, 95, 88]
    results = solve(heart_rate_readings)
    pprint.pprint(results, sort_dicts=False, width=1)


        












