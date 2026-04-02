import numpy as np

def generate(stimType, canvassize=50, objsize=10):
    canvascenter = canvassize / 2

    # I AM GOING  TO USE 1 for white and -1 for black. This makes it easier for pixel flipping in the code, gonna convert it later

    ###0 ~~~ BLACK TRANSLATING STIMULUS ~~~###
    ###1 ~~~ WHITE TRANSLATING STIMULUS ~~~###
    ###2 ~~~ GREY TRANSLATING STIMULUS ~~~###
    ###3 ~~~ CRYPTIC TRANSLATING STIMULUS ~~~###
    ###4 ~~~ ALTERNATING FLIP STIMULUS ~~~###
    ###5 ~~~ BLACK FLASH STIMULUS ~~~###
    ###6 ~~~ WHITE FLASH STIMULUS ~~~###
    ###7 ~~~ RANDOM FLASH STIMULUS ~~~###

    bgimage = np.random.choice([-1, 1], size=(int(canvassize), int(canvassize)))  # generate a white noise bg

    blackOBJ = np.ones((int(objsize), int(objsize))) * -1  # black square
    whiteOBJ = np.ones((int(objsize), int(objsize)))  # white square
    greyOBJ = np.zeros((int(objsize), int(objsize)))  # grey square

    secondOrderOBJ = bgimage[int(canvascenter - objsize / 2):int(canvascenter + objsize / 2),
                     int(canvascenter - objsize / 2):int(
                         canvascenter + objsize / 2)]  # take from the bg the central square for translating second order

    AltFlipOBJ = bgimage[int(canvascenter - objsize * 3 / 2):int(canvascenter + objsize * 3 / 2),
                 int(canvascenter - objsize / 2):int(
                     canvascenter + objsize / 2)]  # this instead takes the rectangle used for rectangular based objects
    RandFlashOBJ = bgimage[int(canvascenter - objsize * 3 / 2):int(canvascenter + objsize * 3 / 2),
                   int(canvascenter - objsize / 2):int(
                       canvascenter + objsize / 2)]  # this instead takes the rectangle used for rectangular based objects

    travel_positions = np.arange(start=10, stop=-10, step=-1)

    # prepare lists to contain stim frames
    blackSTIM = []
    whiteSTIM = []
    greySTIM = []
    secondOrderSTIM = []
    AltFlipSTIM = []
    blackFlashSTIM = []
    whiteFlashSTIM = []
    randomFlashSTIM = []
    blank = []

    if stimType == 0:
        ###~~~ BLACK TRANSLATING STIMULUS ~~~###
        for i in range(5):  # five frames before first stimulus appearance
            blackSTIM.append(bgimage)
        for pos in travel_positions:
            thisframe = bgimage.copy()
            thisframe[int(canvascenter + pos - objsize / 2):int(canvascenter + pos + objsize / 2),
            int(canvascenter - objsize / 2):int(canvascenter + objsize / 2)] = blackOBJ
            blackSTIM.append(thisframe)
        for pos in list(reversed(travel_positions)):
            thisframe = bgimage.copy()
            thisframe[int(canvascenter + pos - objsize / 2):int(canvascenter + pos + objsize / 2),
            int(canvascenter - objsize / 2):int(canvascenter + objsize / 2)] = blackOBJ
            blackSTIM.append(thisframe)
        for i in range(5):
            blackSTIM.append(bgimage)
        outSTIM = np.array(blackSTIM)

    elif stimType == 1:
        ###~~~ WHITE TRANSLATING STIMULUS ~~~###
        for i in range(5):  # five frames before first stimulus appearance
            whiteSTIM.append(bgimage)
        for pos in travel_positions:
            thisframe = bgimage.copy()
            thisframe[int(canvascenter + pos - objsize / 2):int(canvascenter + pos + objsize / 2),
            int(canvascenter - objsize / 2):int(canvascenter + objsize / 2)] = whiteOBJ
            whiteSTIM.append(thisframe)
        for pos in list(reversed(travel_positions)):
            thisframe = bgimage.copy()
            thisframe[int(canvascenter + pos - objsize / 2):int(canvascenter + pos + objsize / 2),
            int(canvascenter - objsize / 2):int(canvascenter + objsize / 2)] = whiteOBJ
            whiteSTIM.append(thisframe)
        for i in range(5):
            whiteSTIM.append(bgimage)
        outSTIM = np.array(whiteSTIM)

    elif stimType == 2:
        ###~~~ GREY TRANSLATING STIMULUS ~~~###
        for i in range(5):  # five frames before first stimulus appearance
            greySTIM.append(bgimage)
        for pos in travel_positions:
            thisframe = bgimage.copy()
            thisframe[int(canvascenter + pos - objsize / 2):int(canvascenter + pos + objsize / 2),
            int(canvascenter - objsize / 2):int(canvascenter + objsize / 2)] = greyOBJ
            greySTIM.append(thisframe)
        for pos in list(reversed(travel_positions)):
            thisframe = bgimage.copy()
            thisframe[int(canvascenter + pos - objsize / 2):int(canvascenter + pos + objsize / 2),
            int(canvascenter - objsize / 2):int(canvascenter + objsize / 2)] = greyOBJ
            greySTIM.append(thisframe)
        for i in range(5):
            greySTIM.append(bgimage)
        outSTIM = np.array(greySTIM)

    elif stimType == 3:
        ###~~~ CRYPTIC TRANSLATING STIMULUS ~~~###
        for i in range(5):  # five frames before first stimulus appearance
            crypticSTIM.append(bgimage)
        for pos in travel_positions:
            thisframe = bgimage.copy()
            thisframe[int(canvascenter + pos - objsize / 2):int(canvascenter + pos + objsize / 2),
            int(canvascenter - objsize / 2):int(canvascenter + objsize / 2)] = crypticOBJ
            crypticSTIM.append(thisframe)
        for pos in list(reversed(travel_positions)):
            thisframe = bgimage.copy()
            thisframe[int(canvascenter + pos - objsize / 2):int(canvascenter + pos + objsize / 2),
            int(canvascenter - objsize / 2):int(canvascenter + objsize / 2)] = crypticOBJ
            crypticSTIM.append(thisframe)
        for i in range(5):
            crypticSTIM.append(bgimage)
        outSTIM = np.array(crypticSTIM)

    elif stimType == 4:
        ###~~~ ALTERNATING FLIP STIMULUS ~~~###
        flippers = [np.random.choice([-1, 1], size=AltFlipOBJ.shape, p=[50 / 300, 250 / 300]) for i in range(20)]
        # prepare data flipping. Each pixel may either flip (-1) or not flip (1). In each given frame, 50 pixels should flip.
        # this is half the number of total pixels of the square stimulus. Being the background random, half the pixels will stay
        # the same color, half will change. Given that the total area of movement goes from -15 to +15, the full pixel space
        # is 10*30, for a total of 300 pixels. SO the probability of a pixel flipping per frame should be 50/300
        thisframe = bgimage.copy()
        for i in range(5):  # five frames before first stimulus appearance
            AltFlipSTIM.append(bgimage)
        for flp in flippers:
            AltFlipOBJ = thisframe[int(canvascenter - objsize * 3 / 2):int(canvascenter + objsize * 3 / 2),
                         int(canvascenter - objsize / 2):int(canvascenter + objsize / 2)].copy()
            thisframe[int(canvascenter - objsize * 3 / 2):int(canvascenter + objsize * 3 / 2),
            int(canvascenter - objsize / 2):int(canvascenter + objsize / 2)] = AltFlipOBJ.copy() * flp
            AltFlipSTIM.append(thisframe.copy())
        for flp in reversed(flippers):
            AltFlipOBJ = thisframe[int(canvascenter - objsize * 3 / 2):int(canvascenter + objsize * 3 / 2),
                         int(canvascenter - objsize / 2):int(canvascenter + objsize / 2)].copy()
            thisframe[int(canvascenter - objsize * 3 / 2):int(canvascenter + objsize * 3 / 2),
            int(canvascenter - objsize / 2):int(canvascenter + objsize / 2)] = AltFlipOBJ.copy() * flp
            AltFlipSTIM.append(thisframe.copy())
        for i in range(5):
            AltFlipSTIM.append(bgimage)
        outSTIM = np.array(AltFlipSTIM)

    elif stimType == 5:
        ###~~~ BLACK FLASH STIMULUS ~~~###
        for i in range(5):  # five frames before first stimulus appearance
            blackFlashSTIM.append(bgimage)
        for i in range(40):
            thisframe = bgimage.copy()
            if i % 2 == 0:
                thisframe[int(canvascenter - objsize / 2):int(canvascenter + objsize / 2),
                int(canvascenter - objsize / 2):int(canvascenter + objsize / 2)] = blackOBJ
            blackFlashSTIM.append(thisframe)
        for i in range(5):
            blackFlashSTIM.append(bgimage)
        outSTIM = np.array(blackFlashSTIM)

    elif stimType == 6:
        ###~~~ WHITE FLASH STIMULUS ~~~###
        for i in range(5):  # five frames before first stimulus appearance
            whiteFlashSTIM.append(bgimage)
        for i in range(40):
            thisframe = bgimage.copy()
            if i % 2 == 0:
                thisframe[int(canvascenter - objsize / 2):int(canvascenter + objsize / 2),
                int(canvascenter - objsize / 2):int(canvascenter + objsize / 2)] = whiteOBJ
            whiteFlashSTIM.append(thisframe)
        for i in range(5):
            whiteFlashSTIM.append(bgimage)
        outSTIM = np.array(whiteFlashSTIM)

    elif stimType == 7:
        ###~~~ RANDOM FLASH STIMULUS ~~~###
        flipper = np.random.choice([-1, 1], size=AltFlipOBJ.shape, p=[50 / 300, 250 / 300])
        # this flipper is the same as above, but it is only one, as it repeats over subsequent frames
        thisframe = bgimage.copy()
        for i in range(5):  # five frames before first stimulus appearance
            randomFlashSTIM.append(bgimage)
        for i in range(40):
            RandFlashOBJ = thisframe[int(canvascenter - objsize * 3 / 2):int(canvascenter + objsize * 3 / 2),
                           int(canvascenter - objsize / 2):int(canvascenter + objsize / 2)].copy()
            thisframe[int(canvascenter - objsize * 3 / 2):int(canvascenter + objsize * 3 / 2),
            int(canvascenter - objsize / 2):int(canvascenter + objsize / 2)] = RandFlashOBJ.copy() * flipper
            randomFlashSTIM.append(thisframe.copy())
        for i in range(5):
            randomFlashSTIM.append(bgimage)
        outSTIM = np.array(randomFlashSTIM)

    elif stimType == 8:
        for i in range(50):
            blank.append(bgimage)
        outSTIM = np.array(blank)

    return outSTIM
