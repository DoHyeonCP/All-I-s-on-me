package com.example.scatter.activity

sealed class MenuItems(val name: String) {
    object 롯데월드 : MenuItems("잠실역 롯데월드")
    object 방이동_먹자골목 : MenuItems("방이동먹자골목")
    object 에비뉴엘월드타워점 : MenuItems("롯데백화점에비뉴엘월드타워점")
    object 롯데월드몰 : MenuItems("롯데월드몰")
    object 올림픽공원 : MenuItems("올림픽공원")
}