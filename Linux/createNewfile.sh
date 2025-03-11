#!/bin/bash
# Сделайте скрипт, который будет спрашивать название и создавать файл, затем спрашивать права для этого файла и задавать их.
read -p "Print name: " name
touch $name
read -p "What rights are needed? " rights
chmod $rights $name