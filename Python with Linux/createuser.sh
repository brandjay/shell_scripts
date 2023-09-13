#!/bin/bash

read -p "Enter a username " name

read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

sudo useradd $name

