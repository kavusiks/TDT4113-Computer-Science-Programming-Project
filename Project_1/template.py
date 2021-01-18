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
        #GPIO.setup(PIN_BTN, GPIO.IN, GPIO.LOW)
        self.T = 0.3

    def reset(self):
        """ reset the variable for a new run """
        self.current_symbol = ""
        self.current_word = ""

    def read_one_signal(self):
        """ read a signal from Raspberry Pi """
        GPIO.setup(PIN_BTN, GPIO.IN, GPIO.LOW)
        return GPIO.input(PIN_BTN)

    def decoding_loop(self):
        """ the main decoding loop """
        while True:
            current_state = self.read_one_signal()
            #print("curr", current_state)
            previous_state = self.read_one_signal()
            if self.confirm_action(self.find_handle_on_signal(current_state)):
                #print("state: ", previous_state1)
                processing_state = previous_state
                #::::
                #Hvorfor må denne ha processing, og ikke current?
                self.stop_watch(processing_state)

    def confirm_action(self, signal):
        previous_state1 = self.read_one_signal()
        previous_state2 = self.read_one_signal()
        previous_state3 = self.read_one_signal()
        if previous_state1 == previous_state2 == previous_state3 == signal:
            return True

    def find_handle_on_signal(self, signal):
        if signal == 0:
            return 1
        if signal == 1:
            return 0

    def stop_watch(self, signal):
        timer_start = time.time()
        counting = True
        while counting:
           # if (time.time()-timer_start) < (1.5 * self.T):
            #    self.toggle_led("BLUE")
            #else:
             #   self.toggle_led("RED")
            if self.confirm_action(self.find_handle_on_signal(signal)):
                counting = False
        elapsed = time.time() - timer_start
        if signal == 1:
            #print("Holdt inn space i: ",elapsed)
            if (time.time()-timer_start) < (1.5 * self.T):
                self.set_led("BLUE", GPIO.HIGH)
                self.set_led("RED", GPIO.LOW)
            else:
                self.set_led("RED", GPIO.HIGH)
                self.set_led("BLUE", GPIO.LOW)

        #if signal == 0:
            #print("Sluppet space i: ", elapsed)
        return self.process_signal(signal, elapsed)

    def set_led(self, color, state):
        loop_blue = False
        loop_red = False
        if color == "BLUE":
            loop_blue = True
            GPIO.output(PIN_BLUE_LED, state)
        if color == "RED":
            loop_red = True
            GPIO.output(PIN_RED_LED_0, state)
            GPIO.output(PIN_RED_LED_1, state)
            GPIO.output(PIN_RED_LED_2, state)

    def toggle_led(self, color):
        loop_blue = False
        loop_red = False
        if color == "BLUE":
            #loop_blue = True
            GPIO.output(PIN_BLUE_LED, GPIO.HIGH)
            GPIO.output(PIN_BLUE_LED, GPIO.LOW)
        if color == "RED":
            #loop_red = True
            GPIO.output(PIN_RED_LED_0, GPIO.HIGH)
            GPIO.output(PIN_RED_LED_1, GPIO.HIGH)
            GPIO.output(PIN_RED_LED_2, GPIO.HIGH)
            GPIO.output(PIN_RED_LED_0, GPIO.LOW)
            GPIO.output(PIN_RED_LED_1, GPIO.LOW)
            GPIO.output(PIN_RED_LED_2, GPIO.LOW)


    def process_signal(self, signal, elapsed):
        """ handle the signals using corresponding functions """
        if signal == GPIO.PUD_DOWN:
            if elapsed <= (1.5 * self.T):
                return self.update_current_symbol('.')
            #if elapsed <= (4.5 * T):
            if elapsed > (1.5 * self.T): #for enklere timing av trykkinga
                return self.update_current_symbol('-')
        elif signal == GPIO.PUD_UP:
            if elapsed <= (1.5 * self.T):
                return
            if elapsed <= (4.5 * self.T):
                return self.handle_symbol_end()
            #if elapsed <= (4.5*T):
            if elapsed > (4.5 * self.T): #for enklere timing av trykkingen
                return self.handle_word_end()
        #print("Current word in process_signal: ", self.current_word)

    def update_current_symbol(self, signal):
        """ append the signal to current symbol code """
        if signal == ".":
            self.current_symbol += signal
        if signal == "-":
            self.current_symbol += signal
        #print("current signal: ", signal)

    def handle_symbol_end(self):
        """ process when a symbol ending appears """
        if self.current_symbol != "":
            #print("sjekker dette signalet", self.current_symbol)
            if self.current_symbol in MORSE_CODE:
                current_char = MORSE_CODE.get(self.current_symbol)
                self.current_word += current_char
                self.current_symbol = ""
                #print("current word: ", self.current_word)
            else:
                self.current_symbol = ""
                print("Ugyldig symbol, skriv symbolet på nytt!")
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
        print("Message: ", self.current_word)


def main():
    """ the main function """
    modecode = MorseDecoder()
    print("Dekodingen starter om 3 sek")
    for i in range (4):
        print(3-i)
        time.sleep(1)
    modecode.decoding_loop()


if __name__ == "__main__":
    main()
