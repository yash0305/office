from django.contrib import admin
from .models import Client, Project

# class ProjectInline(admin.TabularInline):
#     """
#     Allows projects to be edited directly within the Client admin page.
#     """
#     model = Project
#     extra = 1  # Number of empty forms to display for new projects
#     fields = ['project_name', 'users', 'created_by', 'created_at']
#     readonly_fields = ['created_by', 'created_at']

# class ClientAdmin(admin.ModelAdmin):
#     """
#     Customizes the admin interface for the Client model.
#     """
#     list_display = ['client_name', 'created_by', 'created_at', 'updated_at']
#     search_fields = ['client_name', 'created_by__username']
#     list_filter = ['created_at', 'created_by']
#     readonly_fields = ['created_by', 'created_at', 'updated_at']
#     inlines = [ProjectInline]

#     def save_model(self, request, obj, form, change):
#         """
#         Sets the created_by field to the current user when a new Client is created.
#         """
#         if not obj.pk:  # Only set created_by during the first save (creation)
#             obj.created_by = request.user
#         super().save_model(request, obj, form, change)

# class ProjectAdmin(admin.ModelAdmin):
#     """
#     Customizes the admin interface for the Project model.
#     """
#     list_display = ['project_name', 'client', 'created_by', 'created_at']
#     search_fields = ['project_name', 'client__client_name', 'created_by__username']
#     list_filter = ['created_at', 'client', 'created_by']
#     filter_horizontal = ['users']  # Provides a better UI for ManyToMany fields
#     readonly_fields = ['created_by', 'created_at']

#     def save_model(self, request, obj, form, change):
#         """
#         Sets the created_by field to the current user when a new Project is created.
#         """
#         if not obj.pk:  # Only set created_by during the first save (creation)
#             obj.created_by = request.user
#         super().save_model(request, obj, form, change)

# Register the models with the custom admin classes
admin.site.register(Client)
admin.site.register(Project)
