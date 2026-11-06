def loose_change(cents):
    if cents<0:
        return {"Nickels": 0, "Pennies": 0, "Dimes": 0, "Quarters": 0}
    cents = int(cents)
    monedas_valor = {"Quarters": 25, "Dimes": 10, "Nickels": 5, "Pennies": 1}
    monedas_cantidad = {"Nickels": 0, "Pennies": 0, "Dimes": 0, "Quarters": 0}
    for key, value in monedas_valor.items():
        if cents >= value:
            monedas_cantidad[key] = (cents // value)
            cents = cents % value
        else:
            continue
    return monedas_cantidad
if __name__ == '__main__':
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
print("Casos test superados")
