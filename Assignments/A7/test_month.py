def month_length(month, leap_year=False):
    """Return the number of days in the given month."""
    if month in {"September", "April", "June", "November"}:
        return 30
    elif month in {"January", "March", "May", "July",
                        "August", "October", "December"}:
        return 31
    if month == "February":
        if not leap_year:
            return 28
        else:
            return 29
    else:
        return None

def test_month():
    assert month_length("September") == 30
    assert month_length("January") == 31
    assert month_length("February", leap_year=True) == 29
    assert month_length("February", leap_year=False) == 28
    assert month_length("Octomber") == None