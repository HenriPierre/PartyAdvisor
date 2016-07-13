from django.shortcuts import render
from parties.models import Party

# Create your views here.
def index(request):
	# this is your new view
	partys = Party.objects.all()
	return render(request, 'index.html', {
		'partys':partys,
	})