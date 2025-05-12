from abc import abstractmethod
from collections import namedtuple
    
News = namedtuple("News", ["type","title"])
class NewsPublisherInterface:
    @abstractmethod
    def add_subscriber(self, subscriber):
        raise NotImplementedError
    @abstractmethod
    def remove_subscriber(self, subscriber):
        raise NotImplementedError
    @abstractmethod
    def notify_subscribers(self):
        raise NotImplementedError

class NewsSubscriberInterface:
    @abstractmethod
    def update(self, news: News):
        pass

class NewsPublisher(NewsPublisherInterface):
    def __init__(self):
        self._subscribers = []
        self._news = None
    
    @property
    def news(self):
        return self._news
    
    @news.setter
    def news(self, news: News):
        self._news = news

    def add_subscriber(self, subscriber):
        self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update(self.news)

class SportsNewsSubsriber(NewsSubscriberInterface):
    def update(self, news: News):
        if news.type == "Sports":
            print(f"[Sports news]: {news.title}")
            return
        print("[Sports news]: ")

class WeatherNewsSubsriber(NewsSubscriberInterface):
    def update(self, news: News):
        if news.type == "Weather":
            print(f"[Weather news]: {news.title}")
            return
        print("[Weather news]: ")
        

class PoliticsNewsSubsriber(NewsSubscriberInterface):
    def update(self, news: News):
        if news.type == "Politics":
            print(f"[Politics news]: {news.title}")
            return
        print("[Politics news]: ")

if __name__ == "__main__":
    publisher = NewsPublisher()
    s = SportsNewsSubsriber()
    w = WeatherNewsSubsriber()
    p = PoliticsNewsSubsriber()
    publisher.add_subscriber(s)
    publisher.add_subscriber(p)
    publisher.add_subscriber(w)
    publisher.news = News("Sports","NBA vs. Lakers")
    publisher.notify_subscribers()
    print("_"*10)
    publisher.news = News("Weather","Hot")
    publisher.notify_subscribers()
    print("_"*10)
    publisher.news = News("Politics","Trump")
    publisher.notify_subscribers()
    print("_"*10)
    publisher.remove_subscriber(s)
    publisher.notify_subscribers()
    print("_"*10)