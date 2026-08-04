import json
from pet import Pet
def save_pet(pet):
    pet_data={
        "name":pet.name,
        "hunger":pet.hunger,
        "mood":pet.mood,
        "energy":pet.energy,
        "age":pet.age,
        "gender":pet.gender
    }
    with open('pet.json','w',encoding='utf-8') as f:
        json.dump(pet_data,f,indent=4,ensure_ascii=False)
def load_pet():
    try:
        with open('pet.json',"r",encoding="utf-8") as f:
            data=json.load(f)
    except FileNotFoundError:
        return None
    pet=Pet(
        data["name"],
        data["age"],
        data["gender"]
    )


    pet.hunger=data["hunger"]
    pet.mood=data["mood"]
    pet.energy=data["energy"]
    return pet




       
    