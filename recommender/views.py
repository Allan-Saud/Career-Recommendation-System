import joblib
import pandas as pd
from django.conf import settings
from django.shortcuts import render
from huggingface_hub import InferenceClient
from .forms import StudentForm

# Load ML assets once when the app starts
model = joblib.load('recommender/models/best_career_recommendation_model.pkl')
scaler = joblib.load('recommender/models/scaler.pkl')
label_encoder = joblib.load('recommender/models/label_encoder.pkl')
client = InferenceClient(token=settings.HF_TOKEN)

def recommend_career(student_data):
    input_df = pd.DataFrame([student_data])
    input_scaled = scaler.transform(input_df)
    career_code = model.predict(input_scaled)[0]
    return label_encoder.inverse_transform([career_code])[0]

def generate_description(career):
    try:
        response = client.text_generation(
            prompt=f"""<s>[INST] <<SYS>>
You are a career counselor providing clear, factual descriptions.
<</SYS>>

Describe a {career} career in 2-3 sentences. Highlight:
- Key characteristics
- Required skills
- Typical responsibilities [/INST]""",
            model="mistralai/Mistral-7B-Instruct-v0.2",
            max_new_tokens=100,
            temperature=0.7
        )
        return response.split("[/INST]")[-1].strip().replace("\n", " ")
    except Exception as e:
        return f"Description unavailable. Error: {str(e)}"

def career_recommendation_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student_data = {
                'part_time_job': form.cleaned_data['part_time_job'],
                'absence_days': form.cleaned_data['absence_days'],
                'extracurricular_activities': form.cleaned_data['extracurricular_activities'],
                'weekly_self_study_hours': form.cleaned_data['weekly_self_study_hours'],
                'math_score': form.cleaned_data['math_score'],
                'history_score': form.cleaned_data['history_score'],
                'physics_score': form.cleaned_data['physics_score'],
                'chemistry_score': form.cleaned_data['chemistry_score'],
                'biology_score': form.cleaned_data['biology_score'],
                'english_score': form.cleaned_data['english_score'],
                'geography_score': form.cleaned_data['geography_score'],
            }
            
            career = recommend_career(student_data)
            description = generate_description(career)
            
            return render(request, 'recommender/result.html', {
                'career': career,
                'description': description
            })
    else:
        form = StudentForm()
    
    return render(request, 'recommender/index.html', {'form': form})