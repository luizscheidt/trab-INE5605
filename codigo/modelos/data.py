from datetime import datetime

class Data:

    def agora():
        agora = datetime.now()
        return agora.strftime('%m/%d/%Y')
