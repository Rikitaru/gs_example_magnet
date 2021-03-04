#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gs_module import CargoController
from time import sleep

cargo = CargoController() # создаем объект магнитного захвата
cargo.on() # включаем магнит
cargo.changeColor(255, 0, 0, 0) # меняем цвет 0-го светодиода на красный, первыми тремя аргументами передаем цвет светодиода в RGB, четвертым аргументом номер светодиода от 0 до 3
sleep(2) # ожидаем 2 секунды
cargo.changeColor(0, 255, 0, 1) # меняем цвет 1-го светодиода на на зеленый
sleep(2)
cargo.changeColor(0, 0, 255, 2) # меняем цвет 2-го светодиода на на синий
sleep(2)
cargo.changeAllColor(255, 0, 0) # меняем цвет всех светодиодов на на красный
sleep(5)
cargo.changeAllColor(0, 0, 0) # выключаем все лампочки
cargo.off() # выключаем магнит
