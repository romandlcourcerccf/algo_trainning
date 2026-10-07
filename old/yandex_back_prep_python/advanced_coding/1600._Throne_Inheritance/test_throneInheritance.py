from throneInheritance import ThroneInheritance


# Explanation
# ThroneInheritance t= new ThroneInheritance("king"); // order: king
# t.birth("king", "andy"); // order: king > andy
# t.birth("king", "bob"); // order: king > andy > bob
# t.birth("king", "catherine"); // order: king > andy > bob > catherine
# t.birth("andy", "matthew"); // order: king > andy > matthew > bob > catherine
# t.birth("bob", "alex"); // order: king > andy > matthew > bob > alex > catherine
# t.birth("bob", "asha"); // order: king > andy > matthew > bob > alex > asha > catherine
# t.getInheritanceOrder(); // return ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
# t.death("bob"); // order: king > andy > matthew > bob > alex > asha > catherine
# t.getInheritanceOrder(); // return ["king", "andy", "matthew", "alex", "asha", "catherine"]


def test_throne_inheritance():
    t = ThroneInheritance("king")

    t.birth("king", "andy")
    t.birth("king", "bob")
    t.birth("king", "catherine")
    t.birth("andy", "matthew")
    t.birth("bob", "alex")
    t.birth("bob", "asha")

    assert t.getInheritanceOrder() == [
        "king",
        "andy",
        "matthew",
        "bob",
        "alex",
        "asha",
        "catherine",
    ]
    t.death("bob")

    t.getInheritanceOrder() == ["king", "andy", "matthew", "alex", "asha", "catherine"]
