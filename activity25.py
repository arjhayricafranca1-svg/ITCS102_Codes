#different genre

Explosion_Magic = "Megumin's signature spell is an ultra-destructive, \n massive-scale blast. She invests all of her skill points into boosting its raw destructive  \n power rather than learning other spells or raising her mana pool."
High_Mana_and_High_Intelligence = " As a Crimson Demon Arch Wizard, \n she possesses high intelligence and strong magical aptitude,\n allowing her to output massive damage—often acting as a finisher against tough foes."
HighSpeed_Incantation_and_Staff_Boosts = "Through skill investment and training, \n she can speed up her casting and uses a magic staff \n (upgraded with powerful crystals) to amplify and support her Explosion spell."









Megumin = [Explosion_Magic, High_Mana_and_High_Intelligence,HighSpeed_Incantation_and_Staff_Boosts]
KonoSuba = ["Aqua",Megumin,"Darkness"]
isekai = ["The Boy and the Beast", KonoSuba,  "Isekai Quartet: The Movie Another World "]
anime_type = {"old_school":"shonen", "new":isekai, "korean":"manwa"}

print(anime_type["new"][1][1][0])