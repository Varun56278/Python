from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
     [
         r"what is your name ?",
         ["My name is Tim and I'm a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i need your help",
        ["Yes","I'm here to help you find what you need in a snap",]
    ],
    [
        "a quick question before we proceed",
        ["Would you like to receive promo alerts, financal news, and money tips from time to time",]
    ],
    [
        r"can you provide me some information about bank services",
        ["What product are you looking for?","Choose from the option below:loan,accountopen,inquiry",]
    ],
    [
        r"loan",
        ["What Loan product are you interested in?","Choose from the button below:Personal Loan,Car Loan,House Loan,Study Loan",]
    ],
    [
        r"Personal Loan",
        ["Great,(.*)Here are the requirements for a Personal Loan","*If you're currently employed*","Government-issued photo-bearing ID Passport, Driver's License,SSS,PRC,etc","3 months original pay slip and/or Latest income Tax Return with BIR or Bank stamp"]
],
]                                                                                                                                                                                                 
def tim():
    print("Hi, I'm Tim and I chat alot ;)")
    c = Chat(pairs, reflections)
    c.converse()

#call
tim()
