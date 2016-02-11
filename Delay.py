def delay_print(s, delay=0.05):
    for c in str(s):
        sys.stdout.write('%s' % c )
        sys.stdout.flush()
        time.sleep(delay)

def delay_input(s):
    delay_print(s)
    return input()