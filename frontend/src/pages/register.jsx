import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { register } from "../services/auth";

export default function Register() {

    const navigate = useNavigate();

    const [form,setForm]=useState({

        username:"",
        email:"",
        password:"",
        full_name:""

    });

    const handleSubmit=async(e)=>{

        e.preventDefault();

        await register(form);

        alert("Registration Successful");

        navigate("/");

    };

    return(

        <div
            style={{
                width:"450px",
                margin:"80px auto"
            }}
        >

            <h1>Register</h1>

            <form onSubmit={handleSubmit}>

                <input
                    placeholder="Full Name"
                    onChange={(e)=>setForm({...form,full_name:e.target.value})}
                />

                <br/><br/>

                <input
                    placeholder="Username"
                    onChange={(e)=>setForm({...form,username:e.target.value})}
                />

                <br/><br/>

                <input
                    placeholder="Email"
                    onChange={(e)=>setForm({...form,email:e.target.value})}
                />

                <br/><br/>

                <input
                    type="password"
                    placeholder="Password"
                    onChange={(e)=>setForm({...form,password:e.target.value})}
                />

                <br/><br/>

                <button>

                    Register

                </button>

            </form>

        </div>

    );

}