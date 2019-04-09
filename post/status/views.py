from django.shortcuts import render,HttpResponse
from .models import post
from .forms import post_f
# Create your views here.
def publish(request):
	if request.method=='POST':
		form=post_f(request.POST)
		if(form.is_valid):
			demo=request.POST.dict()
			d=post(author=demo.get("author"),title=demo.get("title"),text=demo.get("text"),created_date=demo.get("created_date"))
			d.publish()
			d.save()
			demo=post.objects.all()
		return render(request,"post.html",{"demo":demo})

	else:
		form=post_f()
	return render(request,'upload.html',{'form':form})		
def see(request):
	demo=post.objects.all()
	return render(request,"post.html",{"demo":demo})	
def delete_(request):
	post.objects.all().delete()
	demo=post.objects.all()
	return render(request,"post.html",{"demo":demo})
