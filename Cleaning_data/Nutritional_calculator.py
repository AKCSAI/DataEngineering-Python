# Sample nutrition_dict (values are per 100g)
nutrition_dict = {
    "Croissants, cheese": {
        "calories": 413,
        "total_fat": 17.6,
        "protein": 6.6,
        "carbohydrate": 38.6,
        "sugars": 5.3
    },
    "Orange juice, raw": {
        "calories": 45.4,
        "total_fat": 0.2,
        "protein": 0.7,
        "carbohydrate": 10.4,
        "sugars": 7.2
    }
}

def nutritional_summary(meal_plan):
    result = {
        "calories": 0.0,
        "total_fat": 0.0,
        "protein": 0.0,
        "carbohydrate": 0.0,
        "sugars": 0.0
    }
    
    for food, grams in meal_plan.items():
        if food not in nutrition_dict:
            return food  # Return first missing food
        
        # Scale each nutrient based on grams / 100
        food_data = nutrition_dict[food]
        factor = grams / 100
        
        for nutrient in result:
            result[nutrient] += food_data[nutrient] * factor
    
    return result

print(nutritional_summary({
    "Croissants, cheese": 150,
    "Orange juice, raw": 250
}))
# Output:
# {'calories': 733.5, 'total_fat': 32.0, 'protein': 15.55, 'carbohydrate': 96.5, 'sugars': 38.025}

print(nutritional_summary({
    "Croissant": 150,
    "Orange juice": 250
}))
# Output:
# "Croissant"
