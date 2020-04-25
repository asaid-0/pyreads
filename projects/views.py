from django.shortcuts import render
from .forms import AddProjectForm, ImageForm, CommentForm, DonateForm
from django.shortcuts import redirect
from django.db.models import Sum, Avg
from users.models import Project, Comment, Category, Donation, Project_pictures, User, Rate, Project_pictures as Pics
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json

comment_form = CommentForm()

@login_required
def add_project(request):
    current_user = request.user
    if request.method == "POST":
        form = AddProjectForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        if form.is_valid() and image_form.is_valid():
            new_project = form.save(commit=False)
            new_project.owner_id = current_user.id
            new_project.save()
            form.save_m2m()
            for file in request.FILES.getlist("picture"):
                picture = Project_pictures(project=new_project, picture=file)
                picture.save()
            return redirect("user_projects")
    else:
        form = AddProjectForm()
        image_form = ImageForm()
    return render(
        request, "projects/add_project.html", {"form": form, "image_form": image_form},
    )


@login_required
def view_project(request, id, form=CommentForm()):
    global comment_form
    project = Project.objects.get(id=int(id))
    pics = Pics.objects.filter(project=project)
    project_donations = project.donation_set.aggregate(total_amount=Sum('amount'))
    project_rate = project.rate_set.aggregate(rate = Avg('rate'))
    reported_comments = []
    for comment in request.user.comment_reports.filter(project=project):
        reported_comments.append(comment.id)
    context = {
                "project": project,
                "is_reported": request.user.project_reports.filter(id=project.id).exists(),
                "reported_comments": reported_comments,
                "project_donations": project_donations,
                "rate":project_rate['rate'], "range": range(pics.count()),
                "pics": pics,
                "form": comment_form,
                "donation_form": DonateForm()
            }
        
    return render(request, "projects/view.html", context)


def delete_project(request , id):
    if request.user.is_authenticated:
        if request.method == "POST":
            
                
                project_donations = project.donation_set.aggregate(total_amount=Sum('amount'))
                project_donations = project_donations if  project_donations['total_amount'] else {'total_amount': 0} 
                if (project.total_target*0.25 >  project_donations['total_amount']) or project_donations.total_amount == None:
                    project.delete()
                    return redirect("user_projects") # with message deleted successfully
                else:
                    return redirect("user_projects")
        else:
            return redirect("user_projects")
    return redirect("home")




@login_required
def delete_project(request, id):
    if request.method == "POST":
        project = Project.objects.filter(id=id)
        if project.exists() and project.first().owner == request.user:
            project = project.first()
            project_donations = project.donation_set.aggregate(total_amount=Sum("amount"))
            project_donations = (
                project_donations
                if project_donations["total_amount"]
                else {"total_amount": 0}
            )
            if (
                project.total_target * 0.25 > project_donations["total_amount"]
            ) or project_donations.total_amount == None:
                project.delete()
                return redirect("user_projects")  # with message deleted successfully
            else:
                return redirect("user_projects")
    return redirect("user_projects")


@login_required
def report_comment(request, id):
    if request.method == "POST":
        comment = Comment.objects.filter(id=id)
        if comment.exists():
            comment = comment.first()
            if not request.user.comment_reports.filter(id=comment.id).exists():
                request.user.comment_reports.add(comment)
            return redirect("view_project", id=comment.project_id)
    return redirect("home")
    

@login_required
def report_project(request, id):
    if request.method == "POST":
        project = Project.objects.filter(id=id)
        if project.exists():
            project = project.first()
            if not request.user.project_reports.filter(id=project.id).exists():
                request.user.project_reports.add(project)
            return redirect("view_project", id=project.id)
    return redirect("home")


@login_required
def add_comment(request, id):
    global comment_form
    comment_form = CommentForm(request.POST)
    project = Project.objects.filter(id=int(id))
    if not (project.exists() and request.user.is_authenticated):
        return redirect("home")

    if request.method.lower() == "get":
        return redirect("view_project", id=project.first().id)

    if comment_form.is_valid():
        user = request.user
        create_comment = comment_form.save(commit=False)
        create_comment.user = user
        create_comment.project = project.first()
        create_comment.save()
        return redirect("view_project", id=project.first().id)
    else:
        return redirect("view_project", id=project.first().id)

@login_required
def get_category_projects(request, id):
    category = Category.objects.get(id=id)
    projects = category.project_set.all()
    context = {"projects": projects, "category": category}
    return render(request, "projects/category_projects.html", context)

@login_required
def add_donation(request):
    if request.is_ajax and request.method == 'POST':
        #save donation 
        if float(request.POST['amount']) > 0:
            try:
                project_id = request.POST['project_id']
                project = Project.objects.get(id=project_id)

                donation = Donation()
                donation.user = request.user
                donation.amount = request.POST['amount']
                donation.project = project
                donation.save()
                
                #return amount of donations
                donations = project.donation_set.aggregate(amount=Sum('amount'))
                return HttpResponse(json.dumps({'donations': donations['amount']}), content_type="application/json")

            except:
                return HttpResponse(json.dumps({'error': "Something went wrong"}), content_type="application/json", status=403)
        else:
            return HttpResponse(json.dumps({'error': "Something went wrong"}), content_type="application/json", status=403)
    else:
        return HttpResponse(json.dumps({'error': "Something went wrong"}), content_type="application/json", status=400)
