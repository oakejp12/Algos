'''
Given a series of video clips from an event that lasted T seconds
Return the minimum number of clips necessary to cover the
entire event. If impossible, return -1.
'''

import sys


def minimum_num_clips(clips: list, T: int) -> int:

    if (len(clips) == 0 and T > 0):
        return -1

    min_count = 0

    current_end = -1  # We want to start looking at intervals [0, :]
    next_end = 0

    # Idea: Sort clips from start intervals and look
    # at each clip in comparison to the current time interval
    for i, j in sorted(clips):
        if next_end >= T or i > next_end:
            break
        elif current_end < i <= next_end:
            # Consider another clip since our current stopping
            # point has passed
            min_count = min_count + 1
            current_end = next_end

        # Update our next stopping point as the
        # max between the current clip we're looking
        # at (j) or our current clip
        next_end = max(next_end, j)

    return min_count if next_end >= T else -1


def minimum_num_clips_dp(clips: list, T: int) -> int:

    # Like Knapsack with repetition, initialize
    # an array to keep track of time 0..T + 1 (or capacity...)
    # where D[i] is the number of distinct clips at time i
    D = []

    # Select clips based on a prefix of time
    # i.e. clips start between t = 0..i
    for i in range(0, T + 1):

        # Append current time interval
        # for clip comparison
        D.append(i)

        # Look at a prefix of clips that fit
        # the current time interval
        # if the smallest clip from before
        # can fit in the time interval, keep it
        # else, increment the number of clips needed
        # for the time interval t == i
        for clip in clips:
            if (i >= clip[0] and i <= clip[1]):
                D[i] = min(D[i], D[clip[0]] + 1)

        if (D[i] == T):
            break

    # Last element in D is the number of
    # distinct clips for the whole time interval
    return D[-1] if D[-1] != T else -1
