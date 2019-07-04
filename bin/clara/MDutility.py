"""usefully things of markdown
    usage:
    >>>from clara import MDutility as m
    >>>m.genOutLine([2,3])
    # 1
    ## 1.1
    ## 1.2
    ## 1.3
    # 2
    ## 2.1
    ## 2.2
    ## 2.3

    >>>m.genOutLine([2,3],produce=[2])
    ## 2.1
    ### 2.1.1
    ### 2.1.2
    ### 2.1.3
    ## 2.2
    ### 2.2.1
    ### 2.2.2
    ### 2.2.3
"""


def genOutLine(orders: [int], produce=[]):
    if orders:
        for i in range(1, orders[0] + 1):
            print(genHeadingLabel(produce + [i]))
            if len(orders) > 1:
                genOutLine(orders[1:], produce + [i])


def genHeadingLabel(levels: [int]):
    if not levels:
        return ""

    label = "#" * len(levels)
    title = str(levels[0])
    for level in levels[1:]:
        title += '.' + str(level)

    return label + ' ' + title


# def produceLevelLabel(levels: list, prefix="#"):
#     if not levels:
#         return ""

#     label = "#" * len(levels)
#     title = str(levels[0])
#     for level in levels[1:]:
#         title += '.' + str(level)

#     return label + ' ' + title

# def deepList(orders, produce=[]):
#     if orders:
#         for i in range(1, orders[0] + 1):
#             print(produceLevelLabel(produce + [i]))
#             if len(orders) > 1: deepList(orders[1:], produce + [i])
