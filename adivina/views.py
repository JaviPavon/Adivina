from django.shortcuts import render

from .models import Adivina
def formulario(request):
    return render(request, 'adivina/formulario.html')

def resultado(request):
    random_number = Adivina.numero
    user_guess = int(request.POST['guess'])

    if user_guess == random_number:
        message = "Felicidades, lo has adivinado."
    elif user_guess > random_number:
        message = "¡Oh no, no lo has adivinado(Te has pasado)."   
    elif user_guess < random_number:
        message = "¡Oh no, no lo has adivinado(Te has quedado corto)."    

    return render(request, 'adivina/resultado.html', {'message': message})