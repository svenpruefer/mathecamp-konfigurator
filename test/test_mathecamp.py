from src.camp import mathecamp

################
# Sample Cases #
################

# TODO write Mathecamp test example

def getMathecampExample():
    pass

#####################
# Constructor tests #
#####################

def test_mathecampConstructorAndToDict():
    mathecamp = getMathecampExample()
    assert (mathecamp.toDict() == {})


####################
# Dictionary tests #
####################

def test_mathecampToDictAndFromDict():
    mathecampDictionary = {}
    assert (mathecamp.fromDict(mathecampDictionary).toDict() == mathecampDictionary)


###############
# Print tests #
###############

def test_mathecampPrint():
    mathecamp = getMathecampExample()
    assert (mathecamp.__str__() == "")
