from django.shortcuts import render, redirect
from .models import client, project, requirement, task, rol, error, comment
from .forms import client_form, project_form, requirement_form, task_form, rol_form, error_form, comment_form

# Create your views here.
def index(request):
    return render(request, 'index.html')

# client
def list_client(request):
	data = client.objects.all()
	return render(request, 'client/client_list.html', {'data': data})


def create_client(request):
	if request.method == 'POST':
		form = client_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_client')
	else:
		form = client_form()
		return render(request, 'client/client.html', {'form': form})


def update_client(request, id):
    data = client.objects.get(id = id)
    form = client_form(request.POST or None, instance = data)
    if form.is_valid():
        form.save()
        return redirect('list_client')
    return render(request, 'client/client.html', {'form': form, 'data': data})


def delete_client(request, id):
    data = client.objects.get(id = id)
    if(request.method == 'POST'):
        data.delete()
        return redirect('list_client')
    return render(request, 'delete_confirm.html')

# client projects
def view_client(request, id):
    data = client.objects.filter(id = id)
    return render(request, '.html', {'data': data})

def client_projects(request, id):
    data = projects.objects.filter(id = id)
    return render(request, '.html', {'data': data})
# end client


# project
def list_project(request):
	data = project.objects.all()
	return render(request, 'project/project_list.html', {'data': data})


def create_project(request):
	if request.method == 'POST':
		form = project_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_project')
	else:
		form = project_form()
		return render(request, 'project/project.html', {'form': form})


def update_project(request, id):
    data = project.objects.get(id = id)
    form = project_form(request.POST or None, instance = data)
    if form.is_valid():
        form.save()
        return redirect('list_project')
    return render(request, 'project/project.html', {'form': form, 'data': data})


def delete_project(request, id):
    data = project.objects.get(id = id)
    if(request.method == 'POST'):
        data.delete()
        return redirect('list_project')
    return render(request, 'delete_confirm.html')
# end project


# requirement
def list_requirement(request):
	data = requirement.objects.all()
	return render(request, 'requirement/requirement_list.html', {'data': data})


def create_requirement(request):
	if request.method == 'POST':
		form = requirement_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_requirement')
	else:
		form = requirement_form()
		return render(request, 'requirement/requirement.html', {'form': form})


def update_requirement(request, id):
    data = requirement.objects.get(id = id)
    form = requirement_form(request.POST or None, instance = data)
    if form.is_valid():
        form.save()
        return redirect('list_requirement')
    return render(request, 'requirement/requirement.html', {'form': form, 'data': data})


def delete_requirement(request, id):
    data = requirement.objects.get(id = id)
    if(request.method == 'POST'):
        data.delete()
        return redirect('list_requirement')
    return render(request, 'delete_confirm.html')
# end requirement


# task
def list_task(request):
	data = task.objects.all()
	return render(request, 'task/task_list.html', {'data': data})


def create_task(request):
	if request.method == 'POST':
		form = task_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_task')
	else:
		form = task_form()
		return render(request, 'task/task.html', {'form': form})


def update_task(request, id):
    data = task.objects.get(id = id)
    form = task_form(request.POST or None, instance = data)
    if form.is_valid():
        form.save()
        return redirect('list_task')
    return render(request, 'task/task.html', {'form': form, 'data': data})


def delete_task(request, id):
    data = task.objects.get(id = id)
    if(request.method == 'POST'):
        data.delete()
        return redirect('list_task')
    return render(request, 'delete_confirm.html')
# end task


# error
def list_error(request):
	data = error.objects.all()
	return render(request, 'error/error_list.html', {'data': data})


def create_error(request):
	if request.method == 'POST':
		form = error_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_error')
	else:
		form = error_form()
		return render(request, 'error/error.html', {'form': form})


def update_error(request, id):
    data = error.objects.get(id = id)
    form = error_form(request.POST or None, instance = data)
    if form.is_valid():
        form.save()
        return redirect('list_error')
    return render(request, 'error/error.html', {'form': form, 'data': data})


def delete_error(request, id):
    data = error.objects.get(id = id)
    if(request.method == 'POST'):
        data.delete()
        return redirect('list_error')
    return render(request, 'delete_confirm.html')
# end error


# comments
def list_comment(request):
	data = comment.objects.all()
	return render(request, 'comment/comment_list.html', {'data': data})


def create_comment(request):
	if request.method == 'POST':
		form = comment_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_comment')
	else:
		form = comment_form()
		return render(request, 'comment/comment.html', {'form': form})


def update_comment(request, id):
    data = comment.objects.get(id = id)
    form = coment_form(request.POST or None, instance = data)
    if form.is_valid():
        form.save()
        return redirect('list_comment')
    return render(request, 'comment/comment.html', {'form': form, 'data': data})


def delete_comment(request, id):
    data = comment.objects.get(id = id)
    if(request.method == 'POST'):
        data.delete()
        return redirect('list_comment')
    return render(request, 'delete_confirm.html')
# end comment


# rol
def list_rol(request):
	data = rol.objects.all()
	return render(request, 'rol/rol_list.html', {'data': data})


def create_rol(request):
	if request.method == 'POST':
		form = rol_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_rol')
	else:
		form = rol_form()
		return render(request, 'rol/rol.html', {'form': form})


def update_rol(request, id):
    data = rol.objects.get(id = id)
    form = rol_form(request.POST or None, instance = data)
    if form.is_valid():
        form.save()
        return redirect('list_rol')
    return render(request, 'rol/rol.html', {'form': form, 'data': data})


def delete_rol(request, id):
    data = rol.objects.get(id = id)
    if(request.method == 'POST'):
        data.delete()
        return redirect('list_rol')
    return render(request, 'delete_confirm.html')
# end rol
