from django.shortcuts import render
from .models import Category,Project,ProjectImage,Product,ProductImage
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    
    products = Product.objects.all()
    projects = Project.objects.all()
    return render(request,'Warzone/home.html',{'projects':projects,'products':products});

def product(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'Warzone/product.html', {'categories': categories,'products': products},)

def project(request):
    projects = Project.objects.all()
    
    return render(request, 'Warzone/work.html', {'projects': projects})

def project_detail(request,project_id):
    project = get_object_or_404(Project,pk=project_id)
    images = project.images.all()
    return render(request,'Warzone/projectdetail.html',{'project':project,'images':images})
    
    


def product_list(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.products.all()  # Uses the related_name 'projects'
    return render(request, 'Warzone/category_detail.html', {'category': category, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    images = product.images.all()  # Uses the related_name 'images'
    return render(request, 'Warzone/productdetail.html', {'product': product, 'images': images})

def services(request):
    return render(request, 'Warzone/services.html')
def work(request):
    return render(request, 'Warzone/work.html')
def about(request):
    return render(request, 'Warzone/about.html')
def contact(request):
    return render(request, 'Warzone/contact.html')

def contactc(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Get the form data to send in the email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            description = form.cleaned_data['description']
            
            # Compose the email content
            subject = f'New Contact Message from {name}'
            message = f"Name: {name}\nEmail: {email}\nPhone: {mobile}\nMessage: {description}"
            recipient_email = 'najus777@gmail.com'  # Replace with the recipient's email address
            
            try:
                # Send the email using Django's send_mail function
                send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email])

                # Redirect to success page or any other appropriate page
                return redirect('Warzone:success')  # You can change 'Warzone:success' to your actual success URL
            except Exception as e:
                # Handle any errors that occur while sending the email
                print(f"Error sending email: {e}")
                return render(request, 'Warzone/contact.html', {'form': form, 'error': 'There was an error sending the email. Please try again.'})

    else:
        form = ContactForm()

    return render(request, 'Warzone/contact.html', {'form': form})
def success(request):
    return render(request, 'Warzone/success.html')