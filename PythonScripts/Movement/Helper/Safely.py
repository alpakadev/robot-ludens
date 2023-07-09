def safely_run(func, error_message):
    try:
        func()
    except Exception as e:
        print(f"{error_message}: {e}")