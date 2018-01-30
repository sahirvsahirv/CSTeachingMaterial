from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site
from twisted.internet import reactor
from arachne import Arachne

from scrapy.settings import Settings

app = Arachne(__name__)
resource = WSGIResource(reactor, reactor.getThreadPool(), app)
site = Site(resource)

reactor.listenTCP(8080, site)
if __name__ == '__main__':
    settings = Settings()
    settings.set("ITEM_PIPELINES", {'makerspacescraper.pipelines.AddTablePipeline': 100})
    reactor.run()

