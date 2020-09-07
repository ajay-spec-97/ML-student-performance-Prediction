from material import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

from . import models


class StudentInformationForm(forms.ModelForm):

    class Meta:
        model = models.StudentInformation
        fields = [
                  'fathers_education',
                  'fathers_occupation',
                  'mothers_education',
                  'mothers_occupation',
                  'annual_family_income',
                  'life_spent_in',
                  'educational_loan',
                  'medium_of_instruction',
                  'marks_in_10th',
                  'marks_in_12th',
                  'marks_in_first_year',
                  'marks_in_second_year',
                  'marks_in_third_year',
                  'type_of_graduation',
                  'gap_year',
                  'hours_spent_on_academic',
                  'assertiveness',
                  'empathy',
                  'decision_making',
                  'leadership',
                  'drive',
                  'stress_management']

    layout = Layout(
            Fieldset("Parents' Details",
                     Row('fathers_education',
                         'fathers_occupation'),
                     Row('mothers_education',
                         'mothers_occupation'),
            ),
            Fieldset("Other Information",
                     Row('annual_family_income',
                         "life_spent_in",
                         "educational_loan")),
            Fieldset("Education Details",
                     Row("medium_of_instruction",
                         "marks_in_10th",
                         "marks_in_12th"),
                     Row("gap_year",
                         "type_of_graduation",
                         "hours_spent_on_academic",),
                     Row("marks_in_first_year",
                         "marks_in_second_year",
                         "marks_in_third_year",
                         ),
            ),
            Fieldset("Psychological Tends",
                     Row("assertiveness",
                         "empathy",
                         "decision_making",),
                     Row("leadership",
                         "drive",
                         "stress_management"),
            ),
    )


class StudentSignUpForm(UserCreationForm):

    class Meta:
        model = models.User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'gender',
                  'current_year',
                  'interests',)
