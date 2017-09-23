from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # UpdateView for editing object.
from django.core.urlresolvers import reverse_lazy
from .models import Filter, Result
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .script import findEBayData
from .script import searchSetups


class IndexView(generic.ListView):
    template_name = 'miner/index.html'
    context_object_name = 'filter_list'

    def get_queryset(self):
        return Filter.objects.all()


#
class DetailView(generic.DetailView):
    """DetailView expects a primary key of a Filter object"""
    model = Filter
    template_name = 'miner/detail.html'


class FilterCreate(CreateView):
    model = Filter
    fields = ['filter_title', 'filter_description', 'filter_script']


class FilterUpdate(UpdateView):
    model = Filter
    fields = ['filter_title', 'filter_description', 'filter_script']


class FilterDelete(DeleteView):
    model = Filter
    success_url = reverse_lazy('miner:index')


# TODO: finish result deletion feature in detail view
class ResultDelete(DeleteView):
    model = Result
    success_url = reverse_lazy('miner:detail')

def favorite_filter(request, filter_id):
    filter = get_object_or_404(Filter, pk=filter_id)
    try:
        if filter.is_favorite:
            filter.is_favorite = False
        else:
            filter.is_favorite = True
            filter.save()
    except (KeyError, Filter.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})

def run_testScript(request):
    laserUrl = "https://www.ebay.co.uk/sch/Business-Office-Industrial" \
               "/12576/i.html?_from=R40&LH_ItemCondition=2500%7C3000%7C7000%7C10&_nkw=Laser&_sop=15"
    minLaserPower = 10  # Watts
    maxLaserPrice = 5000.00  # Pounds
    search1 = searchSetups.LaserSearch(minLaserPower, maxLaserPrice)

    findEBayData.mainSearchMethod(search1, laserUrl, False)

    return render(request, 'miner/index.html', {'filter_list': Filter.objects.all()})