
def or_(b1, b2 ):
    if b1 == "1" or b2 == "1":
        return "1"
    else:
        return "0"
    
def and_(b1, b2):
    if b1 == "0" or b2 == "0":
        return "0"
    else:
        return "1"
    
def not_(b1):
    if b1 == "0" :
        return "1"
    else:
        return "0"
    
def xor_(b1, b2):
    if b1 == b2 :
        return "0"
    else:
        return "1"
    
def xnor_(b1, b2):
    if b1 == b2 :
        return "1"
    else:
        return "0"
    

def nand_(b1, b2):
    if b1 == "0" or b2 == "0":
        return "1"
    else:
        return "0"
    
# def test_logic_gates():
#     # OR Gate Tests
#     assert or_("0", "0") == "0"
#     assert or_("0", "1") == "1"
#     assert or_("1", "0") == "1"
#     assert or_("1", "1") == "1"
    
#     # AND Gate Tests
#     assert and_("0", "0") == "0"
#     assert and_("0", "1") == "0"
#     assert and_("1", "0") == "0"
#     assert and_("1", "1") == "1"
    
#     # NOT Gate Tests
#     assert not_("0") == "1"
#     assert not_("1") == "0"
    
#     # XOR Gate Tests
#     assert xor_("0", "0") == "0"
#     assert xor_("0", "1") == "1"
#     assert xor_("1", "0") == "1"
#     assert xor_("1", "1") == "0"
    
#     # XNOR Gate Tests
#     assert xnor_("0", "0") == "1"
#     assert xnor_("0", "1") == "0"
#     assert xnor_("1", "0") == "0"
#     assert xnor_("1", "1") == "1"
    
#     # NAND Gate Tests
#     assert nand_("0", "0") == "1"
#     assert nand_("0", "1") == "1"
#     assert nand_("1", "0") == "1"
#     assert nand_("1", "1") == "0"

#     print("All tests passed!")

# test_logic_gates()
