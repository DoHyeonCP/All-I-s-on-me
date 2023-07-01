import android.content.ContentValues.TAG
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.scatter.databinding.ActivitySignupBinding

import com.google.firebase.auth.ktx.auth
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.ktx.firestore
import com.google.firebase.ktx.Firebase

//class SignUpActivity : AppCompatActivity() {
//    private lateinit var binding: ActivitySignupBinding
//    lateinit var db: FirebaseFirestore
//
//    override fun onCreate(savedInstanceState: Bundle?) {
//        super.onCreate(savedInstanceState)
//        binding = ActivitySignupBinding.inflate(layoutInflater)
//        setContentView(binding.root)
//
//        val name = binding.nameEdit.text
//        val email = binding.emailSignUpEdit.text
//        val password = binding.pwSignUpEdit.text
//
//        // cloud firestore 초기화
//        db = Firebase.firestore
//
//        binding.signUpbtn2.setOnClickListener { // 회원가입 버튼 누르면
//            doSignUp(email.toString(), password.toString()) // 회원가입
//            // 유저 이름 받아서
//            val user = hashMapOf (
//                "name" to name.toString()
//            )
//
//            // firestore 에 유저 이름 추가
//            db.collection("users").document(name.toString())
//                .set(user)
//                .addOnSuccessListener { documentReference ->
//                    //Log.d(TAG, "DocumentSnapshot added with ID: ${documentReference.id}")
//                }
//                .addOnFailureListener { e ->
//                    Log.w(TAG, "Error adding document", e)
//                }
//        }
//    }
//
//    private fun doSignUp(userEmail: String, password: String) {
//        // 모든 정보를 입력했을 경우에만 회원가입 가능
//        if (userEmail.isNotEmpty() && userPw.isNotEmpty() && name.isNotEmpty()) {
//            Firebase.auth.createUserWithEmailAndPassword(userEmail, userPw)
//                .addOnCompleteListener(this) {
//                    if (it.isSuccessful) {
//                        Firebase.auth.signInWithEmailAndPassword(userEmail, userPw)
//                            .addOnSuccessListener {
//                                var map = HashMap<String, Any>()
//                                map["image"] = BASIC_IMAGE_URL
//                                map["email"] = userEmail
//                                map["name"] = name
//                                val uid = FirebaseAuth.getInstance().currentUser!!.uid
//                                db.collection("profileImages").document(uid)
//                                    .set(map)
//                            }
//                        startActivity(
//                            Intent(this, SNSActivity::class.java)
//                        )
//                        finish()
//                    } else {
//                        Log.w("LoginActivity", "signUpWithEmail", it.exception)
//                        Toast.makeText(this, "비밀번호는 6자 이상이어야 합니다", Toast.LENGTH_SHORT).show()
//                    }
//                }
//        } else {
//            Toast.makeText(this, "회원 정보를 입력해주세요!", Toast.LENGTH_SHORT).show()
//        }
//    }
//}