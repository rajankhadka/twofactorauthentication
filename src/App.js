import logo from './logo.svg';

import { useState,useEffect } from "react";
import RegisterPage from './pages/RegisterPage/RegisterPage';
import classes from './App.module.css'
import LoginPage from './pages/LoginPage/LoginPage';


function App() {
  console.log(window.innerHeight)

  const [register,setRegister] = useState(false)

  const registerHandler = () =>{
    setRegister(true)
  }

  const loginHandler = () =>{
    setRegister(false)
  }
  return (
    <div className={classes.App}
      style={{width:window.innerWidth,height:window.innerHeight}}>
      <RegisterPage register={register} loginHandler={loginHandler} />
      <LoginPage registerHandler = {registerHandler} login = {register}/>
    </div>
  );
}

export default App;
