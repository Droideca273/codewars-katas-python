from decimal import Decimal, ROUND_HALF_UP

def round_by_2_decimal_places(n):
    d = Decimal(str(n))
    return d.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)