from django.shortcuts import render
from django.conf import settings

'''
Basic view for displaying our scheduled job
'''
def index(request):
	return render(request, 'main/index.html', context)


