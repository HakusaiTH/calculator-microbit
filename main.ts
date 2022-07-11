input.onButtonPressed(Button.A, function () {
    if (n == 0) {
        num_1 = num_1 - 1
        basic.showNumber(num_1)
    } else if (n == 1) {
        op = op - 1
        op_p()
    } else if (n == 2) {
        num_2 = num_2 - 1
        basic.showNumber(num_2)
    } else {
        basic.showString("error")
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
    n = n + 1
    if (n == 3) {
        if (op == 1) {
            basic.showString("" + num_1 + "+" + num_2 + "=" + (num_1 + num_2))
        } else if (op == 2) {
            basic.showString("" + num_1 + "-" + num_2 + "=" + (num_1 - num_2))
        } else if (op == 3) {
            basic.showString("" + num_1 + "*" + num_2 + "=" + num_1 * num_2)
        } else if (op == 4) {
            basic.showString("" + num_1 + "/" + num_2 + "=" + num_1 / num_2)
        } else {
            basic.showString("error")
        }
    }
})
input.onButtonPressed(Button.B, function () {
    if (n == 0) {
        num_1 = num_1 + 1
        basic.showNumber(num_1)
    } else if (n == 1) {
        op = op + 1
        op_p()
    } else if (n == 2) {
        num_2 = num_2 + 1
        basic.showNumber(num_2)
    } else {
        basic.showString("error")
    }
})
function op_p () {
    if (op == 1) {
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            `)
    } else if (op == 2) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            . . . . .
            . . . . .
            `)
    } else if (op == 3) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    } else if (op == 4) {
        basic.showLeds(`
            . . # . .
            . . . . .
            # # # # #
            . . . . .
            . . # . .
            `)
    } else {
        basic.showString("error")
    }
}
let n = 0
let op = 0
let num_2 = 0
let num_1 = 0
num_1 = 0
num_2 = 0
op = 0
n = 0
basic.showNumber(num_1)
