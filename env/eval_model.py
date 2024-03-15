class Sentence:
    def __init__(self, orig, **kwargs):
        self.orig = orig
        self.kwargs = kwargs


data = ["At one particular retreat, there were eight people in the circle, and I slowly handed tennis balls to one "
        "person to start throwing around the circle.",
        "If you’re less concerned about how you deliver information than with how you receive it, you’ll ultimately "
        "fail at delegation.",
        "People are much more concerned about catching the ball than throwing it.",
        "During the last two decades many developing countries have joined the global tourism market as part of "
        "globalization processes and the fall of the Iron Curtain.",
        "These countries had suffered from negative public and media image which made it challenging for them to "
        "compete over tourists with countries with strong and familiar brands.",
        "However, in the case of destinations suffering from prolonged image crises, it seems almost unrealistic to "
        "expect any target audience to visit a destination and “put aside” these longlasting negative images and "
        "stereotypes, just because of an advertising campaign or other promotional effort.",
        "Tackling prolonged negative place images is crucial for developing tourism in Africa, the Middle East, "
        "Latin America, Eastern Europe and Asia.",
        "Although these destinations differ greatly, in the eyes of many potential tourists they all suffer from weak "
        "place images, negative stereotypes and problematic perceptions.",
        "This recommendation is based on the assumption that this change is welcomed, but laws banning texting while "
        "walking failed in Toronto, Arkansas, Illinois, Nevada, New Jersey and New York.",
        "Meanwhile, high-tech firms are developing technological solutions to the problem, offering a transparent "
        "screen that allows pedestrians to see what is going on in front of them while texting.",
        "Another direction for adaptation to the problem was provided by city councils via better urban planning and "
        "interventions to generate awareness.",
        "Some towns and college campuses have put ‘look up’ signs in dangerous stairwells and intersections",
        "Once again, your mind makes your last thoughts part of reality.",
        "He or she points out what could be improved, but will then tell you how you could or should perform: “I know "
        "you’ll catch the ball perfectly this time.”"]

sentences = []
for i in range(len(data)):
    sentences.append(Sentence(data[i]))


for i, sen in enumerate(sentences):
    print(f"<Original Sentence>\n\t{sen.orig}")
