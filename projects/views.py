from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from .models import Project, Donation

# ---------------- Landing Page ----------------
def landing_page(request):
    projects = Project.objects.all().order_by('-created_at') 
    return render(request, 'projects/landing.html', {'projects': projects})

# ---------------- Project List ----------------
@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'projects/project_list.html', {'projects': projects})

# ---------------- Create Project ----------------
@login_required
def create_project(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        target_amount = request.POST.get("target_amount")
        end_date = request.POST.get("end_date")
        image = request.FILES.get("image")

        Project.objects.create(
            title=title,
            description=description,
            target_amount=target_amount,
            end_date=end_date,
            image=image,
            owner=request.user
        )
        return redirect('project_list')

    return render(request, 'projects/create_project.html')

# ---------------- Edit Project ----------------
@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == 'POST':
        project.title = request.POST.get("title")
        project.description = request.POST.get("description")
        project.target_amount = request.POST.get("target_amount")
        project.end_date = request.POST.get("end_date")
        if request.FILES.get("image"):
            project.image = request.FILES.get("image")
        project.save()
        return redirect('project_list')

    return render(request, 'projects/edit_project.html', {'project': project})

# ---------------- Delete Project ----------------
@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    project.delete()
    return redirect('project_list')
# ---------------- Donate ----------------
@login_required
def donate(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        amount = request.POST.get("amount")
        if amount and amount.isdigit():
            amount = int(amount)
            if amount > 0:
                Donation.objects.create(project=project, amount=amount)
                return redirect('donate', pk=project.pk)

    return render(request, "projects/donate.html", {"project": project})

# ---------------- Project Detail ----------------
@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

