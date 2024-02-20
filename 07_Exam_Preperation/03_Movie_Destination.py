movie_budget = float(input())
destination = input()
season = input()
days = int(input())

cost_per_day = 0
if season == "Winter":
    if destination == "Dubai":
        cost_per_day = 45000 * 0.7  # Внимавай с процентите!
    elif destination == "Sofia":
        cost_per_day = 17000 * 1.25  # Внимавай с процентите!
    elif destination == "London":
        cost_per_day = 24000
elif season == "Summer":
    if destination == "Dubai":
        cost_per_day = 40000 * 0.7  # Внимавай с процентите!
    elif destination == "Sofia":
        cost_per_day = 12500 * 1.25  # Внимавай с процентите!
    elif destination == "London":
        cost_per_day = 20250

sum_cost = days * cost_per_day

# if destination == "Dubai":
#     sum_cost = sum_cost * 0.7  # Внимавай с процентите!
# elif destination == "Sofia":
#     sum_cost = sum_cost * 1.25  # Внимавай с процентите!

diff = abs(movie_budget - sum_cost)

if movie_budget >= sum_cost:
    print(f"The budget for the movie is enough! We have {diff :.2f} leva left!")
else:
    print(f"The director needs {diff :.2f} leva more!")