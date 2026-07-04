import { useNavigate } from "react-router-dom";
import FileUpload from "../components/FileUpload";
import Chat from "./chat";
import MyDocuments from "../components/MyDocuments";

export default function Dashboard() {

    const navigate = useNavigate();

    const fullName = localStorage.getItem("full_name");

    const handleLogout = () => {

        localStorage.removeItem("token");
        localStorage.removeItem("full_name");
        localStorage.removeItem("username");

        navigate("/");

    };

    return (

        <div
            style={{
                width: "80%",
                margin: "30px auto"
            }}
        >

            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center"
                }}
            >

                <h1>Enterprise AI Knowledge Assistant</h1>

                <button
                    onClick={handleLogout}
                    style={{
                        backgroundColor: "#dc3545",
                        color: "white",
                        border: "none",
                        padding: "10px 18px",
                        borderRadius: "6px",
                        cursor: "pointer",
                        fontWeight: "bold"
                    }}
                >
                    Logout
                </button>

            </div>

            <div
                style={{
                    marginBottom: "25px"
                }}
            >

                <h2
                    style={{
                        marginBottom: "5px"
                    }}
                >
                    Hello, {fullName} 
                </h2>

                <p
                    style={{
                        color: "#666",
                        margin: 0
                    }}
                >
                    Welcome to Enterprise AI Knowledge Assistant
                </p>

            </div>

            <FileUpload onUploadSuccess={() => window.location.reload()} />

            <MyDocuments />

            <Chat />

        </div>

    );

}