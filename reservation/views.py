from django.shortcuts import render, redirect
from .forms import ReservationForm
# Create your views here.


def reserv(request):
    reserv_form = ReservationForm()
    if request.method == "POST":
        reserv_form = ReservationForm(request.POST)
        if reserv_form.is_valid():
            reserv_form.save()
            return redirect("reservation:succes")
    else:
        reserv_form = ReservationForm()
    context = {
        "form" : reserv_form
    }

    return render(request, "reservation/reservation.html", context)


def succes(request):
    return render(request, "reservation/succes.html", {})