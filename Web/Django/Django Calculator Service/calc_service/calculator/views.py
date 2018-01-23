from django.shortcuts import render
from django.contrib import messages
from .forms import CalcForm, OperationForm
from django.contrib.auth.models import User
from .models import Operation

# Create your views here.


def calculation(x, y, operation):
    if operation == 'SUM':
        return x + y
    elif operation == 'SUB':
        return x - y
    elif operation == 'MUL':
        return x * y
    elif operation == 'DIV':
        return x / y
    elif operation == 'POW':
        return x ** y
    else:
        return 'wrong operation'


def calc_home(request):

    form = OperationForm(request.POST or None)
    if request.user.is_authenticated():
        if form.is_valid():
            data = form.cleaned_data

            operation = data["op"]
            x = float(data["x_value"])
            y = float(data["y_value"])

            result = calculation(x, y, operation)

            messages.success(request, "Result: " + str(result))

            user = request.user
            instance = form.save(commit=False)
            instance.user = user
            instance.result = result
            instance.save()

    context_data = {
        "form": form
    }

    return render(request, "calculator_view.html", context_data)


def user_detail(request):
    user = request.user

    user_operations = Operation.objects.filter(user=user)

    context_data = {
        "username": user.username,
        "object_list": user_operations
    }

    return render(request, 'user_view.html', context_data)