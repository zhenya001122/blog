from django.db import models
from django.db.models import F, QuerySet, Sum
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

from shop.models import Product
from shop.spiders import OmaSpider


def get_sorted_product(queryset: QuerySet, order_by: str):
    if order_by == "cost":
        return queryset.order_by("cost")
    elif order_by == "-cost":
        return queryset.order_by("-cost")
    elif order_by == "sold":
        queryset = queryset.annotate(sold=Sum(F("cost") * F("purchases__count")))
        return queryset.order_by("sold")
    elif order_by == "popular":
        queryset = queryset.annotate(popular=Sum("purchases__count"))
        return queryset.order_by("popular")
    return queryset


def run_oma_spider(dry_run: bool = False):
    if dry_run:
        Product.objects.all().delete()

    def crawler_results(signal, sender, item, response, spider):
        Product.objects.update_or_create(external_id=item["external_id"], defaults=item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process = CrawlerProcess(get_project_settings())
    process.crawl(OmaSpider)
    process.start()


def get_popular_products():
    queryset = Product.objects.annotate(
        sold=Sum(
            F("cost") * F("purchases__count"),
            output_field=models.FloatField(),
            default=0,
        )
    )
    return queryset.order_by("-sold")
