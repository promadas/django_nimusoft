from django.shortcuts import render,redirect
from .models import contacts
from .home1 import FormSubmitForm
# Create your views here.
def home1(request):
    
    contact_list = contacts.objects.all().values()
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
        'contacts': contact_list
        
    }
    return render(request, 'home1.html',context) 

def update1(request, pk):
  
  Contact = contacts.objects.get(id=pk)
  
  if request.method == "POST":
      
      form = FormSubmitForm(request.POST, instance=Contact)
      
      if form.is_valid():
          form.save()
      
          return redirect('/home1')
      
      else:
          
          return redirect('/home1')
  
  else:
      pass
  
  
  context = {
      
      'contacts': Contact
      
  }
  return render(request,'update1.html', context)

