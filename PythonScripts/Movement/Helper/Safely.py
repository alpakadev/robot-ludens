def safely_run(func, error_message):
    """
    Führt die angegebene Funktion sicher aus und gibt eine Fehlermeldung aus, falls eine Ausnahme auftritt.

    Args:
        func (function): Die auszuführende Funktion.
        error_message (str): Die Fehlermeldung, die ausgegeben werden soll.

    """
    try:
        func()
    except Exception as e:
        print(f"{error_message}: {e}")
