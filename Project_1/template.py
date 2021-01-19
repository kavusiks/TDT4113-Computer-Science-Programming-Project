""" Template for Project 1: Morse code """

from GPIOSimulator_v1 import *
import time
GPIO = GPIOSimulator()

MORSE_CODE = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g',
              '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n',
              '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u',
              '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '.----': '1',
              '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
              '---..': '8', '----.': '9', '-----': '0'}


class MorseDecoder():
    """ Morse code class """

    def __init__(self):
        """ initialize your class """
        self.current_symbol = ""
        self.current_word = ""
        self.current_char = ""
        self.T = 0.7

    def reset(self):
        """ reset the variable for a new run """
        self.handle_reset()
        self.current_word = ""

    def read_one_signal(self):
        """ read a signal from Raspberry Pi """
        GPIO.setup(PIN_BTN, GPIO.IN, GPIO.LOW)
        return GPIO.input(PIN_BTN)

    def decoding_loop(self):
        """ the main decoding loop """
        while True:
            current_state = self.read_one_signal()
            handle_on_state = self.find_handle_on_signal(current_state)
            if self.confirm_action(handle_on_state):
                self.stop_watch(handle_on_state)

    def confirm_action(self, signal):
        """ used to confirm that a signal to avoid the random 'space'-pressed signal"""
        previous_state1 = self.read_one_signal()
        previous_state2 = self.read_one_signal()
        previous_state3 = self.read_one_signal()
        if previous_state1 == previous_state2 == previous_state3 == signal:
            return True

    def find_handle_on_signal(self, signal):
        """ returns the opposite signal of the given signal """
        if signal == 0:
            return 1
        if signal == 1:
            return 0

    def stop_watch(self, signal):
        """ counting how long the given signal is pressed in """
        timer_start = time.time()
        counting = True
        while counting:
            """ sets the corresponding LED on/off light"""
            if signal == 1:
                if (time.time()-timer_start) < (self.T/2):
                    self.toggle_led("BLUE")
                else:
                    self.toggle_led("RED")
            """ If its a time gap between two word"""
            if signal == 0:
                if (time.time() - timer_start) > (10*self.T):
                    counting = False
            if self.confirm_action(self.find_handle_on_signal(signal)):
                counting = False
        elapsed = time.time() - timer_start
        """ sets the corresponding LED to blink"""
        """
        if signal == 1:
            if (time.time()-timer_start) < (1.5 * self.T):
                self.set_led("BLUE", GPIO.HIGH)
                self.set_led("RED", GPIO.LOW)
            else:
                self.set_led("BLUE", GPIO.LOW)
                self.set_led("RED", GPIO.HIGH)
        """
        return self.process_signal(signal, elapsed)

    def set_led(self, color, state):
        " used to set the output state of the given LEDs"
        if color == "BLUE":
            GPIO.output(PIN_BLUE_LED, state)
        if color == "RED":
            GPIO.output(PIN_RED_LED_0, state)
            GPIO.output(PIN_RED_LED_1, state)
            GPIO.output(PIN_RED_LED_2, state)

    def toggle_led(self, color):
        "used to blink the gived LED"
        if color == "BLUE":
            GPIO.output(PIN_BLUE_LED, GPIO.HIGH)
            time.sleep(self.T/2)
            GPIO.output(PIN_BLUE_LED, GPIO.LOW)
            time.sleep(self.T/2)
        if color == "RED":
            GPIO.output(PIN_RED_LED_0, GPIO.HIGH)
            GPIO.output(PIN_RED_LED_1, GPIO.HIGH)
            GPIO.output(PIN_RED_LED_2, GPIO.HIGH)
            time.sleep(self.T/2)
            GPIO.output(PIN_RED_LED_0, GPIO.LOW)
            GPIO.output(PIN_RED_LED_1, GPIO.LOW)
            GPIO.output(PIN_RED_LED_2, GPIO.LOW)
            time.sleep(self.T/2)


    def process_signal(self, signal, elapsed):
        """ handle the signals using corresponding functions """
        """ uses signal and elapsed time determine '.' or '_' or 'pause'"""
        if signal == GPIO.PUD_DOWN:
            """ since 1*T i already used in the printin of LED state"""
            if elapsed <= (1.5 * self.T):
                return self.update_current_symbol('.')
            if elapsed > (1.5 * self.T):
                return self.update_current_symbol('-')
        elif signal == GPIO.PUD_UP:
            if elapsed <= (1.5 * self.T):
                return
            if (elapsed > (1.5*self.T)) and (elapsed <= (4.5 * self.T)):
                print("Word registered")
                return self.handle_symbol_end()
            if elapsed > (4.5 * self.T):
                return self.handle_word_end()

    def update_current_symbol(self, signal):
        """ append the signal to current symbol code """
        if signal == ".":
            self.current_symbol += signal
        if signal == "-":
            self.current_symbol += signal
        print("Entered signal: ", signal)

    def handle_symbol_end(self):
        """ process when a symbol ending appears """
        if self.current_symbol != "":
            if self.current_symbol in MORSE_CODE:
                current_char = MORSE_CODE.get(self.current_symbol)
                print("Character registerd: ", current_char)
                self.current_word += current_char
                self.handle_reset()
            else:
                self.handle_reset()
                print("Invalid symbol, enter the symbol again!")
        self.show_message()

    def handle_word_end(self):
        """ process when a word ending appears """
        self.handle_symbol_end()
        self.current_word += " "
        self.show_message()
        self.handle_reset()

    def handle_reset(self):
        """ process when a reset signal received """
        self.current_symbol = ""

    def show_message(self):
        """ print the decoded message """
        if not self.current_word.isspace():
            print("Current message:", self.current_word)


def main():
    """ the main function """
    modecode = MorseDecoder()
    print("Decoding starts in 3 sec")
    for i in range(4):
        print(3-i)
        time.sleep(1)
    modecode.decoding_loop()


if __name__ == "__main__":
    main()
