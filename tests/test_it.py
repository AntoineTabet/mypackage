from mypackage.lib import try_me
def test_it():
    list1=[1,2,3,4,7,8,9]
    assert isinstance(try_me(list1),int)
