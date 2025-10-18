from fractions import Fraction
from pathlib import Path

import pandas as pd
from spamirai_dataset_common import DataLabel


def _calculate_fraction(x: int, y: int) -> Fraction | None:
    if x == 0 or y == 0:
        return None

    return Fraction(x / y).limit_denominator(2)


def print_stats(dataset_path: Path):
    print(dataset_path.name)

    if not dataset_path.exists():
        print("\tN/A")
        print()
        return

    df = pd.read_csv(dataset_path)

    count = len(df)
    spam_count = len(df[df["label"] == DataLabel.SPAM.value])
    not_spam_count = len(df[df["label"] == DataLabel.NOT_SPAM.value])
    spam_not_spam_fraction = _calculate_fraction(spam_count, not_spam_count)

    print(f"\tcount: {count}")
    print(f"\tspam count: {spam_count}")
    print(f"\tnot spam count: {not_spam_count}")
    print(f"\tspam/not spam fraction: {spam_not_spam_fraction}")
    print()
