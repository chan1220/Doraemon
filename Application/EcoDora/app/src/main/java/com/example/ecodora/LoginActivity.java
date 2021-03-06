package com.example.ecodora;

import android.content.Intent;
import android.os.Bundle;
import android.os.StrictMode;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;
import com.bumptech.glide.request.target.DrawableImageViewTarget;
import com.example.ecodora.utills.DBRequester;
import com.google.android.gms.auth.api.Auth;
import com.google.android.gms.auth.api.signin.GoogleSignInAccount;
import com.google.android.gms.auth.api.signin.GoogleSignInOptions;
import com.google.android.gms.auth.api.signin.GoogleSignInResult;
import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.SignInButton;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.firebase.iid.FirebaseInstanceId;

import org.json.JSONArray;
import org.json.JSONObject;

public class LoginActivity extends AppCompatActivity implements DBRequester.Listener {
    private static final int RESOLVE_CONNECTION_REQUEST_CODE = 1;
    private GoogleApiClient mGoogleApiClient;
    private SignInButton googleLoginButton;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

//        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
//                WindowManager.LayoutParams.FLAG_FULLSCREEN); // 풀스크린 만들기
        getSupportActionBar().hide(); // 엑션 바 감추기

        setContentView(R.layout.activity_login);


        //StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        //StrictMode.setThreadPolicy(policy);

        googleLoginButton = findViewById(R.id.button_login_google);

        GoogleSignInOptions gso = new GoogleSignInOptions.Builder( GoogleSignInOptions.DEFAULT_SIGN_IN )
                .requestEmail( )
                .requestProfile( )
                .build( );

        mGoogleApiClient = new GoogleApiClient.Builder(LoginActivity.this)
                .enableAutoManage( LoginActivity.this, new GoogleApiClient.OnConnectionFailedListener( )
                {
                    @Override
                    public void onConnectionFailed( @NonNull ConnectionResult connectionResult )
                    {
                        // 연결에 실패했을 경우 실행되는 메서드입니다.
                    }
                } ).addApi( Auth.GOOGLE_SIGN_IN_API, gso ).build( );


        Log.w("ParkChan","hehehehehehe");

        googleLoginButton.setOnClickListener( new View.OnClickListener( )
        {
            @Override
            public void onClick(View view )
            { // 구글 로그인 화면을 출력합니다. 화면이 닫힌 후 onActivityResult가 실행됩니다.
                Intent signInIntent = Auth.GoogleSignInApi.getSignInIntent( mGoogleApiClient );
                startActivityForResult( signInIntent, RESOLVE_CONNECTION_REQUEST_CODE );
            }
        } );


        ImageView flash = findViewById(R.id.imageView_flash);

        DrawableImageViewTarget gifImage = new DrawableImageViewTarget(flash);
        Glide.with(this).load(R.drawable.flash).into(gifImage);

    }

    @Override
    protected void onActivityResult( int requestCode, int resultCode, Intent data )
    {
        try {
            switch ( requestCode )
            {
                case RESOLVE_CONNECTION_REQUEST_CODE:
                    GoogleSignInResult result = Auth.GoogleSignInApi.getSignInResultFromIntent(data);
                    if(result.isSuccess() == false)
                        throw new Exception("could not login with google id");

                    GoogleSignInAccount acct = result.getSignInAccount( ); // 계정 정보 얻어오기
                    String id, name, token;
                    name = acct.getDisplayName();
                    id = acct.getId();
                    token = FirebaseInstanceId.getInstance().getToken();


                    Log.w("ParkChan",id);
                    Log.w("ParkChan",name);
                    Log.w("ParkChan",token);
                    // 실행!
                    JSONObject user = new JSONObject();
                    user.put("id", id);
                    user.put("name", name);
                    user.put("token", token);
                    new DBRequester.Builder(this, "http://15.164.149.11:5000", this)
                            .attach("register/user")
                            .streamPost(user)
                            .request("register user");
                    break;

                default:
                    super.onActivityResult( requestCode, resultCode, data );
            }
        } catch (Exception e) {

            Log.d("activity result", e.getMessage());
        }

    }


    @Override
    public void onResponse(String id, JSONObject json, Object... params) {

        try {
            if(json.getBoolean("success") == false)
                return;

            switch(id) {

                case "register user":
                    JSONObject data = json.getJSONObject("data");
                    String uid = data.getString("id");
                    String uname = data.getString("name");
                    String token = data.getString("token");
                    Intent intent=new Intent(LoginActivity.this,MainActivity.class);
                    intent.putExtra("name",uname);
                    intent.putExtra("id",uid);

                    startActivity(intent);
                    finish();
                    break;
            }
        } catch (Exception e) {

            Log.d("on response", e.getMessage());

        }
    }

    @Override
    public void onResponse(String id, JSONArray json, Object... params) {

    }

    @Override
    public void onError(String id, String message, Object... params) {

    }
}



