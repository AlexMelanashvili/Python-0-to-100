word = "supercalifragilisticexpialidocious"
word[5:9:1]
'cali'
word[5:]
'califragilisticexpialidocious'
word[word.index("fra"):word.index("gilistic")]
'fra'
word[word.index("cex"):word.index("piali")]
'cex'
word[word.index("agili"):word.index("stice")]
'agili'

what is your email address?: adsda@dsd.com
Your username is {} and your domain name is {}.format(user, domain)

what is your email address?: asdsd@gmg.com
Your username is asdsd and your domain name is gmg.com

name = "Alex"
age = 28
address = "Tbilisi"

output = "My name is {} and I am {} years old and I live in {}".format(name,str(age),address)
print(output)
My name is Alex and I am 28 years old and I live in Tbilisi
