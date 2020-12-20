"""
This is answer of question five
"""
import toga
import numpy_financial as npf
from toga.style import Pack
from toga.style.pack import COLUMN, BOLD, RIGHT, CENTER

class Question:
    def __init__(self, name, symbol, forex, format='%.2f'):
        self.name = name
        self.symbol = symbol
        self.forex = forex
        self.format = format

    def __str__(self):
        if self.symbol:
            return '{} ({})'.format(self.name, self.symbol)
        else:
            return self.name


class QuestionFive(toga.App):

    def calculate(self):
        try:
            futureLumpSum = self.amount.value;
            print('interest', self.interest.value)
            print('compoundingFrequency', self.compoundingFrequency.value)
            print('future value', futureLumpSum)

            value = self.amount.value
            print('value',value)
            my_amount = npf.pv(self.interest.value/12, self.compoundingFrequency.value*12, -self.saving.value, self.amount.value)
            print('my amount', my_amount)
            self.my_amount.value = my_amount

        except (ValueError, TypeError) as e:
            if self.amount.value:
                value = '?'
            else:
                value = ''


            self.my_amount.value = value
            # self.my_amount.value = my_amount

    def on_select(self, widget):
        self.calculate()

    def on_change(self, widget):
        self.calculate()

    def startup(self):
        self.main_window = toga.MainWindow(
            title=self.formal_name,
            size=(320, 568)
        )

        box = toga.Box(style=Pack(direction=COLUMN, padding=5))

        interest_box = toga.Box(
            style=Pack(
                padding=(20, 0, 5, 0),
                alignment=CENTER
            )
        )
        interest_box.add(toga.Label(
            'Interest:',
            style=Pack(
                width=120,
                padding_right=5,
                font_family='Helvetica',
                font_size=16,
                font_weight=BOLD,
                text_align=RIGHT,
            )
        ))
        box.add(interest_box)

        self.interest = toga.NumberInput(
            on_change=self.on_change,
            min_value=0,
            step='0.01',
            style=Pack(
                font_family='Helvetica',
                font_size=48,
                text_align=RIGHT
            )
        )
        box.add(self.interest)

        compoundingFrequency_box = toga.Box(
            style=Pack(
                padding=(20, 0, 5, 0),
                alignment=CENTER
            )
        )
        compoundingFrequency_box.add(toga.Label(
            'Frequency:',
            style=Pack(
                width=120,
                padding_right=1,
                font_family='Helvetica',
                font_size=16,
                font_weight=BOLD,
                text_align=RIGHT,
            )
        ))
        box.add(compoundingFrequency_box)

        self.compoundingFrequency = toga.NumberInput(
            on_change=self.on_change,
            min_value=0,
            step='0.01',
            style=Pack(
                font_family='Helvetica',
                font_size=48,
                text_align=RIGHT
            )
        )
        box.add(self.compoundingFrequency)

        saving_box = toga.Box(
            style=Pack(
                padding=(20, 0, 5, 0),
                alignment=CENTER
            )
        )
        saving_box.add(toga.Label(
            'Saving monthly:',
            style=Pack(
                width=120,
                padding_right=1,
                font_family='Helvetica',
                font_size=16,
                font_weight=BOLD,
                text_align=RIGHT,
            )
        ))
        box.add(saving_box)

        self.saving = toga.NumberInput(
            on_change=self.on_change,
            min_value=0,
            step='0.01',
            style=Pack(
                font_family='Helvetica',
                font_size=48,
                text_align=RIGHT
            )
        )
        box.add(self.saving)



        local_box = toga.Box(
            style=Pack(
                padding=(20, 0, 5, 0),
                alignment=CENTER
            )
        )
        local_box.add(toga.Label(
            'Future Value:',
            style=Pack(
                width=120,
                padding_right=5,
                font_family='Helvetica',
                font_size=16,
                font_weight=BOLD,
                text_align=RIGHT,
            )
        ))

        box.add(local_box)

        self.amount = toga.NumberInput(
            on_change=self.on_change,
            min_value=0,
            step='0.01',
            style=Pack(
                font_family='Helvetica',
                font_size=48,
                text_align=RIGHT
            )
        )
        box.add(self.amount)

        my_box = toga.Box(
            style=Pack(
                padding=(10, 0, 5, 0),
                alignment=CENTER
            )
        )
        my_box.add(toga.Label(
            'Present Value:',
            style=Pack(
                width=120,
                padding_right=5,
                font_family='Helvetica',
                font_size=16,
                font_weight=BOLD,
                text_align=RIGHT
            )
        ))

        box.add(my_box)

        self.my_amount = toga.TextInput(
            readonly=True,
            style=Pack(
                font_family='Helvetica',
                font_size=48,
                text_align=RIGHT
            )
        )
        box.add(self.my_amount)

        self.calculate()

        self.main_window.content = box
        self.main_window.show()


def main():
    return QuestionFive()
