import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { login } from "../services/auth";

export default function Login() {

    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleLogin = async (e) => {

        e.preventDefault();

        try {

            const response = await login(username, password);

            localStorage.setItem("token", response.access_token);
            localStorage.setItem("full_name", response.full_name);
            localStorage.setItem("username", response.username);

            navigate("/dashboard");

        } catch (err) {

            console.log(err);

            setError("Invalid username or password");

        }

    };

    return (

        <div
            style={{
                width: "400px",
                margin: "100px auto"
            }}
        >

            <h1>Enterprise AI Assistant</h1>

            <form onSubmit={handleLogin}>

                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    style={{
                        width: "100%",
                        padding: "10px",
                        marginBottom: "15px"
                    }}
                />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    style={{
                        width: "100%",
                        padding: "10px",
                        marginBottom: "15px"
                    }}
                />

                <button
                    style={{
                        width: "100%",
                        padding: "10px"
                    }}
                >
                    Login
                </button>

            </form>

            <p style={{ color: "red" }}>{error}</p>

            <p>
                New Employee?{" "}
                <Link to="/register">
                    Register
                </Link>
            </p>

        </div>

    );

}