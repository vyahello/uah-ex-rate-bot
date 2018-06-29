from bin.bot.messages import Answer, BotAnswer, BotMessage
from bin.bot.text import Text, InputText
from bin.ex_rate.currency import ForeignCurrency, Currency
from bin.server import SERVER, METHODS, Request, ServerRequest, POST, WELCOME_MESSAGE, Server

_server: Server = SERVER


@_server.route('/', methods=METHODS)
def index():
    request: Request = ServerRequest()
    answer: Answer = BotAnswer(request)

    if request.method() == POST:
        text: Text = InputText(answer.message())

        if text.match():
            currency: Currency = ForeignCurrency(text.get_coin())
            BotMessage(answer.chat_id(), currency).send()

    return WELCOME_MESSAGE
