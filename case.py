import pygame
import random
import modules.odds as odds
import modules.wear_values as wear
import modules.cases.csgo_weapon_case as case1
import modules.cases.esports_2013_case as case2

# Pygame Initialization #

pygame.init()
mainLoop = True
size = (512, 512)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("CSGO Case Unboxer")
screen.fill((255, 255, 255))
loopCount = 0
image_assets_path = "assets/images/"

###########################

# CS:GO Case Initialization #

list_of_cases = ["placeholder", case1, case2]
case_opened = False
show_image_skin = False
show_image_case = False
show_image_stattrak = False
image_stattrak = pygame.image.load(image_assets_path + "stattrak.png")

while mainLoop:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            mainLoop = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                case_opened = True
                case_id = 1
            if event.key == pygame.K_w:
                case_opened = True
                case_id = 2

    # Pygame Loop #
    screen.fill((255, 255, 255))
    ###############

    # CS:GO Case Loop #

    if case_opened == True:

        rarity_float = 100 * random.random()
        image_case = pygame.image.load(
            image_assets_path + list_of_cases[case_id].case_name + "/" + "case.png"
        )
        show_image_stattrak = False
        show_image_skin = False

        if rarity_float < odds.mil_spec:

            rarity = list_of_cases[case_id].mil_spec

            selected_skin = random.randint(0, len(rarity) - 1)
            skin_full_name = (
                rarity[selected_skin]["weapon"] + " | " + rarity[selected_skin]["skin"]
            )
            image_skin = pygame.image.load(
                image_assets_path
                + list_of_cases[case_id].case_name
                + "/"
                + str(rarity[selected_skin]["id"])
                + ".png"
            )

        elif rarity_float < odds.restricted and rarity_float >= odds.mil_spec:

            rarity = list_of_cases[case_id].restricted

            selected_skin = random.randint(0, len(rarity) - 1)
            skin_full_name = (
                rarity[selected_skin]["weapon"] + " | " + rarity[selected_skin]["skin"]
            )
            image_skin = pygame.image.load(
                image_assets_path
                + list_of_cases[case_id].case_name
                + "/"
                + str(rarity[selected_skin]["id"])
                + ".png"
            )

        elif rarity_float < odds.classified and rarity_float >= odds.restricted:

            rarity = list_of_cases[case_id].classified

            selected_skin = random.randint(0, len(rarity) - 1)
            skin_full_name = (
                rarity[selected_skin]["weapon"] + " | " + rarity[selected_skin]["skin"]
            )
            image_skin = pygame.image.load(
                image_assets_path
                + list_of_cases[case_id].case_name
                + "/"
                + str(rarity[selected_skin]["id"])
                + ".png"
            )

        elif rarity_float < odds.covert and rarity_float >= odds.classified:

            rarity = list_of_cases[case_id].covert

            selected_skin = random.randint(0, len(rarity) - 1)
            skin_full_name = (
                rarity[selected_skin]["weapon"] + " | " + rarity[selected_skin]["skin"]
            )
            image_skin = pygame.image.load(
                image_assets_path
                + list_of_cases[case_id].case_name
                + "/"
                + str(rarity[selected_skin]["id"])
                + ".png"
            )

        elif rarity_float < odds.exceedingly_rare and rarity_float >= odds.covert:

            rarity = list_of_cases[case_id].exceedingly_rare

            selected_skin = random.randint(0, len(rarity) - 1)
            selected_knife_skin_index = random.randint(
                0, (len(rarity[selected_skin]["skin"]) - 1),
            )
            selected_knife_skin_name = rarity[selected_skin]["skin"][
                selected_knife_skin_index
            ]

            if selected_knife_skin_index == 0:
                skin_full_name = rarity[selected_skin]["weapon"]

            else:
                skin_full_name = (
                    rarity[selected_skin]["weapon"] + " | " + selected_knife_skin_name
                )
            image_skin = pygame.image.load(
                image_assets_path
                + list_of_cases[case_id].case_name
                + "/knives/"
                + str(rarity[selected_skin]["id"])
                + "/"
                + str(selected_knife_skin_index)
                + ".png"
            )

        stattrak_float = 100 * random.random()

        if stattrak_float < odds.stattrak:
            stattrak = True
        else:
            stattrak = False

        case_opened = False

        show_image_skin = True
        show_image_case = True
        if stattrak == True:
            if rarity_float < odds.exceedingly_rare and rarity_float >= odds.covert:
                skin_full_name = "★ StatTrak™ " + skin_full_name
            else:
                skin_full_name = "StatTrak™ " + skin_full_name
            show_image_stattrak = True
        elif stattrak == False and (
            rarity_float < odds.exceedingly_rare and rarity_float >= odds.covert
        ):
            skin_full_name = "★ " + skin_full_name
        if rarity == list_of_cases[case_id].exceedingly_rare:
            print("Index:" + str(selected_knife_skin_index))
            wear_float = random.uniform(
                (case1.knife_skin_wears[selected_knife_skin_index - 1][0]),
                (case1.knife_skin_wears[selected_knife_skin_index][1]),
            )
        else:
            wear_float = random.uniform(
                (rarity[selected_skin]["wear_range"][0]),
                (rarity[selected_skin]["wear_range"][1]),
            )

        if wear_float < wear.factory_new[1]:
            skin_wear = "fn"
            skin_wear_full_name = "Factory New"
        elif wear_float < wear.minimal_wear[1] >= wear.factory_new[1]:
            skin_wear = "mw"
            skin_wear_full_name = "Minimal Wear"
        elif wear_float < wear.field_tested[1] >= wear.minimal_wear[1]:
            skin_wear = "ft"
            skin_wear_full_name = "Field-Tested"
        elif wear_float < wear.well_worn[1] >= wear.field_tested[1]:
            skin_wear = "ww"
            skin_wear_full_name = "Well Worn"
        elif wear_float < wear.battle_scarred[1] >= wear.well_worn[1]:
            skin_wear = "bs"
            skin_wear_full_name = "Battle Scarred"

        print(
            "["
            + list_of_cases[case_id].case_full_name
            + "] "
            + skin_full_name
            + " ("
            + skin_wear_full_name
            + ")"
        )

    if show_image_skin == True:
        screen.blit(image_skin, (0, 0))
    if show_image_stattrak == True:
        screen.blit(image_stattrak, (400, 0))
    if show_image_case == True:
        screen.blit(image_case, (0, 300))

    pygame.display.flip()
    clock.tick(60)
    ###################
pygame.quit()
