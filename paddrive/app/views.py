from django.shortcuts import render, redirect

# Create your views here.
from .models import HomepageSlides, Mission, Project, SocialEvents, Admins, Stats, Blog, Quotes, ContactInformation, Feedback, Photo


def index(request):
    slides = HomepageSlides.objects.all()
    missions = Mission.objects.all()
    projects = Project.objects.all()
    events = SocialEvents.objects.all()

    admins = Admins.objects.all()
    stats = Stats.objects.all()
    quotes = Quotes.objects.all()
    contacts = ContactInformation.objects.all()
    blogs = Blog.objects.all()[1:]
    return render(request, "index.html",
                  context={"slides": slides,
                           "missions": missions,
                           "projects": projects,
                           "events": events,
                           "admins": admins,
                           "stats": stats,
                           "quotes": quotes,
                           "contacts": contacts,
                           "blogs": blogs
                           }
                  )


def about(request):
    missions = Mission.objects.all()
    contacts = ContactInformation.objects.all()
    return render(request, "about.html", context={"missions": missions, "contacts": contacts})


def contact(request):
    if request.method == "GET":
        missions = Mission.objects.all()
        contacts = ContactInformation.objects.all()
        return render(request, "contact.html", context={"missions": missions, "contacts": contacts})
    elif request.method == "POST":
        if not request.POST['name'] or not request.POST['message'] or not request.POST['email'] or not request.POST['subject']:
            return redirect("/contact")
        try:
            feedback = Feedback(
                name=request.POST['name'],
                message=request.POST['message'],
                email=request.POST['email'],
                subject=request.POST['subject']
            )
            feedback.save()
        except:
            return redirect("/contact")
        return redirect("/")


def blog(request):
    if request.method == "GET":
        missions = Mission.objects.all()
        contacts = ContactInformation.objects.all()
        blogs = Blog.objects.all()
        return render(request, "blog.html", context={"missions": missions, "contacts": contacts, "blogs": blogs})


def blog_detail(request, id):
    if request.method == "GET":
        blog_match = Blog.objects.get(id=id)
        missions = Mission.objects.all()
        contacts = ContactInformation.objects.all()
        return render(request, "blog_details.html", context={"missions": missions, "contacts": contacts, "blog": blog_match})


def gallery(request):
    if request.method == "GET":
        images = Photo.objects.all()
        return render(request, "gallery.html", context={"images": images})
