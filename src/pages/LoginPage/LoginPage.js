import { React,useEffect,useState } from "react";
import { TextField,Button } from "@material-ui/core";
import classes from './LoginPage.module.css';
import OTPPage from "../OTPPage/OTPPage";


const LoginPage = (props) =>{
    const [username,setUserName] = useState('')

    const [password,setPassword] = useState('')

    const [logged,setLogged] = useState(false)


    const submitHandler = (event) =>{
        event.preventDefault()
        const datas = {
                username : username,
                password: password,
            };
        fetch('http://127.0.0.1:8000/user/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify(datas)
            }).then((response) => response.json())
                .then(data => {
                    console.log(data)
                    
                    setLogged(true)
                })
                .catch(error => console.log(error))
    }

    let loginPage = null;

    if(!props.login){
        loginPage = (
            <div className={classes.loginPage}>
            {logged ? <OTPPage username={username} /> :

            <div>
            <form  onSubmit={submitHandler} >
                <div>
                    <TextField 
                        name="username"
                        label="UserName" 
                        variant="outlined" 
                        value={username}  
                        onChange={(event)=> setUserName(event.target.value)}
                    />
                </div>
               
                
                <div>
                    <TextField label="Password" variant="outlined" 
                        name='password'
                        type="password"
                        value={password}
                        onChange={(event) => setPassword(event.target.value)}  
                    />
                </div>
                
                
                
                <div>
                    <Button variant="contained" color="primary" type='submit'>
                        Login
                    </Button>
                </div>
            </form>
            <Button color="primary" onClick = {props.registerHandler}>Register</Button>
            </div>
            }

            
        </div>
        )
    }

    return (
        loginPage
    )
    
}

export default LoginPage