from bin.server import SERVER, Server


def run(bot: Server) -> None:
    bot.run()


if __name__ == '__main__':
    run(bot=SERVER)
