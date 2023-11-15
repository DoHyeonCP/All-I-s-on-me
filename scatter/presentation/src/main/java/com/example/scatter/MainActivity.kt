package com.example.scatter

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material.*
import androidx.compose.ui.Modifier
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.scatter.view.ForecastView
import com.example.scatter.view.MainView
import com.example.scatter.viewmodel.MainViewModel
import dagger.hilt.android.AndroidEntryPoint


@AndroidEntryPoint
class MainActivity: ComponentActivity(){
    private val mainViewModel: MainViewModel by viewModels()


    override fun onCreate(savedInstanceState: Bundle?){
        super.onCreate(savedInstanceState)
        setContent{
            val navController = rememberNavController()

            NavHost(navController = navController, startDestination = "mainScreen"){
                composable("mainScreen"){
                    Column {
                        Surface(
                            modifier = Modifier.fillMaxSize(),

                            ) {
                            MainView().Main(mainViewModel = mainViewModel, navController =  navController)
                        }
                    }
                }
                composable("forecastScreen"){
                    ForecastView().Content(navController = navController)
                }

            }

        }
    }
}