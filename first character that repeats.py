def first_dup(s):
    return next((word for word in s if s.count(word)>1),None)