def loose_change(cents):
    cents = int(cents)
    monedas = {
        "Nickels": 0,
        "Pennies": 0,
        "Dimes": 0,
        "Quarters": 0,
        }
    if cents >= 25:
        monedas["Quarters"] = int(cents / 25)
        cents = cents - (monedas["Quarters"] * 25)
    if cents >= 10:
        monedas["Dimes"] = int(cents / 10)
        cents = cents - (monedas["Dimes"] * 10)
    if cents >= 5:
        monedas["Nickels"] = int(cents / 5)
        cents = cents - (monedas["Nickels"] * 5)
    if cents >= 0:
        monedas["Pennies"] = cents
    return monedas  # Formato diccionario
if __name__ == '__main__':
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
print("Pasos test superados")
