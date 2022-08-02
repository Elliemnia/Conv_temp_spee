# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 16:51:52 2022
last edit Sun Jul 7/3/2022

This program convert the temperature to celcius and,
convert the speed in miles to meter

@author: Ellie Nia
"""

def farenheid_to_celsius(temp):     #Function to convert the temperature
    result = int((temp - 32) * 5/9)
    print("The temperature in Celsius is: ",result)
    
def miles_to_meter(speed):          #Function to convert the speed
    result = int(speed * 0.44704)
    print("The speed in meters per second is: ",result)
    


def main():             #main function to ask user to input the number of which function wants to use
    
    f = int(input("Enter 1 to convert Fahrenheit temoerature to Celsius or\nEnter 2 to convert speed from miles per hour to meters per second: "))
    
    if f == 1:
      temp = int(input('Enter a temperature in Farenhite: '))
      farenheid_to_celsius(temp)        #if the user enter 1, the function of the temperature is call
      
    elif f == 2:
      speed = int(input('Enter a speed in mile per hour: '))  
      miles_to_meter(speed)         #if the user enter 2, the function of speed is call
    
    else:
       print("you should enter 1 or 2, please try again")
    
main()
    