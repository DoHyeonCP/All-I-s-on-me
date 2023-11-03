package com.example.scatter.activity

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.material.Button
import androidx.compose.material.Icon
import androidx.compose.material.IconButton
import androidx.compose.material.Scaffold
import androidx.compose.material.ScaffoldState
import androidx.compose.material.Text
import androidx.compose.material.TopAppBar
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.Menu
import androidx.compose.material.rememberScaffoldState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.launch

import com.example.scatter.R

class ScaffoldView{
    @Composable
    fun MyScaffoldLayout(
        viewModel: MainViewModel,
        onMenuItemClick: (MenuItems) -> Unit,
        content: @Composable (PaddingValues) -> Unit) {
        val scaffoldState = rememberScaffoldState()
        val coroutineScope = rememberCoroutineScope()

        Scaffold(scaffoldState = scaffoldState,
            topBar = {
                MyTopAppBar {
                    coroutineScope.launch{
                        scaffoldState.drawerState.open()
                    }
                }
            },
            drawerContent = {
                MyNavigationDrawer(
                    coroutineScope = coroutineScope,
                    scaffoldState = scaffoldState,
                    onMenuItemClick = {menuItems ->
                        viewModel.onMenuItemSelected(menuItems.name)
                    }
                ) },){
                paddingValues -> content(paddingValues)
        }
    }

    @Composable
    fun MyTopAppBar(onNaviagionIconClick: () -> Unit) {
        TopAppBar(
            backgroundColor = Color(0xFF10316B),
            contentColor = Color.White,
            elevation = 10.dp
        ) {
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween
            ) {
                // 네비게이션 아이콘
                IconButton(onClick = onNaviagionIconClick) {
                    Icon(
                        imageVector = Icons.Outlined.Menu,
                        contentDescription = "navigation",
                        tint = Color.White, // 안하면 배경색이 같이 바뀜
                        modifier = Modifier.size(60.dp) // 아이콘 크기를 36dp로 키우기
                    )
                }

                // 가운데 로고
                Image(
                    painter = painterResource(id = R.drawable.congestionlogo),
                    contentDescription = "center_image",
                    modifier = Modifier.align(Alignment.CenterVertically)
                )

                // 아이콘과 동일한 크기의 빈 공간을 만들어 로고를 중앙에 유지합니다.
                Spacer(modifier = Modifier.size(60.dp))
            }
        }
    }


    @Composable
    fun MyNavigationDrawer(
        coroutineScope: CoroutineScope,
        scaffoldState: ScaffoldState,
        onMenuItemClick: (MenuItems) -> Unit
    ) {
        val menuItemsList = listOf(
            MenuItems.롯데월드,
            MenuItems.방이동_먹자골목,
            MenuItems.에비뉴엘월드타워점,
            MenuItems.롯데월드몰,
            MenuItems.올림픽공원
        )

        Column(
            modifier = Modifier.fillMaxSize(),
            verticalArrangement = Arrangement.Top,
            horizontalAlignment = Alignment.Start,
        ) {

            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .height(50.dp)
                    .background(Color(0xFF10316B)), // Just for demonstration, you can add your preferred background or image
                contentAlignment = Alignment.TopStart
            ) {
                Row{
                    Text(text = "지역을선택해주세요!", style = TextStyle(fontSize = 24.sp, color = Color.White))
                    Spacer(modifier =  Modifier.width(20.dp))
                    Button(
                        onClick = {
                            coroutineScope.launch {
                                scaffoldState.drawerState.close()
                            }
                        }) {
                        Text(text = "닫기")
                    }
                }

            }
            menuItemsList.forEach { menuItem ->
                Text(
                    text = menuItem.name,
                    style = TextStyle(fontSize = 20.sp, textAlign = TextAlign.Start),
                    modifier = Modifier.clickable{
                        onMenuItemClick(menuItem)
                        coroutineScope.launch {
                            scaffoldState.drawerState.close()
                        }
                    }
                )
                Spacer(modifier = Modifier.height(8.dp))
            }
        }
    }
}


