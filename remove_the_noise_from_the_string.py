def remove_noise(st):
    noise = "%$&/#·@|º\\ª" 
    return (''.join(c) for c in st if c not in noise) 