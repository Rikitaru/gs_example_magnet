#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gs_module import CargoController
from time import sleep

cargo = CargoController() # создаем объект магнитного захвата
cargo.on() # включаем магнит
n=int(0)
#поочередное зажигание конкретного светодиода в завимости от кратности числа N числу четыре. Зажигается цветом в зависимости от кратности N к числу 3 
while  n < 10:
    n=n+1
    if ((n%3) == 0): 
        cargo.changeColor(255, 0, 0, n%4)
    if ((n%3) == 1):
        cargo.changeColor(0, 255, 0, n%4)
    if ((n%3) == 2):
        cargo.changeColor(0, 0, 255, n%4)
    sleep(0.5)# ожидаем 0.5 секунды

cargo.off() # выключаем магнит
sleep(2)# ожидаем 2 секунды
cargo.on() # включаем магнит
cargo.changeColor(255, 0, 0, 0) # меняем цвет 0-го светодиода на красный, первыми тремя аргументами передаем цвет светодиода в RGB, четвертым аргументом номер светодиода от 0 до 3
sleep(2) 
cargo.changeColor(0, 255, 0, 1) # меняем цвет всех светодиодов на зеленый
sleep(2) 
cargo.changeColor(0, 0, 255, 2) # меняем цвет всех светодиодов на зеленый
sleep(2)
cargo.changeAllColor(255, 0, 0) # выключаем все лампочки
sleep(5)
cargo.changeAllColor(0, 0, 0) # выключаем все лампочки
cargo.off() # выключаем магнит
