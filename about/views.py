from django.shortcuts import render
from about.models import TeamMember, Link, Media

def about(request):
	team = TeamMember.objects.all()
	links = Link.objects.all()
	media = Media.objects.all()
	context = {'team': team, 'links': links, 'media': media}
	return render(request, 'about/about.html', context)

