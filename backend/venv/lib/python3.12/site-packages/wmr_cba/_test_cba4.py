from wmr_cba import wmr_cba
import time

def __test_cba4():
    def show_status():
        disp = "Volts=" + str(cba.get_voltage()) + "V"
        disp += " Load=" + str(cba.get_set_current()) + "A"
        disp += " Feedback=" + str(cba.get_measured_current()) + "A"
        disp += " Running=" + str(cba.is_running())
        disp += " PLim=" + str(cba.is_power_limited())
        print(disp)
        #end show_status()

    test = wmr_cba.CBA4.test()
    if test:
        print("Test ERROR: " + test)
    else:
        print("Test OK")

    devices = wmr_cba.CBA4.scan()
    print("Found "+str(len(devices))+" devices.")

    cba = wmr_cba.CBA4()

    if not cba.is_valid():
        print("ERROR!  Couldn't open a device!")
        exit(-1)
    
    print("Opened CBA4, serial #" + str(cba.get_serial_number()))

    show_status()

    load = 0.2
    print("Starting load = " + str(load))
    cba.do_start(load)

    reads = 10
    while reads:
        time.sleep(1)
        show_status()
        reads -= 1
    
    cba.do_stop()
    print("Stopped test")

    reads = 5
    while reads:
        time.sleep(1)
        show_status()
        reads -= 1

    load = 0.1
    print("Starting load = " + str(load))
    cba.do_start(load)

    reads = 10
    while reads:
        time.sleep(1)
        show_status()
        reads -= 1
    
    cba.do_stop()
    print("Stopped test")

    reads = 5
    while reads:
        time.sleep(1)
        show_status()
        reads -= 1

    cba.close()

    print("Done")
    #end __test_cba4

if __name__ == "__main__":
    print("running _test_cba4.py")
    __test_cba4()