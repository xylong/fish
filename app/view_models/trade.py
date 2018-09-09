class TradeInfo:
    def __init__(self, books):
        self.total = 0
        self.trades = []

    def _parse(self, books):
        self.total = len(books)
        self.trades = [self.__map_to_trade(book) for book in books]

    def __map_to_trade(self, single):
        if single.create_time:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )
