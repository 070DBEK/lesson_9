from django.shortcuts import render, redirect, get_object_or_404
from .models import Sport


def sport_list(request):
    sports = Sport.objects.all()
    ctx = {'sports': sports}
    return render(request, 'sports/list.html', ctx)


def create_sport(request):
    if request.method == "POST":
        name = request.POST.get('name')
        location = request.POST.get('location')
        date = request.POST.get('date')
        sport_type = request.POST.get('sport_type')
        if name and location and date and sport_type:
            Sport.objects.create(
                name=name,
                location=location,
                date=date,
                sport_type=sport_type,
            )
            return redirect('sports:sport_list')
    return render(request, 'sports/form.html')


def update_sport(request, sport_id):
    sport = get_object_or_404(Sport, pk=sport_id)

    if request.method == "POST":
        name = request.POST.get('name')
        location = request.POST.get('location')
        date = request.POST.get('date')
        sport_type = request.POST.get('sport_type')

        if location and name and date and sport_type:
            sport.name = name
            sport.location = location
            sport.date = date
            sport.sport_type = sport_type
            sport.save()

            return redirect('sports:sport_detail', sport_id=sport.pk)

    ctx = {'sport': sport}
    return render(request, 'sports/form.html', ctx)



def sport_detail(request, sport_id):
    sport = get_object_or_404(Sport, pk=sport_id)
    ctx = {'sport': sport}
    return render(request, 'sports/detail.html', ctx)


def sport_delete(request, sport_id):
    sport = get_object_or_404(Sport, pk=sport_id)
    sport.delete()
    return redirect('sports:sport_list')