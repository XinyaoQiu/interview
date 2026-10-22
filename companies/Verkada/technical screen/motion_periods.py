"""
Problem: Motion Detection Periods

Part 1: Given sorted (timestamp, motion_intensity) pairs and a threshold,
return inclusive [start, end] periods where motion is at or above the threshold.

Part 2: Given multiple streams, return the periods where ALL cameras meet
the threshold at the same time.

Assumptions to confirm with the interviewer:
- Input is valid; intensities and the threshold are between 0 and 1.
- Timestamps strictly increase within each stream and use a shared time axis.
- A consecutive run of qualifying samples represents a closed interval from
  its first timestamp to its last timestamp, including the time between them.
  A below-threshold sample ends the run at the previous qualifying timestamp.
- A single qualifying sample produces [timestamp, timestamp]. Do not extend
  intervals beyond qualifying samples or interpolate threshold crossings.
- Cameras may sample at different times; intersect their inferred intervals.
- No cameras, or any empty stream, produces no common periods.

Approach:
Part 1: Track the first and last timestamps of each qualifying run.
Part 2: Extract intervals for each camera, then intersect them one camera at
a time with two pointers. Inclusive intervals overlap when start <= end.

Complexity:
Part 1: O(n) time, O(1) auxiliary space excluding the O(n) output.
Part 2: O(K * N) worst-case time and O(N) space, where K is the number of
cameras and N is the total number of samples. Intermediate intersections can
contain O(N) intervals and may be scanned again for subsequent cameras.
"""


def motion_periods(stream, threshold):
    periods = []
    start = None
    end = None

    for timestamp, intensity in stream:
        if intensity >= threshold:
            if start is None:
                start = timestamp
            end = timestamp
        elif start is not None:
            periods.append([start, end])
            start = None

    if start is not None:
        periods.append([start, end])

    return periods


def intersect_periods(first, second):
    result = []
    i = j = 0

    while i < len(first) and j < len(second):
        start = max(first[i][0], second[j][0])
        end = min(first[i][1], second[j][1])
        if start <= end:
            result.append([start, end])

        # The interval ending first cannot overlap any later interval
        # in the other list, so advance its pointer.
        if first[i][1] < second[j][1]:
            i += 1
        else:
            j += 1

    return result


def common_motion_periods(streams, threshold):
    if not streams:
        return []

    common = motion_periods(streams[0], threshold)
    for stream in streams[1:]:
        if not common:
            break
        common = intersect_periods(common, motion_periods(stream, threshold))

    return common


# Part 1: threshold equality, separated runs, and a final qualifying sample.
print(motion_periods([
    (1, 0.2), (2, 0.5), (3, 0.8), (4, 0.1), (5, 0.9),
], 0.5))  # [[2, 3], [5, 5]]
print(motion_periods([(1, 0.1), (2, 0.2)], 0.5))  # []
print(motion_periods([(1, 0.7), (2, 0.8)], 0.5))  # [[1, 2]]
print(motion_periods([], 0.5))  # []

# Part 2: different sampling times and three cameras.
print(common_motion_periods([
    [(1, 0.9), (5, 0.8), (6, 0.1), (8, 0.7), (10, 0.9)],
    [(2, 0.6), (4, 0.9), (5, 0.1), (9, 0.8), (12, 0.7)],
    [(3, 0.9), (10, 0.9)],
], 0.5))  # [[3, 4], [9, 10]]

# Inclusive endpoints can intersect at a single timestamp.
print(common_motion_periods([
    [(1, 0.9), (3, 0.9)],
    [(3, 0.8), (5, 0.8)],
], 0.5))  # [[3, 3]]

# Disjoint periods, an empty camera stream, and no cameras.
print(common_motion_periods([
    [(1, 0.9), (2, 0.9)],
    [(3, 0.9), (4, 0.9)],
], 0.5))  # []
print(common_motion_periods([[(1, 0.9)], []], 0.5))  # []
print(common_motion_periods([], 0.5))  # []
