anime_type = ["isekai","adventure","sciFi","manwa"]
anime_title = []

while True:
    ans = input("Do you know any anime ---> (yes/no)")
    if ans.lower() == 'yes':
        print("What is its type --> ? select from the list")
        for x in anime_type:
            print(x) #traversing a list

        a_type = input("type ---> ")

        title = input("what is the tittle of the anime ---> ")
        anime_title.append(title)
        continue
    else:
        print("Thank you")
        break