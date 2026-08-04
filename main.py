from pet import Pet
from storage import save_pet,load_pet
def main():
    pet=load_pet()
    if pet is None:
        name=input ("请给我命名吧 ●'◡'●")
        age=int(input('我几岁啦?'))
        gender=input('boy or girl? ✿◡‿◡')
        pet=Pet(name,age,gender)
    while True:
        choice=input('''
        ======电子宠物=====
        1：查看状态
        2：喂食
        3：摸头
        4：睡觉
        5：退出''')
        if choice == '1':
            pet.show_status()
        elif choice =='2':
            pet.feed()
        elif choice =='3':
            pet.touch()
        elif choice =='4':
            pet.sleep()
        elif choice =="5":
            save_pet(pet)
            print('保存成功！')
            break
if __name__ == '__main__':
    main()



                
