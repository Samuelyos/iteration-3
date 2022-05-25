def validate_couseID(courseID):
    """validerer course ID er tal og ikke mere end 3 decimaler"""
    if not int:  # tjekker om det er tal
        return False  # retunerer false hvis det ikke er tal
    if len(str(courseID)) > 4:  # tjekker at længden ikke er over 3
        return False
    return True  # retunere true hvis den er guddi


def validate_course(course: str):
    """validerer længden på course"""
    if len(course) < 2:  # længen af navnet på kurset er over 3 tegn
        return False
    if len(course) > 35:  # længden af kurset må ikke være over 35 tegn
        return False
    return True


def validate_room(room: str):
    """validerer om det første er et bokstav og længden er passende"""
    if room[0].isdigit():  # hvis det er et tal, da det skal være et bokstav
        return False
    if len(room) > 35:  # længen må ikke være over 35
        return False
    return True


def validate_date(date):
    """validerer dato"""
    strdate = str(date)
    if not strdate[0].isdigit():  # det første skal være et tal
        return False
    return True


def validate_timefrom(timefrom):
    """validerer start tidspunkt"""
    if not str(timefrom)[2] == ":":  # tjekker at ":" er på plads 3)
        return False
    return True


def validate_timeuntil(timeuntil):
    """validerer slut tidspunkt"""
    if len(timeuntil) > 6:  # tjekker at længden ikke er over 4
        return False
    if not str(timeuntil)[2] == ":":  # tjekker at ":" er på plads 3)
        return False
    return True


def validate_zoom(zoom):
    """validerer zoom"""
    return True
