from django.shortcuts import render, redirect, get_object_or_404
from .models import EssayDetail, EssayCategory, Essay, EssayDownload, Order, Comment
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from random import randint
from .forms import OrderCreateForm, CommentForm
from video.views import download_link



verified = False
download_link_es = []


def homepage(request):
    global download_link_es
    download_link_es.clear()
    download_link.clear()
    return render(request, "essay/categories.html", {"categories": EssayCategory.objects.all()})

def canceled(request):
    global download_link_es
    download_link_es.clear()
    download_link.clear()
    return render(request, 'essay/BadReq.html')


def single_slug(request,single_slug):
    global download_link_es
    download_link.clear()
    download_link_es.clear()
    categories = [c.category_slug for c in EssayCategory.objects.all()]
    if single_slug in categories:
        matching_series = Essay.objects.filter(essay_category__category_slug=single_slug)

        series_urls = {}
        for m in matching_series.all():
            part_one = EssayDetail.objects.filter(essay_title__essay_title=m.essay_title).earliest("date")
            series_urls[m] = part_one.essay_slug

        return render(request, "essay/category.html", {"part_ones":series_urls,
                                                       "categories": EssayCategory.objects.all(),
                                                       })


    files = [t.essay_slug for t in EssayDetail.objects.all()]
    if single_slug in files:

        this_tutorial = EssayDetail.objects.get(essay_slug=single_slug)
        posts_from_series = EssayDetail.objects.filter(essay_title__essay_title=this_tutorial.essay_title).order_by("date")


        this_tutorial_idx = list(posts_from_series).index(this_tutorial)

        post = get_object_or_404(EssayDetail, essay_slug=single_slug)

        comments = Comment.objects.filter(post=post).order_by("-timestamp")

        if request.method == "POST":
            comment_form = CommentForm(request.POST or None)
            if comment_form.is_valid():
                content = request.POST.get('دیدگاه')
                name    = request.POST.get('نام')
                comment = Comment.objects.create(post=post,نام=name, دیدگاه=content)
                comment.save()
                return HttpResponseRedirect(single_slug)
        else:
            comment_form = CommentForm()





        download_link_es.append(single_slug)


        return render(request, 'essay/postshow.html',{"posts":this_tutorial,
                                                     "sidebar": posts_from_series,
                                                     "this_tutorial_idx":this_tutorial_idx,
                                                      "comments": comments,
                                                      "comment_form": comment_form,
                                                    })

    return HttpResponse('<h1>404</h1>')







def link(request,link,url_generator):
    global download_link_es

    download_link.clear()

    l = []
    rand = ''
    for i in range(8):
        a = randint(0, 9)
        l.append(a)

    for i in range(len(l)):
        rand += str(l[i])

    url_generator = rand



    dl_link = EssayDownload.objects.filter(essay_title__essay_slug=download_link_es[0])

    return render(request, 'essay/link.html',{'link':dl_link[0],
                                              'url':url_generator,
                                              })



def order_create(request):
    global download_link_es

    download_link.clear()

    l = []
    rand = ''
    for i in range(8):
        a = randint(0, 9)
        l.append(a)

    for i in range(len(l)):
        rand += str(l[i])

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()

            Order.paid = True

            return render(request, 'essay/result.html', {'order': order,
                                                    'link': download_link_es[0],
                                                    'url': rand,
                                                    })

    else:
        form = OrderCreateForm()
    return render(request, 'essay/create.html', {'form': form})






