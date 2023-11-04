package com.example.scatter.activity

import android.util.Log
import androidx.activity.ComponentActivity
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.livedata.observeAsState
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.data.api.ApiResponse
import com.example.data.model.Congestion
import com.example.scatter.R

class MainView: ComponentActivity() {

    @Composable
    fun Main(mainViewModel: MainViewModel) {
        val congestionData by mainViewModel.congestionData.observeAsState()

        // MyScaffoldLayout을 사용하여 UI를 구성합니다.
        ScaffoldView().MyScaffoldLayout(viewModel = mainViewModel,onMenuItemClick = { selectedItem ->
            // ViewModel을 통해 API를 호출합니다.
            mainViewModel.getCongestionData(selectedItem.name)

        }) { paddingValues ->
            // 컨텐츠를 구성하는 나머지 부분입니다.
            Content(congestionData, paddingValues)
        }
    }

    @Composable
    fun Content(congestionData: ApiResponse?, paddingValues: PaddingValues) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues),
            verticalArrangement = Arrangement.Top,
            horizontalAlignment = Alignment.Start
        ) {
            // 지도 이미지
            Image(
                painter = painterResource(id = R.drawable.jamsil_map),
                contentDescription = "jamsil_map",
                modifier = Modifier.fillMaxWidth()
            )
            Spacer(modifier = Modifier.height(16.dp))
            // 혼잡도 데이터 텍스트
            congestionData?.let { congestion ->
                Log.d("Selection", "${congestion}")
                Text(
                    text = "지역: ${congestion.areaName}\n" +
                            "혼잡도: ${congestion.congestionLevel}\n" +
                            "날짜: ${congestion.datetime}",
                    style = TextStyle(
                        fontSize = 30.sp,
                        textAlign = TextAlign.Start,
                        fontWeight = FontWeight.Bold
                    ),
                )
            }
        }
    }
}