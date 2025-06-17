import threading, pyfirmata2, time

PORT = pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino(PORT)

servo_1 = board.get_pin('d:9:s')
servo_2 = board.get_pin('d:8:s')
servo_3 = board.get_pin('d:7:s')
servo_4 = board.get_pin('d:6:s')
servo_5 = board.get_pin('d:5:s')


stop_event = threading.Event()

def open_close_loop1():
    deg = 180
    while not stop_event.is_set():
        servo_1.write(deg)
        deg = 0 if deg == 180 else 180
        time.sleep(1)  # Pause to prevent hammering the servo

def open_close_loop2():
    deg = 180
    while not stop_event.is_set():
        servo_2.write(deg)
        deg = 0 if deg == 180 else 180
        time.sleep(1)  # Pause to prevent hammering the servo

def open_close_loop3():
    deg = 180
    while not stop_event.is_set():
        servo_3.write(deg)
        deg = 0 if deg == 180 else 180
        time.sleep(1)  # Pause to prevent hammering the servo

def open_close_loop4():
    deg = 180
    while not stop_event.is_set():
        servo_4.write(deg)
        deg = 0 if deg == 180 else 180
        time.sleep(1)  # Pause to prevent hammering the servo

def open_close_loop5():
    deg = 180
    while not stop_event.is_set():
        servo_5.write(deg)
        deg = 0 if deg == 180 else 180
        time.sleep(1)  # Pause to prevent hammering the servo


# Start the loop
t1 = threading.Thread(target=open_close_loop1).start()
t2 = threading.Thread(target=open_close_loop2).start()
t3 = threading.Thread(target=open_close_loop3).start()
t4 = threading.Thread(target=open_close_loop4).start()
t5 = threading.Thread(target=open_close_loop5).start()

input("Press Enter to stop...\n")
stop_event.set()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()


