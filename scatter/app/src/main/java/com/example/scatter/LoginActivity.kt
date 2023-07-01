package com.example.scatter

import android.os.Bundle
import android.os.PersistableBundle
import androidx.appcompat.app.AppCompatActivity
import com.example.scatter.databinding.LoginActivityBinding

class LoginActivity : AppCompatActivity() {
    private lateinit var loginActivityBinding: LoginActivityBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        setTheme(R.style.AppTheme)
        super.onCreate(savedInstanceState)
        loginActivityBinding = LoginActivityBinding.inflate(layoutInflater)

        setContentView(loginActivityBinding.root)
    }
}