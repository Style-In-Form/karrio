import django.db.models as models
import karrio.server.providers.models as providers


@providers.has_rate_sheet("deutschepost")
class DeutschePostSettings(providers.Carrier):
    class Meta:
        db_table = "deutschepost-settings"
        verbose_name = "Deutsche Post Settings"
        verbose_name_plural = "Deutsche Post Settings"

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dhl_api_key = models.CharField(max_length=200)
    customer_number = models.CharField(max_length=50)
    tracking_consumer_key = models.CharField(max_length=200, blank=True, null=True)
    tracking_consumer_secret = models.CharField(max_length=200, blank=True, null=True)
    services = models.ManyToManyField("ServiceLevel", blank=True)

    @property
    def carrier_name(self) -> str:
        return "deutschepost"


SETTINGS = DeutschePostSettings
