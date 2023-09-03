from django.shortcuts import render, redirect
from .models import Member
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.serializers import serialize

def index(request):
    return render(request, 'StaffApp/index.html')

def rules(request):
    return render(request, 'StaffApp/rules.html')

def staff(request):
    members = Member.objects.all()

    is_superstaff = request.user.is_superuser
    print(is_superstaff)

    return render(request, 'StaffApp/faculty-members.html', {'members': members, 'is_superstaff':is_superstaff})

def online_tables(request):
    return render(request, 'StaffApp/online-tables.html')

def add_member(request):
    if request.method == "POST":
        name_in_latin = request.POST.get('name_in_latin')
        email = request.POST.get('email')
        category = request.POST.get('category')
        research_interests = request.POST.get('research_interests')  # Depending on how you implement this
        profile_photo = request.FILES.get('profile_photo')
        short_cv = request.POST.get('short_cv')
        full_cv = request.POST.get('full_cv')
        scopus = request.POST.get('scopus')
        google_scholar = request.POST.get('google_scholar')
        web_of_science = request.POST.get('web_of_science')
        orcid = request.POST.get('orcid')
        additional_info = request.POST.get('additional_info')

        # Now create the Member instance and save
        member = Member(
            name=name_in_latin,
            email=email,
            category=category,
            research_interests=research_interests,
            profile_photo=profile_photo,
            short_cv=short_cv,
            full_cv=full_cv,
            scopus=scopus,
            google_scholar=google_scholar,
            web_of_science=web_of_science,
            orcid=orcid,
            additional_info=additional_info
        )
        member.save()

        return redirect('/department/staff/')  # Replace with your redirect view name

    return redirect('/department/staff/')  # Replace with your template path

@csrf_exempt
def delete_staff(request, staff_id):
    if request.method == "DELETE":
        try:
            staff_member = Member.objects.get(pk=staff_id)
            staff_member.delete()
            return JsonResponse({'success': True})
        except Member.DoesNotExist:
            return JsonResponse({'success': False})
    return JsonResponse({'success': False})

def staff_details(request, staff_name):
    staff = Member.objects.get(name=staff_name)
    staff.research_interests = staff.research_interests.split('/*/')
    staff.research_list = staff.written_researches.all()

    user = request.user
    user.full_name = user.first_name +' '+ user.last_name
    
    members = Member.objects.all()

    members_name_list = []
    for member in members:
        members_name_list.append(member.name)

    return render(request, 'StaffApp/member-details.html', {'staff':staff, 'members':members_name_list})

'''
@csrf_exempt
def edit_member(request, id):
    if request.method == "POST":
        try:
            member = Member.objects.get(pk=id)  # replace YourMemberModel with your model name
        except Member.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Member not found!'})
        
        uploaded_photo = request.FILES.get('profile_photo')
        if uploaded_photo:
            # Save the new photo and handle it as per your logic
            member.profile_photo = uploaded_photo
        else:
            # If no new photo has been uploaded, retain the existing image using the value from 'current_profile_photo'
            existing_photo_path = request.POST.get('current_profile_photo')


        member.name = request.POST.get('name_in_latin')
        member.email = request.POST.get('email')
        member.category = request.POST.get('category')
        member.research_interests = request.POST.get('research_interests')  # Depending on how you implement this
        member.short_cv = request.POST.get('short_cv')
        member.full_cv = request.POST.get('full_cv')
        member.scopus = request.POST.get('scopus')
        member.google_scholar = request.POST.get('google_scholar')
        member.web_of_science = request.POST.get('web_of_science')
        member.orcid = request.POST.get('orcid')
        member.additional_info = request.POST.get('additional_info')
        # ... similarly update other fields ...

        profile_photo = request.FILES.get('profile_photo', None)
        if profile_photo:
            # If you want to overwrite the old image, you might want to delete it first
            if member.profile_photo:
                member.profile_photo.delete()
                
            fs = FileSystemStorage()
            filename = fs.save(profile_photo.name, profile_photo)
            member.profile_photo = fs.url(filename)

        member.save()
        return redirect(f'/department/staff/{member.pk}/')
        return JsonResponse({'status': 'success', 'message': 'Successfully updated member!'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request!'})
'''

@csrf_exempt
def edit_member(request, id):
    if request.method == "POST":
        # ... [rest of the code] ...
        member = Member.objects.get(pk=id)
        member.name = request.POST.get('name_in_latin')
        member.email = request.POST.get('email')
        member.category = request.POST.get('category')
        member.research_interests = request.POST.get('research_interests')  # Depending on how you implement this
        member.short_cv = request.POST.get('short_cv')
        member.full_cv = request.POST.get('full_cv')
        member.scopus = request.POST.get('scopus')
        member.google_scholar = request.POST.get('google_scholar')
        member.web_of_science = request.POST.get('web_of_science')
        member.orcid = request.POST.get('orcid')
        member.additional_info = request.POST.get('additional_info')


        profile_photo = request.FILES.get('profile_photo', None)
        if profile_photo:
            # If you want to overwrite the old image, you might want to delete it first
            if member.profile_photo:
                member.profile_photo.delete()
                
            member.profile_photo = profile_photo
        member.save()

        # Redirect to desired page after saving, e.g., the detail page for the edited member
        return redirect(f'/department/staff/{member}/')
        
    # If it's not a POST request or there's an issue, you can handle it appropriately here
    return render(request, 'error_template.html', context={...})

@csrf_exempt
def registrate(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        name = request.POST.get('name')
        email = request.POST.get('email-register')
        password = request.POST.get('password-register')

        #print('TEST REGISTER')

        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'error': 'Email already exists'})

        # Splitting the name into first and last for the User model
        first_name, last_name = name.split(maxsplit=1) if ' ' in name else (name, "")

        user = User(username=email, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()

        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def ajax_login(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        
        # Debugging
        print("Received email:", username)
        print("Received password:", password)

        user = authenticate(request, username=username, password=password)
        
        # Debugging
        print("User object after authenticate:", user)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid login credentials'})

    return JsonResponse({'success': False, 'error': 'Not a POST request'})