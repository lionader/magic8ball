#this program tries to provide a random answer out of the possibilities
import random

def magic8ball():
    eball = ['It is certain','It is decidedly so','Without a doubt','Yes - definitely',
                'You may rely on it','As I see it, yes','Most likely','Outlook good',
                'Yes','Signs point to yes','''Don't count on it''','My reply is no.',' My sources say no',
                 ' Outlook not so good.','Very doubtful','Reply hazy','try again','Ask again later','Better not tell you now',
                  'Cannot predict now','Concentrate and ask again']

    len_ball = len(eball)
    ran_guess = random.randint(0,len_ball-1)
    guess = eball[ran_guess]
    return guess


