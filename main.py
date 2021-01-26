import math

def main():
    cls()
    choice = input("""
        Welcome to the Explosive Ordnance Disposal Calculator
        What would you like to do?

        1. Safe Distance from Blast
        2. Nuke Stay Time
        3. Determine Radiation Levels (inverse square)
        4. *Chart* PSI by K-Factor and Effects on the Body
        5. Quit

        >>> """)

    if choice == '1':
        safe_distance()
    elif choice == '2':
        stay_time()
    elif choice == '3':
        radiation_levels()
    elif choice == '4':
        psi()
    else:
        print("Please select a number between 1-4.")
        main()


def cls():
    return print("\n" * 100)


def safe_distance():
    '''Info: This function determines desired distance from blast'''

    new = input("\nEnter the Net Explosive Weight (NEW) >> ")
    k_fact = input("K-Factor >> ")
    cube_root = float(new) ** (1. / 3.)
    safe_distance = float(cube_root) * int(k_fact)

    print(f"Stay {math.ceil(safe_distance)}' from the point of initiation.")
    run_another(1)


def run_another(func):

    sd_choice = input("Would you like to run another calculation?? \n1: Yes\n2: No\n>> ")

    if sd_choice == '1':
        if func == 1:
            safe_distance()
        elif func == 2:
            stay_time()
        elif func == 3:
            radiation_levels()

    elif sd_choice == '2':
        main()
    else:
        print("Please enter a 1 or a 2")
        run_another()


def stay_time():
    '''Info: This function determines the nuke safe stay times'''

    mr_hr = input("\nWhat is your radiation reading in mR/hr? >> ")
    max_dose = input("What is your max dose in REM? >> ")
    rem_hr = float(mr_hr) * .001
    safe_time = float(max_dose) / float(rem_hr)

    print(
        f"You have {math.floor(safe_time)} hours and {(safe_time - math.floor(safe_time)) * 60} minutes before reaching your max dose.\n")
    run_another(2)


def radiation_levels():
    '''This function determines radiation levels or finding distances utilizing the inverse square law'''

    which_equat = input("What are you looking to solve for?\n\n1. I1\n2. I2\n3. D1\n4. D2\n\n>>> ")
    if which_equat == '1':
        i2 = input("What is the intensity in mREM at the furthest distance?\n\n>>> ")
        d1 = input("What is the distance in feet of the closer reading?\n\n>>> ")
        d2 = input("What is the distance in feet of the furthest reading?\n\n>>> ")

        i1 = (float(i2) * (float(d2) ** 2)) / float(d1) ** 2
        print(f"I1 equals {i1} mREM or {i1 * .001} REM.")
        run_another(3)

    elif which_equat == '2':
        i1 = input("What is the intensity in mREM at the closest distance?\n\n>>> ")
        d1 = input("What is the distance in feet of the closer reading?\n\n>>> ")
        d2 = input("What is the distance in feet of the furthest reading?\n\n>>> ")

        i2 = (float(i1) * (float(d1) ** 2)) / float(d2) ** 2
        print(f"I2 equals {i2} mREM or {i2 * .001} REM.")
        run_another(3)
    elif which_equat == '3':
        i1 = input("What is the intensity in mREM at the closer distance?\n\n>>> ")
        i2 = input("What is the intensity in mREM at the furthest distance?\n\n>>> ")
        d2 = input("What is the distance in feet of the furthest reading?\n\n>>> ")

        d1 = (float(i2) * (float(d2) ** 2)) / float(i1)
        print(f"D1 equals {math.floor(d1)}' and {d1 - math.floor(d1) / 12}\".")
        run_another(3)
    elif which_equat == '4':
        i1 = input("What is the intensity in mREM at the closer distance?\n\n>>> ")
        i2 = input("What is the intensity in mREM at the furthest distance?\n\n>>> ")
        d1 = input("What is the distance in feet of the closest reading?\n\n>>> ")

        d2 = (float(i1) * (float(d1) ** 2)) / float(i2)
        print(f"D2 equals {math.floor(d2)}' and {d2 - math.floor(d2) * 12}\".")
        run_another(3)
    else:
        print("Please select a number between 1-4")
        radiation_levels(3)
    run_another(3)

def psi():
    print("""
    *****************
    |K-Factor -> PSI|
    *****************
        
    K-2   =  313.91
    K-5   =  41.95
    K-10  = 9.56
    K-20  = 3
    K-50  = .89
    K-328 = .066
        
    **************************
    |Damage to the human body|
    **************************
        
    < 0.2 PSI   = Below threshold for temporary ear damage
    0.2 PSI     = Temporary ear damage
    5.0 PSI     = Eardrum rupture threshold
    15.0 PSI    = 50% Eardrum rupture
    30-40 PSI   = Lung damage threshold
    80.0 PSI    = 50% Lung damange
    130-180 PSI = 50% Lethality
    200-250 PSI = ~100% lethality
    """)

    input('\nHit Enter To Continue')
    main()


main()
