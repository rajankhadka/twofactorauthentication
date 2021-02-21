import { React,useEffect,useState } from "react";
import { TextField,Button } from "@material-ui/core";
import classes from './RegisterPage.module.css';


const RegisterPage = (props) =>{
    const [username,setUserName] = useState('')
    const [email,setEmail] = useState('')
    const [password,setPassword] = useState('')
    const [rePassword,setRePassword] = useState('')
    const [phoneNumber,setPhoneNumber] = useState('')
    const [data,setData] = useState({})

    
    const submitHandler = (event) =>{
        event.preventDefault()
        const options = {
          headers: {'content-type': 'application/json'}
        };

        
        const datas = {
                username : username,
                email: email,
                password: password,
                phoneNumber: phoneNumber
            };
        fetch('http://127.0.0.1:8000/user/register/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify(datas)
            }).then((response) => response.json())
                .then(data => {
                    console.log(data);
                    props.loginHandler()
                })
                .catch(error => console.log(error))
    }

    let registerPage = null;

    if(props.register){
        registerPage = (
            <div className={classes.registerPage}>
            
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
                    <TextField  label="Email" variant="outlined" 
                      name='email'
                      value={email}
                      onChange={(event) => setEmail(event.target.value)}  
                    />
               </div>
                
                <div>
                    <TextField  label="Password" variant="outlined" 
                        name='password'
                        type="password"
                        value={password}
                        onChange={(event) => setPassword(event.target.value)}  
                    />
                </div>
                
                <div>
                    <TextField  label="Re-Password" variant="outlined" 
                        name='rePassword'
                        value={rePassword}
                        type="password"
                        onChange={(event) => setRePassword(event.target.value)}  
                    />
                </div>

                <div>
                    <TextField  label="phoneNumber" variant="outlined" 
                      name='phoneNumber'
                      value={phoneNumber}
                      onChange={(event) => setPhoneNumber(event.target.value)}  
                    />
               </div>
                
                
                <div>
                    <Button variant="contained" color="primary" type='submit'>
                        Register
                    </Button>
                </div>
            </form>
            <Button color="primary" onClick ={props.loginHandler} >Login</Button>
        </div>
        )
    }
    

    return (
        
        registerPage
    )
    
}

export default RegisterPage