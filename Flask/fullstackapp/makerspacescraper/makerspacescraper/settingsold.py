

#adding spider settings to enable arachne as a flask app
#location is the location of the makerspacebot.py file
SPIDER_SETTINGS = [
    {
        'endpoint': 'makerspacebot',
        'location': 'spiders.Makerspacebot',
        'spider': 'MakerspacebotSpider',
        'scrapy_settings': {
                                'ITEM_PIPELINES': {
                                    'pipelines.JsonPipeline': 300
                                }
                            }
    }
]

EXPORT_JSON = True
