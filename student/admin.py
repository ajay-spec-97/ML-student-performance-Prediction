from django.contrib import admin
from . import models


admin.site.register(models.User)


class StudentInformation(admin.ModelAdmin):

    fieldsets= (
        ("Student", {
            'fields': ('student',),},
        ),

        ("Parents' Education", {
            'fields': ('fathers_education',
                       'mothers_education',)}
        ),

        ("Parents' Occupation", {
            'fields': ('fathers_occupation',
                       'mothers_occupation',)}
        ),

        ("Family Income", {
            'fields': ('annual_family_income',)}
        ),

        ("Personal Information", {
            'fields': ('educational_loan',
                       'life_spent_in',),},
        ),

        ("Students' Education Details", {
            'fields': ('medium_of_instruction',
                       'marks_in_10th',
                       'marks_in_12th',
                       'marks_in_first_year',
                       'marks_in_second_year',
                       'marks_in_third_year',
                       'marks_in_graduation',
                       'gap_year',
                       'hours_spent_on_academic',
                       'type_of_graduation',
                      ),}
        ),

        ("Psychological Tends", {
            'fields': ('assertiveness',
                       'empathy',
                       'decision_making',
                       'leadership',
                       'drive',
                       'stress_management'
                      ),},
        ),
    )
admin.site.register(models.StudentInformation, StudentInformation)
