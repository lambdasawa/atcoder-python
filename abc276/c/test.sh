#!/bin/bash

set -xeuo pipefail

printf "4\n1 2 4 3" | python main.py
printf "4\n1 3 2 4" | python main.py
printf "4\n1 3 4 2" | python main.py
printf "4\n1 4 2 3" | python main.py
printf "4\n1 4 3 2" | python main.py
printf "4\n2 1 3 4" | python main.py
printf "4\n2 1 4 3" | python main.py
