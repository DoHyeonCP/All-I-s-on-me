from celery import shared_task
from callapi import SkCallCongestion
from .models import AreaInfo

@shared_task
def periodic_upadate_congetion_data():
    updater = UpdateSkAPi()
    updater.update_congestion_data()


class UpdateSkAPi:
    def __init__(self):
        self.sk_songpagu_areas_id = ["9273", "9270"]
        self.sk_songpagu_pois_id = ["5783805", "5799875", "188633"]
        self.areas_api = SkCallCongestion.areas_get
        self.pois_api = SkCallCongestion.pois_get

    def update_congestion_data(self):
        AreaInfo.objects.all().delete()
        for sk_areaid in self.sk_songpagu_areas_id:
            self.areas_api(sk_areaid)
        print("save areas to AreaInfo")
        for sk_poiid in self.sk_songpagu_pois_id:
            self.pois_api(sk_poiid)
        print("save pois to AreaInfo")

    