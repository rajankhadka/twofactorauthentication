import { React,useEffect,useState } from "react";
import { TextField,Button } from "@material-ui/core";
import classes from './OTPPage.module.css';
import Home from "../Home";


const OTPPage = (props) =>{
    const [otpcode,setOtpcode] = useState('')
    const [authorized,setAuthorized] = useState(false)
    const submitHandler = (event) =>{
        event.preventDefault()
        const datas = {
                username : props.username,
                otp: parseInt(otpcode),
            };
            console.log(otpcode)
        fetch('http://127.0.0.1:8000/user/otpcode/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify(datas)
            }).then((response) => response.json())
                .then(data => {
                    if(data.msg === 'U R Authorized TO ACCESS'){
                        console.log('UR ')
                        console.log(data)
                        setAuthorized(true)
                    }
                    

                })
                .catch(error => console.log(error))
    }

    

    return (
        <div className={classes.otpPage}>
            {authorized 
                ? <Home />
                : 
                <div>

                    <div>
                <h2>Enter Your OTP Code</h2>
            </div>
            <div>
            <form  onSubmit={submitHandler} >

                <div>
                    <TextField 
                        id="outlined-basic" 
                        name="otpcode"
                        label="otpcode" 
                        variant="outlined" 
                        value={otpcode}  
                        onChange={(event)=> setOtpcode(event.target.value)}
                    />
                </div>
               
                <div>
                    <Button variant="contained" color="primary" type='submit'>
                        Veify
                    </Button>
                </div>
            </form>
                </div>

                </div>
              
            }
       </div>    
    )
    
}

export default OTPPage