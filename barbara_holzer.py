#!/usr/bin/env python
import sys, os
from PIL import Image, ImageOps, ImageFont, ImageDraw
import tracery, json
import disarticulate
from random import Random
random=Random()
holzer=[
"a little knowledge can go a long way", "a lot of professionals are crackpots", "a man can't know what it is to be a mother", "a name means a lot just by itself", "a positive attitude means all the difference in the world", "a relaxed man is not necessarily a better man", "a sense of timing is the mark of genius", "a sincere effort is all you can ask",
"a single event can have infinitely many interpretations", "a solid home base builds a sense of self", "a strong sense of duty imprisons you", "absolute submission can be a form of freedom", "abstraction is a type of decadence", "abuse of power comes as no surprise", "action causes more trouble than thought", "alienation produces eccentrics or revolutionaries",
"all things are delicately interconnected", "ambition is just as dangerous as complacency", "ambivalence can ruin your life", "an elite is inevitable", "anger or hate can be a useful motivating force", "animalism is perfectly healthy", "any surplus is immoral", "anything is a legitimate area of investigation", "artificial desires are despoiling the earth",
"at times inactivity is preferable to mindless functioning", "at times your unconsciousness is truer than your conscious mind", "automation is deadly", "awful punishment awaits really bad people", "bad intentions can yield good results", "being alone with yourself is increasingly unpopular", "being happy is more important than anything else", "being judgmental is a sign of life",
"being sure of yourself means you're a fool", "believing in rebirth is the same as admitting defeat", "boredom makes you do crazy things", "calm is more conductive to creativity than is anxiety", "categorizing fear is calming", "change is valuable when the oppressed become tyrants", "chasing the new is dangerous to society", "children are the most cruel of all",
"children are the hope of the future", "class action is a nice idea with no substance", "class structure is as artificial as plastic", "confusing yourself is a way to stay honest", "crime against property is relatively unimportant", "decadence can be an end in itself", "decency is a relative thing", "dependence can be a meal ticket", "description is more important than metaphor",
"deviants are sacrificed to increase group solidarity", "disgust is the appropriate response to most situations", "disorganization is a kind of anesthesia", "don't place to much trust in experts", "drama often obscures the real issues", "dreaming while awake is a frightening contradiction", "dying and coming back gives you considerable perspective",
"dying should be as easy as falling off a log", "eating too much is criminal", "elaboration is a form of pollution", "emotional responses ar as valuable as intellectual responses", "enjoy yourself because you can't change anything anyway", "ensure that your life stays in flux", "even your family can betray you", "every achievement requires a sacrifice", "everyone's work is equally important",
"everything that's interesting is new", "exceptional people deserve special concessions", "expiring for love is beautiful but stupid", "expressing anger is necessary", "extreme behavior has its basis in pathological psychology", "extreme self-consciousness leads to perversion", "faithfulness is a social not a biological law", "fake or real indifference is a powerful personal weapon",
"fathers often use too much force", "fear is the greatest incapacitator", "freedom is a luxury not a necessity", "giving free rein to your emotions is an honest way to live", "go all out in romance and let the chips fall where they may", "going with the flow is soothing but risky", "good deeds eventually are rewarded", "government is a burden on the people", "grass roots agitation is the only hope",
"guilt and self-laceration are indulgences", "habitual contempt doesn't reflect a finer sensibility", "hiding your emotions is despicable", "holding back protects your vital energies", "humanism is obsolete", "humor is a release", "ideals are replaced by conventional goals at a certain age", "if you aren't political your personal life should be exemplary", "if you can't leave your mark give up",
"if you have many desires your life will be interesting", "if you live simply there is nothing to worry about", "ignoring enemies is the best way to fight", "illness is a state of mind", "imposing order is man's vocation for chaos is hell", "in some instances it's better to die than to continue", "inheritance must be abolished", "it can be helpful to keep going no matter what",
"it is heroic to try to stop time", "it is man's fate to outsmart himself", "it is a gift to the world not to have babies", "it's better to be a good person than a famous person", "it's better to be lonely than to be with inferior people", "it's better to be naive than jaded", "it's better to study the living fact than to analyze history", "it's crucial to have an active fantasy life",
"it's good to give extra money to charity", "it's important to stay clean on all levels", "it's just an accident that your parents are your parents", "it's not good to hold too many absolutes", "it's not good to operate on credit", "it's vital to live in harmony with nature", "just believing something can make it happen", "keep something in reserve for emergencies",
"killing is unavoidable but nothing to be proud of", "knowing yourself lets you understand others", "knowledge should be advanced at all costs", "labor is a life-destroying activity", "lack of charisma can be fatal", "leisure time is a gigantic smoke screen", "listen when your body talks", "looking back is the first sign of aging and decay", "loving animals is a substitute activity",
"low expectations are good protection", "manual labor can be refreshing and wholesome", "men are not monogamous by nature", "moderation kills the spirit", "money creates taste", "monomania is a prerequisite of success", "morals are for little people",  "most people are not fit to rule themselves","mostly you should mind your own business", "mothers shouldn't make too many sacrifices",
"much was decided before you were born", "murder has its sexual side", "myth can make reality more intelligible", "noise can be hostile", "nothing upsets the balance of good and evil", "occasionally principles are more valuable than people", "offer very little information about yourself", "often you should act like you are sexless", "old friends are better left in the past",
"opacity is an irresistible challenge", "pain can be a very positive thing", "people are boring unless they are extremists", "people are nuts if they think they are important", "people are responsible for what they do unless they are insane", "people who don't work with their hands are parasites", "people who go crazy are too sensitive", "people won't behave if they have nothing to lose",
"physical culture is second best", "planning for the future is escapism", "playing it safe can cause a lot of damage in the long run", "politics is used for personal gain", "potential counts for nothing until it's realized", "private property created crime", "pursuing pleasure for the sake of pleasure will ruin you", "push yourself to the limit as often as possible",
"raise boys and girls the same way", "random mating is good for debunking sex myths", "rechanneling destructive impulses is a sign of maturity", "recluses always get weak", "redistributing wealth is imperative", "relativity is no boon to mankind", "religion causes as many problems as it solves", "remember you always have freedom of choice", "repetition is the best way to learn",
"resolutions serve to ease our conscience", "revolution begins with changes in the individual", "romantic love was invented to manipulate women", "routine is a link with the past", "routine small excesses are worse than then the occasional debauch", "sacrificing yourself for a bad cause is not a moral act", "salvation can't be bought and sold", "self-awareness can be crippling",
"self-contempt can do more harm than good", "selfishness is the most basic motivation", "selflessness is the highest achievement", "separatism is the way to a new beginning", "sex differences are here to stay", "sin is a means of social control", "slipping into madness is good for the sake of comparison", "sloppy thinking gets worse over time", "solitude is enriching",
"sometimes science advances faster than it should", "sometimes things seem to happen of their own accord", "spending too much time on self-improvement is antisocial", "starvation is nature's way", "stasis is a dream state", "sterilization is a weapon of the rulers", "strong emotional attachment stems from basic insecurity", "stupid people shouldn't breed", "survival of the fittest applies to men and animals",
"symbols are more meaningful than things themselves", "taking a strong stand publicizes the opposite position", "talking is used to hide one's inability to act", "teasing people sexually can have ugly consequences", "technology will make or break us", "the cruelest disappointment is when you let yourself down", "the desire to reproduce is a death wish", "the family is living on borrowed time",
"the idea of revolution is an adolescent fantasy", "the idea of transcendence is used to obscure oppression", "the idiosyncratic has lost its authority", "the most profound things are inexpressible", "the mundane is to be cherished", "the new is nothing but a restatement of the old", "the only way to be pure is to stay by yourself", "the sum of your actions determines what you are",
"the unattainable is invariable attractive", "the world operates according to discoverable laws", "there are too few immutable truths today", "there's nothing except what you sense", "there's nothing redeeming in toil", "thinking too much can only cause problems", "threatening someone sexually is a horrible act", "timidity is laughable", "to disagree presupposes moral integrity",
"to volunteer is reactionary", "torture is barbaric", "trading a life for a life is fair enough", "true freedom is frightful", "unique things must be the most valuable", "unquestioning love demonstrates largesse of spirit", "using force to stop force is absurd", "violence is permissible even desirable occasionally", "war is a purification rite", "we must make sacrifices to maintain our quality of life",
"when something terrible happens people wake up", "wishing things away is not effective", "with perseverance you can discover any truth", "words tend to be inadequate", "worrying can help you prepare", "you are a victim of the rules you live by", "you are guileless in your dreams", "you are responsible for constituting the meaning of things", "you are the past present and future", 
"you can live on through your descendants", "you can't expect people to be something they're not", "you can't fool others if you're fooling yourself", "you don't know what's what until you support yourself", "you have to hurt others to be extraordinary", "you must be intimate with a token few", "you must disagree with authority figures", "you must have one grand passion",
"you must know where you stop and the world begins", "you can understand someone of your sex only", "you owe the world not the other way around", "you should study as much as possible", "your actions ae pointless if no one notices", "your oldest fears are the worst ones" ]

grammar1=tracery.Grammar(json.load(open("holzer_markov.json", "r")))
grammar2=tracery.Grammar(json.load(open("templates/proverbs_tracery.json", "r")))
grammar3=tracery.Grammar(json.load(open("templates/memebombs_combined.json", "r")))
slogan=random.choice([random.choice(holzer), random.choice([grammar1.flatten("#origin#"), grammar1.flatten("#origin#"), grammar2.flatten("#origin#"), grammar3.flatten("#origin#")])])
slogan=random.choice([slogan, slogan.upper(), slogan.upper(), slogan.upper(), disarticulate.disarticulate(slogan, random.randint(1, 15))])

print(slogan)

try:
    font=ImageFont.truetype("arialbi.ttf", 64)
except:
    try:
        font=ImageFont.truetype("arial.ttf", 64)
    except:
        font=ImageFont.load_default()
size=font.getsize(slogan)
sloganRender=Image.new("RGB", (size[0]+10, size[1]+10), color="red")
sloganDraw=ImageDraw.Draw(sloganRender)
sloganDraw.text((5, 5), slogan, font=font, fill="white")

candidates=[]
def walk_helper(arg, dirname, fnames):
    for item in fnames:
        fullpath=os.path.join(dirname, item)
        if not (os.path.isdir(fullpath)):
            candidates.append(fullpath)
for path in sys.argv[1:]:
    if(os.path.isdir(path)):
        os.path.walk(path, walk_helper, None)
    else:
        candidates.append(path)
random.shuffle(candidates)
bg=None
for item in candidates:
    try:
        bg=Image.open(item)
        break
    except:
        pass
bg.paste(ImageOps.grayscale(bg), (0, 0))
bg2=Image.new("RGB", bg.size)
bg2.paste(bg, (0, 0))
bg=bg2
while sloganRender.size[0]>bg.size[0] or sloganRender.size[1]>bg.size[1]:
    sloganRender=sloganRender.resize((sloganRender.size[0]/2, sloganRender.size[1]/2))
bg.paste(sloganRender, (bg.size[0]/2-sloganRender.size[0]/2, bg.size[1]/2-sloganRender.size[1]/2))
bg.save("barbara_holzer.png")

