from django.shortcuts import render
from .models import Point, History, RefernceTable
from django.views import generic
from .forms import RequestForm
from .task import calculate_distance


def index(request):
    return render(request, 'points/index.html')

def new_form(request):
    form = RequestForm()

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print("y: " + str(form.cleaned_data['y']))
            print("x: " + str(form.cleaned_data['x']))
            print("n: " + str(form.cleaned_data['n']))
            print("operation_type: " + str(form.cleaned_data['operation_type']))
            entry = form.save(commit=True)
            print(entry)
            calculate_distance(entry)
            return render(request, 'points/history.html', {'history_points': History.objects.all()})
        else:
            print("ERROR INVALID FORM!")


    return render(request, 'points/new_form.html', {'form': form})

def submit_form(request):    
    return render(request, 'points/history.html')

class NewView(generic.DetailView):
    model = Point
    template_name = 'points/new.html'

class HistoryView(generic.ListView):
    model = Point
    template_name = 'points/history.html'
    context_object_name = 'history_points'

    def get_queryset(self):
        """Return the last five published questions."""
        print(History.objects.all())
        return History.objects.all()

    # return render(request, 'points/history.html')

