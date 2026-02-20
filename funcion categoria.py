def categorizar_clima(I):

    if 0 <= I < 5:
        return "desertica"
    elif 5 <= I < 10:
        return "semiarida"
    elif 10 <= I < 20:
        return "arida/arida subterranea"
    elif 20 <= I < 30:
        return "subhumeda"
    elif 30 <= I < 60:
        return "humeda"
    else:
        return "perhumeda"