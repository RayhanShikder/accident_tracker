from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from scrapper.models import Toy

class ToyForm(ModelForm):
    class Meta:
        model = Toy
        fields = ['name', 'start_age']

def toy_list(request, template_name='toy/toy_list.html'):
    toy = Toy.objects.all()
    data = {}
    data['object_list'] = toy
    return render(request, template_name, data)

def toy_view(request, pk, template_name='toy/toy_detail.html'):
    toy = get_object_or_404(Toy, pk=pk)    
    return render(request, template_name, {'object':toy})

def toy_create(request, template_name='toy/toy_form.html'):
    form = ToyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('toy_list')
    return render(request, template_name, {'form':form})

def toy_update(request, pk, template_name='toy/toy_form.html'):
    toy= get_object_or_404(Toy, pk=pk)
    form = ToyForm(request.POST or None, instance=toy)
    if form.is_valid():
        form.save()
        return redirect('toy_list')
    return render(request, template_name, {'form':form})

def toy_delete(request, pk, template_name='toy/toy_confirm_delete.html'):
    toy= get_object_or_404(Toy, pk=pk)    
    if request.method=='POST':
        toy.delete()
        return redirect('toy_list')
    return render(request, template_name, {'object':toy})