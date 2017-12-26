from src.mktypes import MathCircle


################
# Sample Cases #
################

def getMathCircleExample(nr=0):
    if (nr == 0):
        return (MathCircle("10a", 10, [1, 2], 2, ["Symplektische Geometrie", "Motive"]),
                {"name": "10a", "grade": 10, "members": [1, 2], "room": 2,
                 "topics": ["Symplektische Geometrie", "Motive"]})
    else:
        return (MathCircle("5c", 5, [3], 1, []), {"name": "5c", "grade": 5, "members": [3], "room": 1,
                                                  "topics": []})


#####################
# Constructor tests #
#####################

def test_mathCircleConstructorAndToDict():
    (mathCircle, mathCircleDict) = getMathCircleExample()
    assert (mathCircle.toDict() == mathCircleDict)


####################
# Dictionary tests #
####################

def test_mathCircleToDictAndFromDict():
    mathCircleDictionary = getMathCircleExample()[1]
    assert (MathCircle.fromDict(mathCircleDictionary).toDict() == mathCircleDictionary)


###############
# Print tests #
###############

def test_mathCirclePrint():
    mathCircle = getMathCircleExample()[0]
    assert (mathCircle.__str__() == "MathCircle(10a,10,[1, 2],2,['Symplektische Geometrie', 'Motive'])")
