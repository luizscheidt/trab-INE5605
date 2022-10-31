from datetime import datetime

class Data:

    def hoje():
        agora = datetime.now()
        return agora.strftime('%d/%m/%Y')
