from django.shortcuts import render, redirect

from django.contrib.auth import get_user, logout, login
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

import customer
import user
from customer.decorators import allowed_users
from customer.models import Customer
from dashboard.models import staff_Notification
from .models import User, Profile
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

from .models import *

# Create your views here.


# views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import PDFGenerationForm
from .models import User, Profile

from django.http import HttpResponse
from django.shortcuts import render
from io import BytesIO
from reportlab.lib.pagesizes import letter, landscape, portrait
from reportlab.pdfgen import canvas
from .forms import PDFGenerationForm
from .models import User, Profile
from django.db.models import F


# def emp_pdf(request):
#     if request.method == 'POST':
#         form = PDFGenerationForm(request.POST)
#         if form.is_valid():
#             response = HttpResponse(content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
#             # template = get_template('user/pdf_template.html')
#             #
#             #
#             #
#             # response = HttpResponse(content_type='application/pdf')
#             # response['Content-Disposition'] = 'filename="generated_pdf.pdf"'
#
#             buffer = BytesIO()
#             p = canvas.Canvas(buffer, pagesize=letter)
#
#             selected_user_fields = form.cleaned_data['user_fields']
#             selected_profile_fields = form.cleaned_data['profile_fields']
#
#             users = User.objects.all()  # Fetch all User instances
#
#             y_position = 750  # Initial Y-coordinate for positioning text
#
#             for user in users:
#                 user_profile = user.profile  # Retrieve the associated Profile instance
#                 for user_field in selected_user_fields:
#                     y_position -= 15  # Move down the Y-coordinate for each field
#                     field_value = getattr(user, user_field, "")
#                     p.drawString(100, y_position, f"User - {user_field}: {field_value}")
#
#                 for profile_field in selected_profile_fields:
#                     y_position -= 15  # Move down the Y-coordinate for each field
#                     field_value = getattr(user_profile, profile_field, "")
#                     p.drawString(100, y_position, f"Profile - {profile_field}: {field_value}")
#
#             p.showPage()
#             p.save()
#
#             pdf = buffer.getvalue()
#             buffer.close()
#             response.write(pdf)
#             return response
#     else:
#         form = PDFGenerationForm()
#
#     return render(request, 'user/edit_pdf.html', {'form': form})


from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO

# def emp_pdf(request):
#     if request.method == 'POST':
#         form = PDFGenerationForm(request.POST)
#         if form.is_valid():
#             selected_user_fields = form.cleaned_data['user_fields']
#             selected_profile_fields = form.cleaned_data['profile_fields']
#
#             users = User.objects.all()
#
#             context = {
#                 'users': users,
#                 'selected_user_fields': selected_user_fields,
#                 'selected_profile_fields': selected_profile_fields,
#             }
#
#             template = get_template('user/pdf_template.html')
#             html = template.render(context)
#
#             response = HttpResponse(content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
#
#             buffer = BytesIO()
#             pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), buffer)
#
#             if not pdf.err:
#                 response.write(buffer.getvalue())
#                 buffer.close()
#                 return response
#
#     else:
#         form = PDFGenerationForm()
#
#     return render(request, 'user/edit_pdf.html', {'form': form})



from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.conf import settings

# def emp_pdf(request):
#     if request.method == 'POST':
#         form = PDFGenerationForm(request.POST)
#         if form.is_valid():
#             selected_user_fields = form.cleaned_data['user_fields']
#             selected_profile_fields = form.cleaned_data['profile_fields']
#
#             users = User.objects.all()  # Fetch all User instances
#
#             data = []  # Table data
#
#             for user in users:
#                 user_profile = user.profile  # Retrieve the associated Profile instance
#                 user_data = {
#                     'Emp ID': user.id,
#                     **{field: getattr(user, field, "") for field in selected_user_fields},
#                     **{field: getattr(user_profile, field, "") for field in selected_profile_fields}
#                 }
#                 data.append(user_data)
#
#             template = get_template('user/pdf_template.html')
#             context = {'data': data}
#             html = template.render(context)
#
#             result = BytesIO()
#             pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result, encoding="ISO-8859-1")
#             if not pdf.err:
#                 response = HttpResponse(result.getvalue(), content_type='application/pdf')
#                 response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
#                 return response
#     else:
#         form = PDFGenerationForm()
#
#     return render(request, 'user/edit_pdf.html', {'form': form})


from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.conf import settings

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
#
# def emp_pdf(request):
#     if request.method == 'POST':
#         form = PDFGenerationForm(request.POST)
#         if form.is_valid():
#             selected_user_fields = form.cleaned_data['user_fields']
#             selected_profile_fields = form.cleaned_data['profile_fields']
#
#             users = User.objects.all()  # Fetch all User instances
#
#             data = []
#             for user in users:
#                 user_profile = user.profile if hasattr(user, 'profile') else None
#                 user_data = {
#                     'User': user.username,
#                     'user_fields': {field: getattr(user, field, "") for field in selected_user_fields},
#                     'profile_fields': {field: getattr(user_profile, field, "") if user_profile else "" for field in
#                                        selected_profile_fields}
#                 }
#                 data.append(user_data)
#
#             template = get_template('user/pdf_template.html')
#             context = {'data': data, 'selected_user_fields': selected_user_fields, 'selected_profile_fields': selected_profile_fields}
#             html = template.render(context)
#
#             result = BytesIO()
#             pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result, encoding="ISO-8859-1")
#             if not pdf.err:
#                 response = HttpResponse(result.getvalue(), content_type='application/pdf')
#                 response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
#                 return response
#     else:
#         form = PDFGenerationForm()
#
#     return render(request, 'user/edit_pdf.html', {'form': form})
#

from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import render
from .forms import PDFGenerationForm
from .models import User

# def emp_pdf(request):
#     if request.method == 'POST':
#         form = PDFGenerationForm(request.POST)
#         if form.is_valid():
#             # Include additional User fields in selected_user_fields
#             selected_user_fields = form.cleaned_data['user_fields']
#             selected_profile_fields = form.cleaned_data['profile_fields']
#
#             users = User.objects.all()  # Fetch all User instances
#
#             data = []
#             for user in users:
#                 user_profile = user.profile if hasattr(user, 'profile') else None
#                 full_name = f"{user.first_name} {user.last_name}"
#
#                 # Define a dictionary to map database field names to display names
#                 field_display_names = {
#                     'first_name': 'First Name',
#                     'last_name': 'Last Name',
#                     'active': 'Active',
#                     'superuser': 'Superuser',
#                     'last_login': 'Last Login',
#                     'email': 'Email',
#                     'date_joined': 'Date Joined',
#                     'is_staff': 'Is Staff',
#                     # Add more mappings as needed
#                 }
#
#                 # user_data = {
#                 #     'User': user.username,
#                 #     'full_name': full_name,
#                 #     'user_fields': {field: getattr(user, field, "") for field in selected_user_fields if field != 'full_name'},
#                 #     'profile_fields': {field: getattr(user_profile, field, "") if user_profile else "" for field in
#                 #                        selected_profile_fields}
#                 # }
#
#                 user_data = {
#                     'User': user.username,
#                     'full_name': full_name,
#                     'user_fields': {field_display_names.get(field, field): getattr(user, field, "") for field in
#                                     selected_user_fields if field != 'full_name'},
#                     'profile_fields': {
#                         field_display_names.get(field, field): getattr(user_profile, field, "") if user_profile else ""
#                         for field in selected_profile_fields}
#                 }
#
#                 data.append(user_data)
#
#
#             template = get_template('user/pdf_template.html')
#             context = {
#                 'data': data,
#                 'selected_user_fields': selected_user_fields,
#                 'selected_profile_fields': selected_profile_fields,
#                 'field_display_names': field_display_names,  # Pass the display names to the template
#
#             }
#
#
#
#             #context = {'data': data, 'selected_user_fields': selected_user_fields, 'selected_profile_fields': selected_profile_fields}
#             html = template.render(context)
#
#             result = BytesIO()
#             pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result, encoding="ISO-8859-1")
#             if not pdf.err:
#                 response = HttpResponse(result.getvalue(), content_type='application/pdf')
#                 response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
#                 return response
#     else:
#         form = PDFGenerationForm()
#
#     return render(request, 'user/edit_pdf.html', {'form': form})


#
# def emp_pdf(request):
#     if request.method == 'POST':
#         form = PDFGenerationForm(request.POST)
#         if form.is_valid():
#             selected_user_fields = form.cleaned_data['user_fields']
#             selected_profile_fields = form.cleaned_data['profile_fields']
#
#             users = User.objects.all()  # Fetch all User instances
#
#             # Define custom field names
#             field_display_names = {
#                 'first_name': 'First Name',
#                 'last_name': 'Last Name',
#                 'username': 'Username',
#                 'is_active': 'Active',
#                 'is_superuser': 'Superuser',
#                 'last_login': 'Last Login',
#                 'email': 'Email',
#                 'date_joined': 'Date Joined',
#                 'is_staff': 'Staff',
#                 'id': 'Emp ID',
#                 # Add more mappings as needed
#             }
#
#             custom_user_fields = [field_display_names.get(field, field) for field in selected_user_fields]
#             custom_profile_fields = [field_display_names.get(field, field) for field in selected_profile_fields]
#
#             data = []
#             for user in users:
#                 user_profile = user.profile if hasattr(user, 'profile') else None
#                 full_name = f"{user.first_name} {user.last_name}"
#                 user_data = {
#                     'User': user.username,
#                     'full_name': full_name,
#                     'user_fields': {field: getattr(user, field, "") for field in selected_user_fields if field != 'full_name'},
#                     'profile_fields': {field: getattr(user_profile, field, "") if user_profile else "" for field in selected_profile_fields}
#                 }
#                 data.append(user_data)
#
#             template = get_template('user/pdf_template.html')
#             # context = {
#             #     'data': data,
#             #     'selected_user_fields': custom_user_fields,
#             #     'selected_profile_fields': custom_profile_fields,
#             # }
#
#             context = {
#                 'data': data,
#                 'selected_user_fields': selected_user_fields,
#                 'selected_profile_fields': selected_profile_fields,
#                 'custom_user_fields': custom_user_fields,
#                 'custom_profile_fields': custom_profile_fields,
#             }
#
#             html = template.render(context)
#
#             result = BytesIO()
#             pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result, encoding="ISO-8859-1")
#             if not pdf.err:
#                 response = HttpResponse(result.getvalue(), content_type='application/pdf')
#                 response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
#                 return response
#     else:
#         form = PDFGenerationForm()
#
#     return render(request, 'user/edit_pdf.html', {'form': form})


# def emp_pdf(request):
#     if request.method == 'POST':
#         form = PDFGenerationForm(request.POST)
#         if form.is_valid():
#             selected_user_fields = form.cleaned_data['user_fields']
#             selected_profile_fields = form.cleaned_data['profile_fields']
#
#             users = User.objects.all()  # Fetch all User instances
#
#
#             # Define custom field names
#             field_display_names = {
#                 'first_name': 'First Name',
#                 'last_name': 'Last Name',
#                 'active': 'Active',
#                 'superuser': 'Superuser',
#                 'last_login': 'Last Login',
#                 'email': 'Email',
#                 'username': 'Username',
#                 'date_joined': 'Date Joined',
#                 'is_staff': 'Is Staff',
#                 'id': 'Emp ID',
#                 # Add more mappings as needed
#             }
#
#             custom_user_fields = [field_display_names.get(field, field) for field in selected_user_fields]
#             custom_profile_fields = [field_display_names.get(field, field) for field in selected_profile_fields]
#
#             data = []
#             for user in users:
#                 user_profile = user.profile if hasattr(user, 'profile') else None
#                 full_name = f"{user.first_name} {user.last_name}"
#                 user_data = {
#                     'empid': user_profile.customer_id,
#                     'full_name': full_name,
#                     'user_fields': {field: getattr(user, field, "") for field in selected_user_fields if field != 'full_name'},
#                     'profile_fields': {field: getattr(user_profile, field, "") if user_profile else "" for field in selected_profile_fields}
#                 }
#                 data.append(user_data)
#
#             template = get_template('user/pdf_template.html')
#             context = {
#                 'data': data,
#                 'selected_user_fields': custom_user_fields,
#                 'selected_profile_fields': custom_profile_fields,
#                 'profile_fields': custom_profile_fields,  # Pass the profile_fields variable
#             }
#             html = template.render(context)
#
#             result = BytesIO()
#             pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result, encoding="ISO-8859-1")
#             if not pdf.err:
#                 response = HttpResponse(result.getvalue(), content_type='application/pdf')
#                 response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
#                 return response
#     else:
#         form = PDFGenerationForm()
#
#     return render(request, 'user/edit_pdf.html', {'form': form})
#


from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import render
from .forms import PDFGenerationForm
from .models import User
from django.db.models import Q
#
# def emp_pdf(request):
#     users = User.objects.all()
#     if request.method == 'POST':
#         form = PDFGenerationForm(request.POST)
#         if form.is_valid():
#             user_type_filter = request.POST.get('userType')
#
#             # Define the base queryset
#             base_queryset = User.objects.all()
#
#             # Apply filters based on the selected user type
#             if user_type_filter == 'superuser':
#                 base_queryset = base_queryset.filter(Q(is_superuser=True) & Q(is_staff=True) & Q(is_active=True))
#             elif user_type_filter == 'staff':
#                 base_queryset = base_queryset.filter(Q(is_superuser=False) & Q(is_staff=True) & Q(is_active=True))
#             elif user_type_filter == 'active':
#                 base_queryset = base_queryset.filter(Q(is_superuser=False) & Q(is_staff=False) & Q(is_active=True))
#
#             selected_user_fields = form.cleaned_data['user_fields']
#             selected_profile_fields = form.cleaned_data['profile_fields']
#
#             # Check if at least one field from either User or Profile is selected
#             if not (selected_user_fields or selected_profile_fields):
#                 return HttpResponse("Please select at least one field from User or Profile to generate the PDF.")
#
#             # Fetch the filtered users based on the selected user type
#             users = base_queryset  # Correct the indentation here
#
#             # Define custom field names
#             field_display_names = {
#                 'first_name': 'First Name',
#                 'last_name': 'Last Name',
#                 'active': 'Active',
#                 'superuser': 'Superuser',
#                 'last_login': 'Last Login',
#                 'email': 'Email',
#                 'username': 'Username',
#                 'date_joined': 'Date Joined',
#                 'is_staff': 'Is Staff',
#                 'id': 'Emp ID',
#                 # Add more mappings as needed
#             }
#
#             custom_user_fields = [field_display_names.get(field, field) for field in selected_user_fields]
#             custom_profile_fields = [field_display_names.get(field, field) for field in selected_profile_fields]
#
#             data = []
#             for user in users:
#                 user_profile = user.profile if hasattr(user, 'profile') else None
#                 full_name = f"{user.first_name} {user.last_name}"
#                 user_data = {
#                     'empid': user_profile.customer_id,
#                     'full_name': full_name,
#                     'user_fields': {field: getattr(user, field, "") for field in selected_user_fields if field != 'full_name'},
#                     'profile_fields': {field: getattr(user_profile, field, "") if user_profile else "" for field in selected_profile_fields}
#                 }
#                 data.append(user_data)
#
#             template = get_template('user/pdf_template.html')
#             context = {
#                 'data': data,
#                 'selected_user_fields': custom_user_fields,
#                 'selected_profile_fields': custom_profile_fields,
#                 'profile_fields': custom_profile_fields,  # Pass the profile_fields variable
#                 'base_queryset': base_queryset,
#             }
#             html = template.render(context)
#
#             result = BytesIO()
#             pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result, encoding="ISO-8859-1")
#             if not pdf.err:
#                 response = HttpResponse(result.getvalue(), content_type='application/pdf')
#                 response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
#                 return response
#     else:
#         form = PDFGenerationForm()
#
#     return render(request, 'user/edit_pdf.html', {'form': form})




from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO
from django.db.models import Q


# def generate_pdf(request, user_fields, profile_fields, data):
#     buffer = BytesIO()
#     pdf = SimpleDocTemplate(buffer, pagesize=letter)
#
#     # Create the table and apply column widths
#     table_data = [user_fields + profile_fields]  # Header row
#
#     for data_row in data:
#         table_data.append(data_row)
#
#     table = Table(table_data, colWidths=[100] * len(user_fields + profile_fields))  # Adjust column widths
#
#     # Apply styles to the table, e.g., borders
#     style = TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
#                         ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0))])
#     table.setStyle(style)
#
#     elements = [table]
#
#     pdf.build(elements)
#
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
#     response.write(buffer.getvalue())
#     buffer.close()
#
#     return response

# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# from django.http import HttpResponse
# from io import BytesIO
#
# def generate_pdf(request, user_fields, profile_fields, data):
#     buffer = BytesIO()
#     pdf = SimpleDocTemplate(buffer, pagesize=letter)
#
#     # Create the table and apply column widths
#     table_data = [user_fields + profile_fields]  # Header row
#
#     for user_data in data:
#         # Extract cell values from the user_data dictionary
#         row = []
#         for field in user_fields + profile_fields:
#             row.append(user_data.get(field, ""))  # Use get() to handle missing fields gracefully
#         table_data.append(row)
#
#     table = Table(table_data, colWidths=[100] * len(user_fields + profile_fields))  # Adjust column widths
#
#     # Apply styles to the table, e.g., borders
#     style = TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
#                         ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0))])
#     table.setStyle(style)
#
#     elements = [table]
#
#     pdf.build(elements)
#
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
#     response.write(buffer.getvalue())
#     buffer.close()
#
#     return response


from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.http import HttpResponse
from io import BytesIO

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.http import HttpResponse
from io import BytesIO

from io import BytesIO
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter
from django.db.models import Q
from .models import User  # Import your User model here

from io import BytesIO
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter
from django.db.models import Q
from .models import User  # Import your User model here

# def generate_pdf(request, user_fields, profile_fields, data):
#     buffer = BytesIO()
#     pdf = SimpleDocTemplate(buffer, pagesize=letter)
#
#     # Create the table and apply column widths
#     table_data = [['Sr No'] + ['Emp ID'] + user_fields + profile_fields]  # Add 'ID' to the header row
#
#     for index, user_data in enumerate(data, start=1):
#         row = [index, user_data['user_fields'].get('ID')]  # Access 'customer_id' from profile_fields
#         #print(f'Row {index} - ID: {row[1]}')
#         for field in user_fields:
#             if field != 'ID':
#                 row.append(user_data['user_fields'].get(field, ""))
#
#         for field in profile_fields:
#             if field != 'customer_id':
#                 row.append(user_data['profile_fields'].get(field, ""))
#
#         table_data.append(row)
#
#     table = Table(table_data, colWidths=[50, 50, 100] + [100] * (len(user_fields + profile_fields)))  # Adjust column widths
#
#
#
#     # col_widths = [50, 50, 100] + [
#     #     max(50, min(max_col_widths[col] * 10, 200)) if col not in ['username', 'workphone'] else 50 for col in
#     #     user_fields + profile_fields]
#     #
#     # table = Table(table_data, colWidths=col_widths)
#
#
#
#     # Apply styles to the table, e.g., borders
#     style = TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
#                         ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0))])
#     table.setStyle(style)
#
#     elements = [table]
#
#     pdf.build(elements)
#
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
#     response.write(buffer.getvalue())
#     buffer.close()
#
#     return response

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.http import HttpResponse
from io import BytesIO

# def generate_pdf(request, user_fields, profile_fields, data):
#     buffer = BytesIO()
#     #pdf = SimpleDocTemplate(buffer, pagesize=letter)
#     pdf = SimpleDocTemplate(buffer, pagesize=landscape(letter))
#     # Create the table and apply column widths
#     table_data = [['Sr No', 'Emp ID'] + user_fields + profile_fields]  # Add 'ID' to the header row
#
#     for index, user_data in enumerate(data, start=1):
#         row = [index, user_data['user_fields'].get('ID')]  # Access 'customer_id' from profile_fields
#
#         row.extend([user_data['user_fields'].get(field, "") for field in user_fields if field != 'ID'])
#         row.extend([user_data['profile_fields'].get(field, "") for field in profile_fields if field != 'customer_id'])
#         table_data.append(row)
#
#     table = Table(table_data)
#
#     # Apply styles to the table, e.g., borders
#     style = TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
#                         ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0))])
#     table.setStyle(style)
#
#     elements = [table]
#
#     pdf.build(elements)
#
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
#     response.write(buffer.getvalue())
#     buffer.close()
#
#     return response

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageTemplate, Frame, Image
from reportlab.lib import units
from django.http import HttpResponse
from io import BytesIO

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageTemplate, Frame, Image
from reportlab.lib import units
from django.http import HttpResponse
from io import BytesIO

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageTemplate, PageBreak, Image
from reportlab.lib import units
from django.http import HttpResponse
from io import BytesIO

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageTemplate, PageBreak, Frame, Image
from reportlab.lib import units
from django.http import HttpResponse
from io import BytesIO

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageTemplate, PageBreak, Image, Frame
from reportlab.lib import units
from django.http import HttpResponse
from io import BytesIO

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageTemplate, PageBreak, Image, Frame
from reportlab.lib import units
from django.http import HttpResponse
from io import BytesIO


from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageTemplate, Frame, Flowable, Spacer
from reportlab.lib import colors
from reportlab.platypus import Image
from django.http import HttpResponse
from io import BytesIO

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib import colors
from reportlab.platypus import Image
from django.http import HttpResponse
from io import BytesIO

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib import colors
from reportlab.platypus import Image, PageBreak
from django.http import HttpResponse
from io import BytesIO
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# ======================================================================================================
# def generate_pdf(request, user_fields, profile_fields, data, logo_path, top_margin_height=0, user_type_filter=""):
#     buffer = BytesIO()
#     pdf = SimpleDocTemplate(buffer, pagesize=letter, topMargin=top_margin_height * inch)
#
#     elements = []
#
#     # Add the company logo at the top of the first page only
#     logo = Image(logo_path, width=6.5 * inch, height=1.0 * inch)
#     logo.hAlign = 'CENTER'
#     elements.append(logo)
#
#     # Create table data for all user data
#     table_data = [['Sr No', 'Emp ID'] + user_fields + profile_fields]
#
#     for index, user_data in enumerate(data, start=1):
#         row = [index, user_data['user_fields'].get('ID')]
#
#         row.extend([user_data['user_fields'].get(field, "") for field in user_fields if field != 'ID'])
#         row.extend([user_data['profile_fields'].get(field, "") for field in profile_fields if field != 'customer_id'])
#         table_data.append(row)
#
#     table = Table(table_data)
#     style = TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#                         ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
#                         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Make the first row bold
#                         ('ALIGN', (0, 0), (-1, 0), 'CENTER'),  # Center-align the first row
#                         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Add a background color to the first row
#                         ('ALIGN', (0, 1), (1, -1), 'CENTER'),  # Center-align the Sr No and Emp ID columns
#                         ])
#     table.setStyle(style)
#
#     # Create a custom style for the caption
#     caption_style = ParagraphStyle(
#         name='CaptionStyle',
#         fontSize=14,  # Adjust the font size as needed
#         fontName='Helvetica-Bold',  # Use a bold font
#         spaceAfter=12,  # Add space after the caption
#         alignment =1,
#     )
#
#     # Determine the caption text based on the selected_option
#     if user_type_filter == "all":
#         caption_text = "List Type : All Employee List"
#     elif user_type_filter == "superuser":
#         caption_text = "List Type : Admin List"
#     elif user_type_filter == "staff":
#         caption_text = "List Type : Staff List"
#     elif user_type_filter == "active":
#         caption_text = "List Type : Consumer List"
#     else:
#         caption_text = "Unknown List"  # Add a default caption for unknown options
#
#     caption = Paragraph(caption_text, caption_style)
#
#     elements.append(Spacer(1, 0.25 * inch))  # Add space between logo and table
#     elements.append(caption)
#     elements.append(table)
#
#     pdf.build(elements)
#
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
#     response.write(buffer.getvalue())
#     buffer.close()
#
#     return response
#=====================================================================


from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Image, Table, TableStyle, Spacer, Paragraph
from datetime import datetime

@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])

def generate_pdf(request, user_fields, profile_fields, data, logo_path, top_margin_height=0.25, user_type_filter=""):
    buffer = BytesIO()

    # Determine the page size based on the number of fields
    if len(user_fields) + len(profile_fields) > 4:
        page_size = landscape(letter)
    else:
        page_size = portrait(letter)

    # pdf = SimpleDocTemplate(buffer, pagesize=page_size, topMargin=top_margin_height * inch)

    # Define top and bottom margins
    top_margin_height = 0.25  # Top margin in inches
    bottom_margin_height = 0.25  # Bottom margin in inches
    page_height = page_size[1]  # Get the page height
    remaining_height = page_height - (top_margin_height + bottom_margin_height)

    pdf = SimpleDocTemplate(buffer, pagesize=page_size, topMargin=top_margin_height * inch, bottomMargin=bottom_margin_height * inch )

    elements = []

    # Create a custom style for the caption
    caption_style = ParagraphStyle(
        name='CaptionStyle',
        fontSize=14,  # Adjust the font size as needed
        fontName='Helvetica-Bold',  # Use a bold font
        spaceAfter=12,  # Add space after the caption
        alignment=1,  # Center-align the caption text
    )

    # Determine the caption text based on the selected_option
    if user_type_filter == "all":
        caption_text = "List Type: All Employee List"
    elif user_type_filter == "superuser":
        caption_text = "List Type: Admin List"
    elif user_type_filter == "staff":
        caption_text = "List Type: Staff List"
    elif user_type_filter == "active":
        caption_text = "List Type: Consumer List"
    else:
        caption_text = "Unknown List"  # Add a default caption for unknown options

    caption = Paragraph(caption_text, caption_style)

    # Create table data for all user data
    table_data = [['Sr No', 'Emp ID'] + user_fields + profile_fields]

    for index, user_data in enumerate(data, start=1):
        row = [index, user_data['user_fields'].get('ID')]

        row.extend([user_data['user_fields'].get(field, "") for field in user_fields if field != 'ID'])
        row.extend([user_data['profile_fields'].get(field, "") for field in profile_fields if field != 'customer_id'])
        table_data.append(row)

    table = Table(table_data)
    style = TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Make the first row bold
                        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),  # Center-align the first row
                        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Add a background color to the first row
                        ('ALIGN', (0, 1), (1, -1), 'CENTER'),  # Center-align the Sr No and Emp ID columns
                        ])
    table.setStyle(style)

    # Add the company logo at the top of the page
    logo = Image(logo_path, width=5.5 * inch, height=0.70 * inch)
    logo.hAlign = 'CENTER'

    # Create a Spacer for spacing between elements
    spacer = Spacer(1, 0.25 * inch)

    # Create a Paragraph for the current date
    current_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    current_date_style = ParagraphStyle(
        name='CurrentDateStyle',
        fontSize=10,
        fontName='Helvetica',
        alignment=1,  # Center-align the current date
    )
    current_date_paragraph = Paragraph(current_date, current_date_style)

    # Add elements to the content
    elements.extend([logo, caption, current_date_paragraph, spacer, table])

    pdf.build(elements)

    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
    response['Content-Disposition'] = f'attachment; filename ={user_type_filter}_pdf.pdf'
    response.write(buffer.getvalue())
    buffer.close()

    return response


#
# def emp_pdf(request):
#     if request.method == 'POST':
#         form = PDFGenerationForm(request.POST)
#         if form.is_valid():
#             user_type_filter = request.POST.get('userType')
#
#             # Define the base queryset
#             base_queryset = User.objects.all()
#
#             # Apply filters based on the selected user type
#             if user_type_filter == 'superuser':
#                 base_queryset = base_queryset.filter(Q(is_superuser=True) & Q(is_staff=True) & Q(is_active=True))
#             elif user_type_filter == 'staff':
#                 base_queryset = base_queryset.filter(Q(is_superuser=False) & Q(is_staff=True) & Q(is_active=True))
#             elif user_type_filter == 'active':
#                 base_queryset = base_queryset.filter(Q(is_superuser=False) & Q(is_staff=False) & Q(is_active=True))
#
#             selected_user_fields = form.cleaned_data['user_fields']
#             selected_profile_fields = form.cleaned_data['profile_fields']
#
#             # Check if at least one field from either User or Profile is selected
#             if not (selected_user_fields or selected_profile_fields):
#                 return HttpResponse("Please select at least one field from User or Profile to generate the PDF.")
#
#             # Fetch the filtered users based on the selected user type
#             users = base_queryset  # Correct the indentation here
#
#             # Define custom field names
#             field_display_names = {
#                 'first_name': 'First Name',
#                 'last_name': 'Last Name',
#                 'active': 'Active',
#                 'superuser': 'Superuser',
#                 'last_login': 'Last Login',
#                 'email': 'Email',
#                 'username': 'Username',
#                 'date_joined': 'Date Joined',
#                 'is_staff': 'Is Staff',
#                 'id': 'ID',
#                 # Add more mappings as needed
#             }
#
#
#             custom_user_fields = [field_display_names.get(field, field) for field in selected_user_fields]
#             custom_profile_fields = [field_display_names.get(field, field) for field in selected_profile_fields]
#
#             data = []
#             for user in users:
#                 user_profile = user.profile if hasattr(user, 'profile') else None
#                 full_name = f"{user.first_name} {user.last_name}"
#                 user_data = {
#                     'user_fields': {
#                         field_display_names.get(field, field):
#
#                             getattr(user, field, "") if field not in ['full_name', 'id'] else
#                             user.id if field == 'id' else
#                             full_name if field == 'full_name' else ""
#
#                         for field in selected_user_fields
#                     },
#                     'profile_fields': {
#                         field_display_names.get(field, field):
#                             getattr(user_profile, field, "") if user_profile else ""
#                         for field in selected_profile_fields
#                     }
#                 }
#                 data.append(user_data)
#
#             # Call the PDF generation function with the data
#             return generate_pdf(request, custom_user_fields, custom_profile_fields, data)
#     else:
#         form = PDFGenerationForm()
#
#     return render(request, 'user/edit_pdf.html', {'form': form})


@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
def emp_pdf(request):
    if request.method == 'POST':
        form = PDFGenerationForm(request.POST)
        if form.is_valid():
            user_type_filter = request.POST.get('userType')

            # Define the base queryset
            base_queryset = User.objects.all()

            # Apply filters based on the selected user type
            if user_type_filter == 'superuser':
                base_queryset = base_queryset.filter(Q(is_superuser=True) & Q(is_staff=True) & Q(is_active=True))
            elif user_type_filter == 'staff':
                base_queryset = base_queryset.filter(Q(is_superuser=False) & Q(is_staff=True) & Q(is_active=True))
            elif user_type_filter == 'active':
                base_queryset = base_queryset.filter(Q(is_superuser=False) & Q(is_staff=False) & Q(is_active=True))
            elif user_type_filter == 'all':
               # base_queryset = base_queryset.filter((Q(is_superuser=True) & Q(is_staff=True) & Q(is_active=True))&(Q(is_superuser=False) & Q(is_staff=True) & Q(is_active=True)))
               base_queryset = base_queryset.filter(Q(Q(is_superuser=True) & Q(is_active=True)) | Q(Q(is_staff=True) & Q(is_active=True)))

            selected_user_fields = form.cleaned_data['user_fields']
            selected_profile_fields = form.cleaned_data['profile_fields']

            # Check if at least one field from either User or Profile is selected
            if not (selected_user_fields or selected_profile_fields):
                return HttpResponse("Please select at least one field from User or Profile to generate the PDF.")

            # Fetch the filtered users based on the selected user type
            users = base_queryset

            # Define custom field names
            field_display_names = {
                'email': 'Email',
                'username': 'Username',
                'id': 'ID',  # Map 'id' field to 'ID'
                'workphone': 'Contact No',
                'bg': 'Blood Group',
                'DOB': 'Date of Birth',
                'designation': 'Designation',
                'department': 'Department',
                'address': 'Address',
                'city': 'City',
                'taluka': 'Taluka',
                'district': 'District',
                # Add more mappings as needed
            }

            custom_user_fields = ['Full Name'] if 'full_name' in selected_user_fields else []

            for field in selected_user_fields:
                if field in field_display_names and field != 'full_name':
                    custom_user_fields.append(field_display_names[field])

            custom_profile_fields = [field_display_names.get(field, field) for field in selected_profile_fields]

            data = []
            for user in users:
                user_profile = user.profile if hasattr(user, 'profile') else None
                #print(f'User ID: {user.id}, Customer ID: {user_profile.customer_id if user_profile else "N/A"}')

                #user_profile = user.profile if hasattr(user, 'profile') else None
                full_name = f"{user.first_name} {user.last_name}" if 'full_name' in selected_user_fields else ""
                user_fields_data = {
                    'ID': user_profile.customer_id if user_profile else '',  # Access 'customer_id' from profile
                    'Full Name': full_name,
                }
                user_fields_data.update({field_display_names.get(field, field): getattr(user, field, "") for field in selected_user_fields if field != 'full_name'})
                profile_fields_data = {field_display_names.get(field, field): getattr(user_profile, field, "") for field in selected_profile_fields} if user_profile else {}
                user_data = {
                    'user_fields': user_fields_data,
                    'profile_fields': profile_fields_data,
                }
                data.append(user_data)
            logo_path = "media/static/images/dblogo2001.png"  # Replace with the actual path to your logo image
            top_margin_height = 0.25  # Adjust this value as needed

            # Call the PDF generation function with the data
            return generate_pdf(request, custom_user_fields, custom_profile_fields, data, logo_path, top_margin_height, user_type_filter)
    else:
        form = PDFGenerationForm()

    return render(request, 'user/edit_pdf.html', {'form': form})



# def emp_pdf(request):
#     if request.method == 'POST':
#         form = PDFGenerationForm(request.POST)
#         if form.is_valid():
#             user_type_filter = request.POST.get('userType')
#
#             # Define the base queryset
#             base_queryset = User.objects.all()
#
#             # Apply filters based on the selected user type
#             if user_type_filter == 'superuser':
#                 base_queryset = base_queryset.filter(Q(is_superuser=True) & Q(is_staff=True) & Q(is_active=True))
#             elif user_type_filter == 'staff':
#                 base_queryset = base_queryset.filter(Q(is_superuser=False) & Q(is_staff=True) & Q(is_active=True))
#             elif user_type_filter == 'active':
#                 base_queryset = base_queryset.filter(Q(is_superuser=False) & Q(is_staff=False) & Q(is_active=True))
#
#             selected_user_fields = form.cleaned_data['user_fields']
#             selected_profile_fields = form.cleaned_data['profile_fields']
#
#             # Check if at least one field from either User or Profile is selected
#             if not (selected_user_fields or selected_profile_fields):
#                 return HttpResponse("Please select at least one field from User or Profile to generate the PDF.")
#
#             # Fetch the filtered users based on the selected user type
#             users = base_queryset
#
#             # Define custom field names
#             field_display_names = {
#                 'first_name': 'First Name',
#                 'last_name': 'Last Name',
#                 'active': 'Active',
#                 'superuser': 'Superuser',
#                 'last_login': 'Last Login',
#                 'email': 'Email',
#                 'username': 'Username',
#                 'date_joined': 'Date Joined',
#                 'is_staff': 'Is Staff',
#                 'id': 'ID',  # Map 'id' field to 'ID'
#                 # Add more mappings as needed
#             }
#
#             custom_user_fields = []
#             custom_profile_fields = [field_display_names.get(field, field) for field in selected_profile_fields]
#
#             for field in selected_user_fields:
#                 if field in field_display_names:
#                     custom_user_fields.append(field_display_names[field])
#
#             data = []
#             for user in users:
#                 user_profile = user.profile if hasattr(user, 'profile') else None
#                 full_name = f"{user.first_name} {user.last_name}"
#                 user_fields_data = {
#                     'ID': user.id,
#                     'Full Name': full_name if 'full_name' in selected_user_fields else "",
#                 }
#                 user_fields_data.update({field_display_names.get(field, field): getattr(user, field, "") for field in selected_user_fields if field != 'id'})
#                 profile_fields_data = {field_display_names.get(field, field): getattr(user_profile, field, "") for field in selected_profile_fields} if user_profile else {}
#                 user_data = {
#                     'user_fields': user_fields_data,
#                     'profile_fields': profile_fields_data,
#                 }
#                 data.append(user_data)
#
#             # Call the PDF generation function with the data
#             return generate_pdf(request, custom_user_fields, custom_profile_fields, data)
#     else:
#         form = PDFGenerationForm()
#
#     return render(request, 'user/edit_pdf.html', {'form': form})



def register(request):
    count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
    notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        #Profile.objects.create(user=form)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.is_active = True
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}  continue to Login')
            group = Group.objects.get(name='Customers')
            user.groups.add(group)
            return redirect('user-login')
    else:
        form = CreateUserForm()
        #Profile.objects.create(user=form)
    context = {
        'form': form,
        'profile': profile,
        'count1': count1,
        'notification1': notification1,
    }
    return render(request, 'user/register.html', context)

@login_required(login_url='user-login')
def add(request):
    error=""
    count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
    notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
    #    Profile.objects.create(user=form)

        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(request.POST.get('password1'))

            user.is_staff = True
            user.is_active = True
            user.save()
           # print(user.first_name)
            # Add the user to the Customers group
            group = Group.objects.get(name='Customers')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}  Account Created Successfully!!')
            #print(user.password)
            return redirect('user-profile-update', user.id)
    else:
        form = CreateUserForm()
#        Profile.objects.create(user=form)
    context = {
        'form': form,
        'profile': profile,
        'count1': count1,
        'notification1': notification1,
    }
    return render(request, 'user/add.html', context)


# def profile(request,pk):
#     user = User.objects.get(id=pk)
#     item = Profile.objects.get(id=pk)
#     return render(request, 'user/profile.html', locals())

# def profile(request):
#     error = ""
#     count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
#     notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
#     user = request.user
#     employee = Profile.objects.get(customer=user)
#     customer = Customer.objects.get(new_customer=user)
#     if request.method == "POST":
#       o = request.POST['oldpassword']
#       n = request.POST['newpassword']
#     try:
#         u = User.objects.get(id=request.user.id)
#         if user.check_password(o):
#             u.set_password(n)
#             u.save()
#             error = "no"
#         else:
#             error = 'not'
#     except:
#         error = "yes"
#     return render(request, 'user/profile.html', locals())

def profile(request):
    error = ""
    count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
    notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
    user = request.user
    employee = Profile.objects.get(customer=user)

    # Check if the current user is a customer and retrieve their associated object
    try:
        customer = Customer.objects.get(new_customer=user)
    except Customer.DoesNotExist:
        customer = None

    if request.method == "POST":
        old_password = request.POST['oldpassword']
        new_password = request.POST['newpassword']

        # Change the user's password if the old password is correct
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(old_password):
                u.set_password(new_password)
                u.save()
                error = "no"
            else:
                error = 'not'
        except User.DoesNotExist:
            error = "yes"

    return render(request, 'user/profile.html', locals())



def edit_profile(request):
    error = ""
    count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
    notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
    user = request.user
    employee = Profile.objects.get(customer=user)
    bgs = Profile._meta.get_field('bg').choices

    # Check if the current user is a customer and retrieve their associated object

    try:
        customer = Customer.objects.get(new_customer=user)
    except Customer.DoesNotExist:
        customer = None

    if request.method == "POST":
        em = request.POST.get('email')
        add = request.POST.get('address')
        dob = request.POST.get('DOB')
        ph = request.POST.get('ph')
        bg = request.POST.get('bg')
        city = request.POST.get('city')
        taluka = request.POST.get('taluka')
        district = request.POST.get('district')
        add1 = request.POST.get('address1')
        ph1 = request.POST.get('ph1')
        city1 = request.POST.get('city1')
        state1 = request.POST.get('state1')
        pincode1 = request.POST.get('pincode1')
        image = request.FILES.get('image')

        if image:
            employee.image = image
        if em:
          user.email = em
        if ph:
         employee.workphone = ph
        #employee.bg = bg
        if add:
         employee.address = add
        if city:
         employee.city = city
        if taluka:
         employee.taluka = taluka
        if district:
         employee.district = district

        if dob:
            employee.DOB = dob
        if bg:
            employee.bg = bg

        if customer is not None:
            if ph1:
             customer.phone = ph1
            #employee.bg = bg
            if add1:
             customer.Address = add1
            if city1:
             customer.City = city1
            if state1:
             customer.state = state1
            if pincode1:
             customer.Pincode = pincode1

        try:
            employee.save()
            user.save()
            #customer.save()

            # print(employee.image, user.first_name, user.last_name, user.email,
            #       user.password, user.date_joined, employee.DOB, employee.department, employee.phone,
            #       employee.designation)
            # User.objects.create_user(first_name=fn,last_name=ln,username=un,password=pwd,id=ec,email=em,date_joined=jod)
            # Profile.objects.create(address=add,DOB=dob,department=dept,image=img,phone=ph)
            error="no"
        except:
            error="yes"
    return render(request, 'user/edit_profile.html', locals())


#     fn = request.POST['firstname']
    #     ln = request.POST['lastname']
    #
    #
    #     em = request.POST['email']
    #     pwd = request.POST['pwd']
    #     add = request.POST['address']
    #     dob = request.POST['DOB']
    #     jod = request.POST['jod']
    #     dept = request.POST['dept']
    #     image = request.FILES.get('image')
    #     ph = request.POST['ph']
    #     desig = request.POST['desig']
    #
    #     user.first_name = fn
    #     user.last_name = ln
    #     user.email = em
    #     user.password = pwd
    #     employee.department = dept
    #     employee.phone = ph
    #     employee.designation = desig
    #     if jod:
    #         user.date_joined = jod
    #
    #     if dob:
    #         employee.DOB = dob
    #     if image:
    #         employee.image = image
    #
    #     try:
    #         employee.save()
    #         user.save()
    #         print(employee.image, user.first_name, user.last_name, user.email,
    #               user.password, user.date_joined, employee.DOB, employee.department, employee.phone,
    #               employee.designation)
    #         # User.objects.create_user(first_name=fn,last_name=ln,username=un,password=pwd,id=ec,email=em,date_joined=jod)
    #         # Profile.objects.create(address=add,DOB=dob,department=dept,image=img,phone=ph)
    #         error="no"
    #     except:
    #         error="yes"
    # return render(request, 'user/profile.html', locals())



def profile_update(request,pk):
    error = ""
    count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
    notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
    departments = Profile._meta.get_field('department').choices
    designations = Profile._meta.get_field('designation').choices
    bgs = Profile._meta.get_field('bg').choices
    user1 = User.objects.get(id=pk)
    print(user1)
    employee = Profile.objects.get(customer_id=user1)
    print(user1)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        add = request.POST['address']
        dob = request.POST['DOB']
        jod = request.POST['jod']
        dept = request.POST.get('dept')
        image = request.FILES.get('image')
        ph = request.POST['ph']
        desig = request.POST.get('desig')

        bg = request.POST.get('bg')
        city = request.POST['city']
        taluka = request.POST['taluka']
        district = request.POST['district']
        pg = request.POST['pg']
        institution = request.POST['institution']
        yop = request.POST['yop']
        specili = request.POST['specili']
        name = request.POST['name']
        phone = request.POST['phone']
        emremail = request.POST['emremail']
        emraddress = request.POST['emraddress']


        user1.first_name = fn
        user1.last_name = ln
        user1.email = em

        #employee.department = dept
        employee.phone = phone
        #employee.designation = desig
        employee.address = add

        #employee.bg = bg
        employee.city = city
        employee.taluka = taluka
        employee.district = district
        employee.pg = pg
        employee.institution = institution
        employee.specili = specili
        employee.name = name
        employee.workphone = ph
        employee.email = emremail
        employee.emraddress = emraddress

        if dept:
            employee.department = dept
        if desig:
            employee.designation = desig
        if bg:
            employee.bg = bg
        if yop:
            employee.yop = yop

        if jod:
            user1.date_joined = jod

        if dob:
            employee.DOB = dob
        if image:
            employee.image = image

        try:
            user = get_user(request)
            employee.last_updated_by = user.id
            print(user)
            employee.save()
            user1.save()
            print(employee.image, user1.first_name, user1.last_name, user1.email,
                  user1.password, user1.date_joined, employee.DOB, employee.department, employee.phone,
                  employee.designation)
            logout(request)
            login(request, user)



            # User.objects.create_user(first_name=fn,last_name=ln,username=un,password=pwd,id=ec,email=em,date_joined=jod)
            # Profile.objects.create(address=add,DOB=dob,department=dept,image=img,phone=ph)
            error="no"
        except:
            error="yes"
    return render(request, 'user/profile_update.html', locals())


def profile_updatepage(request,pk):
    count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
    notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
    user1 = User.objects.get(id=pk)
    employee = Profile.objects.get(customer_id=pk)
    return render(request, 'user/profile_updatepage.html', locals())



# def profile_update(request,pk):
#     error=" "
#     item1 = User.objects.get(id=pk)
#     item = Profile.objects.get(id=pk)
#
#
#     if request.method == 'POST':
#
#         u_form = UserUpdateForm(request.POST, instance=item1)
#         p_form = ProfileUpdateForm(
#             request.POST, request.FILES, instance=item)
#
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             return redirect('user-profile', item.id)
#     else:
#         u_form = UserUpdateForm(instance=item1)
#         p_form = ProfileUpdateForm(instance=item)
#
#     context = {
#
#         'u_form': u_form,
#         'p_form': p_form,
#     }
#     return render(request, 'user/profile_update.html', context)



