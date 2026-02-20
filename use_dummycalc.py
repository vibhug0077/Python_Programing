"""Run this file from the project root to test package usage."""

from dummycalc import (
    add,
    cli_args,
    current_time,
    divide,
    factorial,
    power,
    python_info,
    quick_report,
)

print("add(10, 5) ->", add(10, 5))
print("divide(10, 2) ->", divide(10, 2))
print("power(2, 4) ->", power(2, 4))
print("factorial(5) ->", factorial(5))
print("quick_report(9, 7) ->", quick_report(9, 7))
print("python_info() ->", python_info())
print("cli_args() ->", cli_args())
print("current_time() ->", current_time())
