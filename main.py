from chatterbot import ChatBot


chatbot = ChatBot(

    'Ultron',
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    logic_adapter = ['chatterbot.MathematicalEvaluation',
                     'chatterbot.logic.TimeLogicAdapter',
                     'chatterbot.logic.BestMatch'
                    {

                        'import_path' : 'chatterbot.logic.BestMatch',
                        'default_response' : 'I am sorry, I do not understand' ,
                        'maximumm_similarity_threshold' : 0.90

                    } 
                     
                    ],
    database_uri='sqlite://database.sqlite3'
                  

)



from chatterbot.trainers import ListTrainers

trainser = ListTrainers(chatbot) 
traingdata = open(path to traing data ).read().split()license

#Traing the corpus
from chatterbot.trainers import ChatterBotCorpusTrainer

trainercorpus = ChatterBotCorpusTrainer(chatbot)
trainercorpus.train(
    'chatterbot.corpus.english'
)


name = input("Enter your name: ")
print("Hello", name , "Wellcome to the invercity.\n How i can help you today")
while True:
    request = input(name+': ')
    if request == "Bye" or request == "bye":
        break
    else:
        response = chatbot.get_response(request)
        print('Bot:' ,response)

    