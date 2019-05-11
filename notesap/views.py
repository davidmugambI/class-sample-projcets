from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from .models import Note
from .forms import NoteForm,UpdateForm
# Create your views here.

def index(request): #Both creates and retrieves
	notes_taken = Note.objects.all().order_by('-created')
	#template = loader.get_template('notesap/index.html')
	#return HttpResponse("Its just a beginner")
	form = NoteForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()

	context = {
	'notes_taken': notes_taken,
	'form': form
	}
	#return HttpResponse(template.render(context,request))
	return render(request, 'notesap/index.html', context)

def delete(request, id):
    noteedit = get_object_or_404(Note, id=id)
    noteedit.delete()
    messages.success(request,'Note deleted')
    return render(request, 'notesap/delete.html', {'noteedit': noteedit})
    return HttpResponseRedirect('')

def update(request,id=None):
    noteedit = get_object_or_404(Note, id=id)
    form = UpdateForm(request.POST or None, instance=noteedit)
    if form.is_valid():
        noteedit = form.save(commit=False)
        noteedit.save()
        messages.success(request, "Note successfully updated")
    else:
	form = UpdateForm(instance=noteedit)
    return render(request, 'notesap/update.html', {'form': form, 'noteedit': noteedit})

	


'''
def post_update(request):
if request.method == 'POST':
    form = UpdateForm(data=request.POST)
    if form.is_valid():
        update = form.save(commit=False)
        update.author = request.user
        form.save()
        return redirect('updates:update_list')
else:
    form = UpdateForm()
return render(request, 'updates/post/post_update.html', {'form': form})


class UpdateListView(ListView):
    queryset = Update.objects.all()
    context_object_name = 'updates'
    paginate_by = 5
    template_name = 'updates/post/update_list.html'


@login_required
def update_detail(request, update_id):
    try:
        update = Update.objects.get(id=update_id)
    except Update.DoesNotExist:
        raise Http404('Update does not exist')
    return render(request, 'updates/post/detail.html', {'update': update})
'''
