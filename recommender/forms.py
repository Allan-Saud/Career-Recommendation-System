from django import forms

class StudentForm(forms.Form):
    part_time_job = forms.BooleanField(required=False, initial=False)
    absence_days = forms.IntegerField(min_value=0, max_value=365)
    extracurricular_activities = forms.BooleanField(required=False, initial=False)
    weekly_self_study_hours = forms.IntegerField(min_value=0, max_value=168)
    math_score = forms.IntegerField(min_value=0, max_value=100)
    history_score = forms.IntegerField(min_value=0, max_value=100)
    physics_score = forms.IntegerField(min_value=0, max_value=100)
    chemistry_score = forms.IntegerField(min_value=0, max_value=100)
    biology_score = forms.IntegerField(min_value=0, max_value=100)
    english_score = forms.IntegerField(min_value=0, max_value=100)
    geography_score = forms.IntegerField(min_value=0, max_value=100)