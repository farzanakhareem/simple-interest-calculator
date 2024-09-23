#!/bin/bash
# Simple Interest Calculator

echo "Enter principal amount:"
read principal
echo "Enter rate of interest (as a percentage):"
read rate
echo "Enter time (in years):"
read time

simple_interest=$(echo "scale=2; ($principal * $rate * $time) / 100" | bc)
echo "The simple interest is: $simple_interest"
