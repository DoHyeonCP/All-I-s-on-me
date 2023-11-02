from django.test import TestCase
from unittest.mock import Mock
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch
from .callapi import SkCallCongestion
from .models import AreaInfo
import json

class AreaInfoModelTestCase(TestCase):
    def test_area_info_creation(self):
        AreaInfo.objects.create(area_name="Test Area", datetime="2023-11-01T12:00:00", congestion_level="보통")
        area_info = AreaInfo.objects.get(area_name="Test Area")
        self.assertEqual(area_info.congestion_level, "보통")


class SkCallCongestionTestCase(TestCase):
    @patch('skapi.callapi.requests.get')
    def test_get_api_success(self, mock_get):
        # 성공적인 API 응답을 모의합니다.
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": {
                "code": "00",
                "message": "success",
                "totalCount": 1
            },
            "contents": {
                "poiId": "188485",
                "poiName": "롯데백화점잠실점",
                "rltm": [
                    {
                        "datetime": "20230704012000",
                        "congestion": 0.00004,
                        "congestionLevel": 1,
                        "type": 1
                    }
                ]
            }
        }
        mock_get.return_value = mock_response

        api = SkCallCongestion()
        response = api.get_api("dummy_url")
        self.assertIsNotNone(response)
        self.assertEqual(response['status']['code'], "00")

    @patch('skapi.callapi.requests.get')
    def test_get_api_failure(self, mock_get):
        # 실패한 API 응답을 모의합니다.
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        api = SkCallCongestion()
        response = api.get_api("dummy_url")
        self.assertIsNone(response)

    @patch('skapi.callapi.SkCallCongestion.get_api')
    def test_areas_get(self, mock_get_api):
        # 성공적인 API 응답을 모의합니다.
        mock_get_api.return_value = {
            "status": {
                "code": "00",
                "message": "success",
                "totalCount": 1
            },
            "contents": {
                "areaname": "Test Area",
                "rltm": {
                    "datetime": "20230704012000",
                    "congestionLevel": 1
                }
            }
        }

        api = SkCallCongestion()
        api.areas_get("dummy_areaid")
        area_info = AreaInfo.objects.get(area_name="Test Area")
        self.assertIsNotNone(area_info)
        self.assertEqual(area_info.congestion_level, "매우혼잡")

    @patch('skapi.callapi.SkCallCongestion.get_api')
    def test_pois_get(self, mock_get_api):
        # 성공적인 API 응답을 모의합니다.
        mock_get_api.return_value = {
            "status": {
                "code": "00",
                "message": "success",
                "totalCount": 1
            },
            "contents": {
                "areaname": "Test Area",
                "rltm": {
                    "datetime": "20230704012000",
                    "congestionLevel": 1
                }
            }
        }

        api = SkCallCongestion()
        api.pois_get("dummy_poiid")
        area_info = AreaInfo.objects.get(area_name="Test Area")
        self.assertIsNotNone(area_info)
        self.assertEqual(area_info.congestion_level, "매우혼잡")


class GetSkHotspotsTestCase(TestCase):
    def setUp(self):
        AreaInfo.objects.create(area_name="Test Area", datetime="2023-11-01T12:00:00", congestion_level="보통")

    def test_get_sk_hotspots(self):
        client = APIClient()
        response = client.get(reverse('get_sk_hotspots'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['area_name'], "Test Area")


