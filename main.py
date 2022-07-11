def on_button_pressed_a():
    global num_1, op, num_2
    if n == 0:
        num_1 = num_1 - 1
        basic.show_number(num_1)
    elif n == 1:
        op = op - 1
        if op == 1:
            basic.show_leds("""
                . . # . .
                                . . # . .
                                # # # # #
                                . . # . .
                                . . # . .
            """)
        elif op == 2:
            basic.show_leds("""
                . . . . .
                                . . . . .
                                # # # # #
                                . . . . .
                                . . . . .
            """)
        elif op == 3:
            basic.show_leds("""
                # . . . #
                                . # . # .
                                . . # . .
                                . # . # .
                                # . . . #
            """)
        elif op == 4:
            basic.show_leds("""
                . . # . .
                                . . . . .
                                # # # # #
                                . . . . .
                                . . # . .
            """)
        else:
            basic.show_string("error")
    elif n == 2:
        num_2 = num_2 - 1
        basic.show_number(num_2)
    else:
        basic.show_string("error")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global n
    basic.clear_screen()
    n = n + 1
    if n == 3:
        if op == 1:
            basic.show_number(num_1 + num_2)
        elif op == 2:
            basic.show_number(num_1 - num_2)
        elif op == 3:
            basic.show_number(num_1 * num_2)
        elif op == 4:
            basic.show_number(num_1 / num_2)
        else:
            basic.show_string("error")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global num_1, op, num_2
    if n == 0:
        num_1 = num_1 + 1
        basic.show_number(num_1)
    elif n == 1:
        op = op + 1
        if op == 1:
            basic.show_leds("""
                . . # . .
                                . . # . .
                                # # # # #
                                . . # . .
                                . . # . .
            """)
        elif op == 2:
            basic.show_leds("""
                . . . . .
                                . . . . .
                                # # # # #
                                . . . . .
                                . . . . .
            """)
        elif op == 3:
            basic.show_leds("""
                # . . . #
                                . # . # .
                                . . # . .
                                . # . # .
                                # . . . #
            """)
        elif op == 4:
            basic.show_leds("""
                . . # . .
                                . . . . .
                                # # # # #
                                . . . . .
                                . . # . .
            """)
        else:
            basic.show_string("error")
    elif n == 2:
        num_2 = num_2 + 1
        basic.show_number(num_2)
    else:
        basic.show_string("error")
input.on_button_pressed(Button.B, on_button_pressed_b)

n = 0
op = 0
num_2 = 0
num_1 = 0
num_1 = 0
num_2 = 0
op = 0
n = 0
basic.show_number(num_1)