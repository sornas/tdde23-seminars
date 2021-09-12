def latest_birthday_before(month, day):
    search_date = (month, day)
    birthdays = [
        ((8, 20), "Alice"),
        ((8, 15), "Bob"),
        ((7, 18), "Carol"),
    ]
    for date, name in birthdays:
        if date < search_date:
            return name
    return birthdays[0][1]


print(latest_birthday_before(8, 18))
print(latest_birthday_before(8, 15))
print(latest_birthday_before(8, 14))
print(latest_birthday_before(7, 10))
