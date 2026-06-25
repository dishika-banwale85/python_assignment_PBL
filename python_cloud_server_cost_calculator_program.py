# Project 2: Cloud Server Cost Calculator

HOURLY_RATE = 0.51
HOURS_PER_DAY = 24
DAYS_PER_WEEK = 7
DAYS_PER_MONTH = 30
BUDGET = 918


def calculate_costs():
    cost_per_day = HOURLY_RATE * HOURS_PER_DAY
    cost_per_week = cost_per_day * DAYS_PER_WEEK
    cost_per_month = cost_per_day * DAYS_PER_MONTH
    days_with_budget = BUDGET / cost_per_day

    return (
        cost_per_day,
        cost_per_week,
        cost_per_month,
        days_with_budget
    )


def main():
    day, week, month, budget_days = calculate_costs()

    print(f"Cost to operate one server per day:   ${day:.2f}")
    print(f"Cost to operate one server per week:  ${week:.2f}")
    print(f"Cost to operate one server per month: ${month:.2f}")
    print(f"Days one server can run with $918:    {budget_days:.2f} days")


if __name__ == "__main__":
    main()