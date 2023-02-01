from django.shortcuts import render,redirect
from .form import FormSubmitForm
from .models import contact

# Create your views here.
def home(request):
    return render(request,'home.html')

def form_submit(request):
    contact_list = contact.objects.all().values()
    if request.method == 'POST':
        
        form = FormSubmitForm(request.POST)
        
        if form.is_valid():
           
            form.save()
            
            return redirect(request.path_info)
        
        else:
            
            form = FormSubmitForm()
            return redirect(request.path_info)
    
    
    else:
        form = FormSubmitForm()
        
    context = {
        'form': form ,
        'contact': contact_list
        
    }
 
    return render(request, 'form.html',context) 

def update(request, pk):
  
  Contact = contact.objects.get(id=pk)
  
  if request.method == "POST":
      
      form = FormSubmitForm(request.POST, instance=Contact)
      
      if form.is_valid():
          form.save()
      
          return redirect('/form')
      
      else:
          
          return redirect('/form')
  
  else:
      pass
  
  
  context = {
      
      'contact': Contact
      
  }
  
  return render(request,'update.html', context)

def delete(request, pk):
  
  Contact = contact.objects.get(id=pk)
  
  if request.method == "POST":
      
      Contact.delete()
      
      return redirect('/form')
  
  else:
      pass
  
  
  context = {
      
      'contact': Contact
      
  }
  
  return render(request,'delete.html', context)

    
    
    
