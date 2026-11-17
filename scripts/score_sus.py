#!/usr/bin/env python3
"""Score SUS survey exports.

Usage:  python3 scripts/score_sus.py SUS_all_responses.csv [more.csv ...]

Reads the CSV downloaded from the survey (columns participant_id, Q1..Q10),
re-scores every row from the raw ratings (it does not trust any score column
in the file), and prints each participant's score plus the group summary.
"""
import csv, math, statistics, sys

GRADES = [(84.1, "A+"), (80.8, "A"), (78.9, "A-"), (77.2, "B+"), (74.1, "B"), (72.6, "B-"),
          (71.1, "C+"), (65.0, "C"), (62.7, "C-"), (51.7, "D"), (0.0, "F")]
ADJ = [(84.1, "Excellent"), (72.6, "Good"), (51.7, "OK"), (25.0, "Poor"), (0.0, "Worst imaginable")]
T95 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262}


def sus(ratings):
    if len(ratings) != 10 or any(r not in (1, 2, 3, 4, 5) for r in ratings):
        raise ValueError(f"need ten ratings from 1 to 5, got {ratings}")
    # index 0 is item 1 (odd, positive): r - 1; index 1 is item 2 (even, negative): 5 - r
    return sum((r - 1) if i % 2 == 0 else (5 - r) for i, r in enumerate(ratings)) * 2.5


def percentile(score, mean=68.0, sd=12.5):
    p = round(50 * (1 + math.erf((score - mean) / (sd * math.sqrt(2)))))
    return max(1, min(99, p))


def band(score, table):
    return next(label for cut, label in table if score >= cut)


def main(paths):
    rows = []
    for path in paths:
        with open(path, newline="", encoding="utf-8") as f:
            for rec in csv.DictReader(f):
                ratings = [int(rec[f"Q{i}"]) for i in range(1, 11)]
                flags = []
                if len(set(ratings)) == 1:
                    flags.append("same answer on all 10")
                if min(ratings[0], ratings[1], ratings[2], ratings[3]) >= 4:
                    flags.append("agreed with opposite items")
                rows.append((rec["participant_id"], sus(ratings), flags))

    print(f"{'ID':<10}{'SUS':>6}{'Pctl':>6}  Grade  Adjective         Flags")
    for pid, s, flags in rows:
        print(f"{pid:<10}{s:>6.1f}{percentile(s):>6}  {band(s, GRADES):<5}  {band(s, ADJ):<16}  {'; '.join(flags)}")

    scores = [s for _, s, _ in rows]
    if len(scores) >= 2:
        m, sd = statistics.mean(scores), statistics.stdev(scores)
        half = T95.get(len(scores) - 1, 1.96) * sd / math.sqrt(len(scores))
        print(f"\nn = {len(scores)}  mean = {m:.1f}  SD = {sd:.1f}  95% CI = {max(0, m - half):.1f} to {min(100, m + half):.1f}")
        print(f"Mean percentile = {percentile(m)}  grade = {band(m, GRADES)}  adjective = {band(m, ADJ)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
