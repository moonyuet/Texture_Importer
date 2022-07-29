
#####################
#SET_FUNCTION

#####################

def set_color(ctrlList=None, color=None):
    
    # create a list of color range
    color_range = [4, 13, 25, 17, 17, 15, 6, 16]

    for ctrlName in ctrlList:

        try:
            mc.setAttr(ctrlName + 'Shape.overrideEnabled', 1)
            for i in range(1, color):
                if color == i + 1:
                    mc.setAttr(ctrlName + 'Shape.overrideColor', color_range[i])
        except:
            pass

#set_color(['circle','circle1'], 8)
