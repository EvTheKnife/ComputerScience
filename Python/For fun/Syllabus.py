from calendar import Calendar
from datetime import *


print("\n--------------------")
print("Welcome to your syllabus generator!")
print("Please enter all dates in this format: mm.dd.yyyy")
print("--------------------\n")

startDateInput = input("Enter your start date: ")
endDateInput = input("Enter your end date: ")


startDateList = startDateInput.split('.')
endDateList = endDateInput.split('.')

startDate = date(int(startDateList[2]), int(startDateList[0]), int(startDateList[1]))
endDate = date(int(endDateList[2]), int(endDateList[0]), int(endDateList[1]))

def daysBetween(startDate, endDate, dayOfWeek):
    calendar = Calendar()
    weekList = []

    for year in range(startDate.year, endDate.year):
        for month in range():
            pass