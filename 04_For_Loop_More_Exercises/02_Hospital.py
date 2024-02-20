period = int(input())

all_patient = 0
treated_patient = 0
untreated_patient = 0
days_counter = 1
doctors_count = 7

for days in range(1, period + 1):
    patients = int(input())
    if days_counter == 3 and untreated_patient > treated_patient:
        days_counter = 1
        doctors_count += 1
        if patients <= doctors_count:
            treated_patient += patients
        else:
            untreated_patient += (patients - doctors_count)
            treated_patient += doctors_count
    else:
        if patients <= doctors_count:
            treated_patient += patients
        else:
            untreated_patient += (patients - doctors_count)
            treated_patient += doctors_count

        days_counter += 1

print(f"Treated patients: {treated_patient}.")
print(f"Untreated patients: {untreated_patient}.")