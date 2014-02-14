from django.shortcuts import render, get_object_or_404
from projects.models import Project, ProjectImage, Client


def index(request):
	#list of designated feature projects for index page
	projects_featured_list = Project.objects.filter(feature_project=True)
	clients = Client.objects.all()

	testimonials = []
	for client in clients:
		if client.testimonial:
			testimonials.append(client.testimonial)

	context = {'projects_featured_list': projects_featured_list, 'clients': clients, 'testimonials': testimonials}

	return render(request, 'projects/index.html', context)

def project_index(request):
	#list of all Project objects
	project_list = Project.objects.all()
	context = {'project_list': project_list}

	return render(request, 'projects/project_index.html', context)

def project_page(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	project_images = project.images
	client = project.client
	context = {'project_images': project_images, 'project': project, 'client': client}

	return render(request, 'projects/project_page.html', context)
