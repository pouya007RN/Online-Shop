from django.shortcuts import render, redirect, get_object_or_404
from .models import Videos, VideoCategory, VideoDetail, VideoDownload, Order, Comment
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from random import randint
from .forms import OrderCreateForm, CommentForm
from .tasks import order_created
#from essay.views import download_link_es




download_link = []


def homepage(request):
    global download_link
    download_link.clear()
    #download_link_es.clear()

    return render(request, "video/categories.html", {"categories": VideoCategory.objects.all()})

def canceled(request):
    global download_link
    download_link.clear()
    #download_link_es.clear()
    return render(request, 'video/BadReq.html')


def single_slug(request,single_slug):
    global download_link
    #download_link_es.clear()
    download_link.clear()

    categories = [c.category_slug for c in VideoCategory.objects.all()]
    if single_slug in categories:
        matching_series = Videos.objects.filter(video_category__category_slug=single_slug)

        series_urls = {}
        for m in matching_series.all():
            part_one = VideoDetail.objects.filter(video_title__video_title=m.video_title).earliest("date")
            series_urls[m] = part_one.video_slug

        return render(request, "video/category.html", {"part_ones":series_urls,
                                                       "categories": VideoCategory.objects.all(),
                                                       })


    videos = [t.video_slug for t in VideoDetail.objects.all()]
    if single_slug in videos:

        this_tutorial = VideoDetail.objects.get(video_slug=single_slug)
        posts_from_series = VideoDetail.objects.filter(video_title__video_title=this_tutorial.video_title).order_by("date")


        this_tutorial_idx = list(posts_from_series).index(this_tutorial)

        post = get_object_or_404(VideoDetail, video_slug=single_slug)

        comments = Comment.objects.filter(post=post).order_by("-timestamp")

        if request.method == "POST":
            comment_form = CommentForm(request.POST or None)
            if comment_form.is_valid():
                content = request.POST.get('دیدگاه')
                name = request.POST.get('نام')
                comment = Comment.objects.create(post=post, نام=name, دیدگاه=content)
                comment.save()
                return HttpResponseRedirect(single_slug)

        else:
            comment_form = CommentForm()

        download_link.append(single_slug)


        return render(request, 'video/postshow.html',{"posts":this_tutorial,
                                                     "sidebar": posts_from_series,
                                                     "this_tutorial_idx":this_tutorial_idx,
                                                      "comments": comments,
                                                      "comment_form": comment_form,

                                                    })

    return HttpResponse('<h1>404</h1>')







def link(request,link,url_generator):
    global download_link
    #download_link_es.clear()


    l = []
    rand = ''
    for i in range(8):
        a = randint(0, 9)
        l.append(a)

    for i in range(len(l)):
        rand += str(l[i])

    url_generator = rand



    dl_link = VideoDownload.objects.filter(video_title__video_slug=download_link[0])

    return render(request, 'video/link.html',{'link':dl_link[0],
                                              'url':url_generator,
                                              })



def order_create(request):
    global download_link
    #download_link_es.clear()

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

            order_created.delay(order.id)
            Order.paid = True

            return render(request, 'video/result.html', {'order': order,
                                                    'link': download_link[0],
                                                    'url': rand,
                                                    })

    else:
        form = OrderCreateForm()
    return render(request, 'video/create.html', {'form': form})






