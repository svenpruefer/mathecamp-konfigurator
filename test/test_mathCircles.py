from src.mktypes import MathCircle


################
# Sample Cases #
################

def getMathCircleExample():
    return (MathCircle("10a", 10, [2, 9, 3], 2, ["Symplektische Geometrie", "Motive"]))


#####################
# Constructor tests #
#####################

def test_mathCircleConstructorAndToDict():
    mathCircle = getMathCircleExample()
    assert (mathCircle.toDict() == {"name": "10a", "grade": 10, "members": [2, 9, 3], "room": 2,
                                    "topics": ["Symplektische Geometrie", "Motive"]})


####################
# Dictionary tests #
####################

def test_mathCircleToDictAndFromDict():
    mathCircleDictionary = {"name": "10a", "grade": 10, "members": [2, 9, 3], "room": 2,
                            "topics": ["Symplektische Geometrie", "Motive"]}
    assert (MathCircle.fromDict(mathCircleDictionary).toDict() == mathCircleDictionary)


###############
# Print tests #
###############

def test_mathCirclePrint():
    mathCircle = getMathCircleExample()
    assert (mathCircle.__str__() == "MathCircle(10a,10,[2, 9, 3],2,['Symplektische Geometrie', 'Motive'])")
