from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from judo.forms import FAQForm, FAQEditForm
from judo.models import FAQ


# Create your views here.

def index(request):
    return render(request, 'judo/index.html',context = {})

def about(request):
    return render(request, 'judo/about.html',context = {})

def faq(request):
    # Retrieve existing FAQs
    faqs = FAQ.objects.all()

    # Add the FAQs to the context dictionary
    context = {'faqs': faqs}

    # Render the 'judo/faq.html' template with the context
    return render(request, 'judo/faq.html', context)

def merch(request):
    return render(request, 'judo/merch.html',context = {})

def contact(request):
    return render(request, 'judo/contact.html',context = {})

#Staff views below

def dashboard(request):
    return render(request, 'judo/staff/dashboard.html',context = {})

def staff_merch(request):
    return render(request, 'judo/staff/staff_merch.html',context = {})

def staff_faq(request):
    # Handle form submission
    if request.method == 'POST':
        faq_form = FAQForm(request.POST)
        if faq_form.is_valid():
            faq_form.save()
            return redirect('judo:dashboard')  # Redirect to the FAQ page after submission

    else:
        faq_form = FAQForm()

    # Retrieve existing FAQs
    faqs = FAQ.objects.all()

    return render(request, 'judo/staff/staff_faq.html', {'faq_form': faq_form, 'faqs': faqs})

def edit_faq(request, faq_id):
    faq = get_object_or_404(FAQ, pk=faq_id)
    if request.method == 'POST':
        edit_form = FAQEditForm(request.POST, instance=faq)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('judo:staff_faq')

    else:
        edit_form = FAQEditForm(instance=faq)

    faqs = FAQ.objects.all()
    return render(request, 'judo/staff/staff_faq.html', {'faq_form': FAQForm(), 'edit_form': edit_form, 'faqs': faqs})

def delete_faq(request, faq_id):
    # Fetch the FAQ entry with the specified ID
    faq = get_object_or_404(FAQ, pk=faq_id)

    # Delete the FAQ entry from the database
    faq.delete()

    # Redirect back to the staff FAQ page after deletion
    return redirect(reverse('judo:staff_faq'))

def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
        # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return render(request, 'judo/index.html')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your GUJC account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print(f"Invalid login details: {username}, {password}")
            messages.info(request, 'Invalid username or password.')
            #return redirect(reverse('just_for_fun:login'))
            #return HttpResponse("Invalid login details supplied. Return to previous page to retry")
        # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'judo/staff/login.html')
    context = {}
    return render(request, 'judo/staff/login.html',context)
@login_required
def user_logout(request):
# Since we know the user is logged in, we can now just log them out.
    logout(request)
# Take the user back to the homepage.
    return redirect(reverse('judo:index'))
