def loose_change(cents):
    cents=int(cents)
    quarters=0
    dimes=0
    pennies=0
    nickels=0
    if cents>=25:
        quarters=int(cents/25)
        cents=cents-(quarters*25)
    if cents>=10:
        dimes=int(cents/10)
        cents=cents-(dimes*10)
    if cents>=5:
        nickels=int(cents/5)
        cents=cents-(nickels*5)
    if cents>=0:
        pennies=cents
    return {'Nickels': nickels,'Pennies': pennies,'Dimes': dimes,'Quarters': quarters} # Formato diccionario