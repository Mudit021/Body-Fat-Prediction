import numpy as np
import pandas as pd
import joblib 

model = joblib.load("bodyfat_linear_model.pkl")
scaler = joblib.load("scaler.pkl")

def classify_bodyfat(bf,gender):
    if gender == 1: #male
        if bf <14:
            return "Lean"
        elif bf <20:
            return "Healthy"
        elif bf <25:
            return "Overweight"
        else:
            return "Obese"
    else : #female
        if bf<20:
            return "Lean"
        elif bf < 28:
            return "Healthy"
        elif bf <35:
            return "Average"
        elif bf < 40:
            return "Overweight"
        else:
            return "Obese"
        
def generate_recommendation(pred_bf, weight, gender):
    min_bf = 12 if gender == 1 else 20
    target_bf = max(pred_bf - 4, min_bf)
    bf_to_lose = pred_bf - target_bf
    months = bf_to_lose / 0.7 if bf_to_lose > 0 else 0

    category = classify_bodyfat(pred_bf, gender)

    print("\n----- RESULTS -----")
    print(f"Predicted Body Fat: {round(pred_bf,1)}%")
    print(f"Category: {category}")
    print(f"Safe Target: {round(target_bf,1)}%")
    print(f"Estimated Duration: {round(months,1)} months")
    print("Recommended Daily Calorie Deficit: ~400 kcal")
    print("\nFocus Areas:")
    
    if category in ["Overfat", "Obese"]:
        print("- Walk 8k–10k steps daily")
        print("- Strength training 3x/week")
        print("- Protein ≈1.6 g/kg body weight")
        print("- Reduce sugary drinks")
    else:
        print("- Maintain strength training")
        print("- Balanced nutrition")
        print("- Consistent sleep")

    print("\n Educational tool only. Not medical advice.")


print("Enter your details:")

age = int(input("Age: "))
gender = int(input("Gender (1=Male, 0=Female): "))
height = float(input("Height (cm): "))
weight = float(input("Weight (kg): "))
waist = float(input("Waist (cm): "))
neck = float(input("Neck (cm): "))

x = pd.DataFrame([{
    "age": age,
    "gender": gender,
    "height_cm": height,
    "weight_kg": weight,
    "waist_cm": waist,
    "neck_cm": neck
}])

x_scaled = scaler.transform(x)

pred_bf = model.predict(x_scaled)[0]

if waist < 0.4 * height or waist > height:
    print(" Waist measurement unrealistic.")
    exit()

if neck < 25 or neck > 50:
    print(" Neck measurement unrealistic.")
    exit()

if weight < 40 or weight > 200:
    print(" Weight unrealistic.")
    exit()

generate_recommendation(pred_bf, weight, gender)





print("Raw model output:", model.predict(x_scaled))
print(df["body_fat_percent"].describe())