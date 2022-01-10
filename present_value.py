#!/usr/bin/env python3

"""
Calculating Present Value
Author: Christoph Karl Heck (hech1031@h-ka.de) December 8, 2021
"""

"""
How to execute the script:
python present_value.py -p 5 -da 365 -i 1.0175 -d 1000 -nbr 137
"""

import argparse


def calculatePresentValue(
    number_of_periods,
    days_per_period,
    number_until_end_period,
    interest_of_each_period,
    denomination,
):
    days_each_period: list = list()
    further_days: int = number_until_end_period
    while number_of_periods >= 0:
        days_each_period.append(further_days)
        further_days += days_per_period
        number_of_periods -= 1

    present_value: float = 0.0
    for days in days_each_period:
        exponent: float = days / days_per_period
        interest: float = (interest_of_each_period * denomination) - denomination
        if days is days_each_period[-1]:
            present_value += (interest + denomination) / (
                (interest_of_each_period) ** exponent
            )
            print(
                str(round(interest, 3))
                + "+"
                + str(denomination)
                + "/"
                + str(interest_of_each_period)
                + "^("
                + str(days)
                + "/"
                + str(days_per_period)
                + ") ="
            )

        else:
            present_value += interest / ((interest_of_each_period) ** exponent)
            print(
                str(round(interest, 3))
                + "/"
                + str(interest_of_each_period)
                + "^("
                + str(days)
                + "/"
                + str(days_per_period)
                + ") + "
            )

    return round(present_value, 3)


def main(args):
    print(
        calculatePresentValue(
            args.periods, args.days, args.number, args.interest, args.denomination
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--periods", help="number of periods", type=int, required=True
    )
    parser.add_argument(
        "-da", "--days", help="days per period", type=int, required=True
    )
    parser.add_argument(
        "-i",
        "--interest",
        help="Interest that will paid by the debtor each period in percentage",
        type=float,
        required=True,
    )
    parser.add_argument(
        "-d",
        "--denomination",
        help="Denomaniation of the bond in euro",
        type=int,
        required=True,
    )
    parser.add_argument(
        "-nbr",
        "--number",
        help="Number of days until the end of the period",
        type=int,
        required=True,
    )
    args = parser.parse_args()
    main(args)
