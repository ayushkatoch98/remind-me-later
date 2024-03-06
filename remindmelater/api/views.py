from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Reminders
import datetime

def isValidDateString(dateStr):
    try:
        datetime.datetime.strptime(dateStr, "%Y-%m-%d")
        return True
    except Exception as err:
        print("got exception", err)
        return False


def isValidTimeString(dateStr):
    try:
        datetime.datetime.strptime(dateStr, "%H:%M:%S")
        return True
    except:
        return False


def isInFuture(dateStr, timeStr):

    reminderDate = datetime.datetime.strptime(dateStr + " " + timeStr , "%Y-%m-%d %H:%M:%S")
    rightNow = datetime.datetime.now()

    if reminderDate <= rightNow:
        return False
    
    return True

    


class ReminderEndpoint(View):

    def get(self, request):
        
        reminders = Reminders.objects.all()

        data = {
            "data": list(reminders.values())
        }
    
        return JsonResponse(data, status=200)

    def post(self, request):
        
        remindDate = request.POST.get("remind_date" , "")
        remindTime = request.POST.get("remind_time" , "")
        message = request.POST.get("message" , "")

        if message is None or len(message) == 0:
            return JsonResponse({"error": True, "err_message": "Message cannot be empty"}, status=400)

        if not isValidDateString(remindDate):
            return JsonResponse({"error" : True, "err_message" : "Invalid Date, correct format is YYYY-MM-DD"}, status=400)
        
        if not isValidTimeString(remindTime):
            return JsonResponse({"error" : True, "err_message" : "Invalid Time, correct format is HH:MM:SS"}, status=400)

        if not isInFuture(remindDate, remindTime):
            return JsonResponse({"error" : True, "err_message" : "Reminder date & time must be in future. If the differance between the provided datetime and the current time is small, this function might return an error due to different timezones (python uses UTC). UTC Time would be -5:30"}, status=400)
            

        reminder = Reminders(message = message, remind_date = remindDate, remind_time = remindTime)
        reminder.save()

        data = {
            "id" : reminder.id,
            "message" : reminder.message,
            "remind_date": reminder.remind_date,
            "remind_time": reminder.remind_time
        }
        
        return JsonResponse(data, status = 200)