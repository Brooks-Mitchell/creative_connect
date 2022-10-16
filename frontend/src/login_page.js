import './index.css';

function LoginPage() {
  return (
    <div className="login-page">
      <div className="image-side">
        <p>
          image placeholder
        </p>
       
      </div>
     
     <div className="login-side">
        <body>
          <input placeholder='username'></input>
          <input placeholder='password'></input>
          <p>
            <button>Login</button>
          </p>
          
          <p>
            <button>Join Now</button>
          </p>
        </body>
      </div>
    </div>
  );
}

export default LoginPage;