from django.shortcuts import render, redirect, get_object_or_404
from .models import POSCollection,POSCategory,POSDetail, Order
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import OrderCreateForm
from .tasks import order_created
from video.views import download_link
from essay.views import download_link_es





def homepage(request):
    download_link.clear()
    download_link_es.clear()
    return render(request, "POS/categories.html", {"categories": POSCategory.objects.all()})




def single_slug(request,single_slug):
    download_link.clear()
    download_link_es.clear()

    categories = [c.category_slug for c in POSCategory.objects.all()]
    if single_slug in categories:
        matching_series = POSCollection.objects.filter(POS_category__category_slug=single_slug)

        series_urls = {}
        for m in matching_series.all():
            part_one = POSDetail.objects.filter(POS_brand__POS_brand=m.POS_brand).earliest("date")
            series_urls[m] = part_one.POS_slug

        return render(request, "POS/category.html", {"part_ones":series_urls,
                                                       "categories": POSCategory.objects.all()})


    POS = [t.POS_slug for t in POSDetail.objects.all()]
    if single_slug in POS:

        this_POS = POSDetail.objects.get(POS_slug=single_slug)
        posts_from_series = POSDetail.objects.filter(POS_brand__POS_brand=this_POS.POS_brand).order_by("date")


        this_tutorial_idx = list(posts_from_series).index(this_POS)








        return render(request, 'POS/postshow.html',{"posts":this_POS,
                                                     "sidebar": posts_from_series,
                                                     "this_tutorial_idx":this_tutorial_idx,

                                                    })

    return HttpResponse('<h1>404</h1>')




def order_create(request):
    download_link.clear()
    download_link_es.clear()

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()
            return render(request, 'POS/created.html', {'order': order})

    else:
        form = OrderCreateForm()
    return render(request, 'POS/create.html', {'form': form})

