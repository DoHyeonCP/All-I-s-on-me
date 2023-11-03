//package com.example.data
//
//
//import com.example.data.api.ApiResponse
//import com.example.data.api.ApiService
//import com.example.data.api.ApiServiceManager
//import com.example.data.api.Hotspot
//import org.junit.Before
//import org.junit.Test
//import org.junit.runner.RunWith
//import org.junit.runners.JUnit4
//import org.mockito.Mock
//import org.mockito.Mockito
//import org.mockito.MockitoAnnotations
//import retrofit2.Call
//import retrofit2.Callback
//import retrofit2.Response
//
//@RunWith(JUnit4::class)
//class TestApiServiceManger {
//    @Mock
//    private lateinit var mockApiService: ApiService
//
//    lateinit var apiServiceManager: ApiServiceManager
//
//
//    @Before
//    fun setUp() {
//        MockitoAnnotations.initMocks(this)
//
//        // ApiServiceManager 인스턴스 생성
//        apiServiceManager = ApiServiceManager(mockApiService)
//    }
//
//    @Test
//    fun testCallApi() {
//        mockApiService.getData() //호출에 대한 가짜 응답 생성
//        val mockCall: Call<ApiResponse> = Mockito.mock(Call::class.java  as Class<Call<ApiResponse>>)
//        val apiResponse = ApiResponse(
//            Hotspot("보통", "2023년08월28일 22.40.00"),
//            Hotspot("조금혼잡", "2023년08월28일 22.40.00"),
//            Hotspot("보통", "2023년08월28일 22.40.00"),
//            Hotspot("여유", "2023년08월28일 22.40.00"),
//            Hotspot("여유", "2023년08월28일 22.40.00")
//        )
//
//        Mockito.`when`(mockApiService.getData()).thenReturn(mockCall)
//
//        // 실제 onResponse 콜백이 호출될 때의 동작 정의
//        Mockito.doAnswer { invocation ->
//            val callback: Callback<ApiResponse> = invocation.getArgument(0)
//            callback.onResponse(mockCall, Response.success(apiResponse))
//            null
//        }.`when`(mockCall).enqueue(Mockito.any())
//
//        // callApi 함수 호출
//        apiServiceManager.callApi("방이동먹자골목")
//
//        // 여기에 검증 로직 추가 (예: 데이터가 제대로 저장되었는지 확인)
//    }
//}
//
///* 실제 호출 데이터
//{"롯데월드": {"congestion_level": "보통", "datetime": "2023년08월28일 22.40.00"},
//"방이동먹자골목": {"congestion_level": "조금혼잡", "datetime": "2023년08월28일 22.40.00"},
//"에비뉴엘월드타워점": {"congestion_level": "보통", "datetime": "2023년08월28일 22.40.00"},
// "롯데월드몰": {"congestion_level": "여유", "datetime": "2023년08월28일 22.40.00"},
// "올림픽공원": {"congestion_level": "여유", "datetime": "2023년08월28일 22.40.00"}}
// */