from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages

from pharmacy.stalk.models import Category, Medicine

# Create your views here.
# adds a new medicine in the stock
def add_medicine(request):
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        manufacturer = request.POST['manufacturer']
        price = request.POST['price']
        stock_quantity = request.POST['stock_quantity']
        expiration_date = request.POST['expiration_date']
        category_id = request.POST.get('category_id')
        image = request.FILES.get('image')
    
        category = Category.objects.get(id=category_id) if category_id else None
        
        Medicine.objects.create(name=name, category=category, manufacturer=manufacturer,
                                price=price, stock_quantity=stock_quantity, expiration_date=expiration_date)
        messages.success(request, "Added medicine successfully!")
        
        return redirect('medicine_list')
    return render(request, 'stalk/add_medicine.html', {'categories': Category.objects.all()})

# returns all  the medicine available in stock
def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'stalk/medicine_list.html', {'medicines': medicines})

# updates the details of a medicine in stock
def update_medicine(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    if request.method == 'POST':
        medicine.name = request.POST['name']
        category_id = request.POST.get('category_id')
        medicine.category = Category.objects.get(id=category_id) if category_id else None
        medicine.manufacturer = request.POST['manufacturer']
        medicine.price = request.POST['price']
        medicine.stock_quantity = request.POST['stock_quantity']
        medicine.expiration_date = request.POST['expiration_date']
        
        if 'image' in request.FILES:
            medicine.image = request.FILES['image']
            
        medicine.save()
        messages.success(request, "Updated medicine successfully!")
        return redirect('medicine_list')
    return render(request, 'stalk/update_medicine.html', {'medicine': medicine, 'categories': Category.objects.all()})

# deletes a medicine from the stock
def delete_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    if request.method == 'POST':
        medicine.delete()
        messages.success(request, "Deleted medicine successfully!")
        return redirect('medicine_list')
    return render(request, 'stalk/delete_medicine.html', {'medicine': medicine})

# privies images
def preview_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    return render(request, 'preview_medicine.html', {'medicine': medicine})
