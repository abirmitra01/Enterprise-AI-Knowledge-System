import { useState } from "react";
import api from "../api/api";

export default function FileUpload({ onUploadSuccess }) {

    const [selectedFile, setSelectedFile] = useState(null);
    const [message, setMessage] = useState("");
    const [uploading, setUploading] = useState(false);

    const handleUpload = async () => {

        if (!selectedFile) {
            setMessage("Please select a file.");
            return;
        }

        try {

            setUploading(true);

            const formData = new FormData();
            formData.append("file", selectedFile);

            const token = localStorage.getItem("token");

            const response = await api.post(
                "/documents/upload",
                formData,
                {
                    headers: {
                        Authorization: `Bearer ${token}`,
                        "Content-Type": "multipart/form-data"
                    }
                }
            );

            setMessage(`✅ ${response.data.filename} uploaded successfully.`);

            setSelectedFile(null);

            document.querySelector('input[type="file"]').value = "";

            if (onUploadSuccess) {
                onUploadSuccess();
            }

        } catch (err) {

            console.error("Upload Error:", err);

            if (err.response) {
                setMessage(`❌ ${err.response.data.detail || "Upload failed."}`);
            } else {
                setMessage("❌ Unable to connect to server.");
            }

        } finally {

            setUploading(false);

        }

    };

    return (

        <div
            style={{
                border: "1px solid #ddd",
                padding: "20px",
                borderRadius: "8px",
                marginBottom: "25px"
            }}
        >

            <h2>Upload Knowledge Document</h2>

            <input
                type="file"
                accept=".pdf,.doc,.docx,.ppt,.pptx,.txt"
                onChange={(e) => setSelectedFile(e.target.files[0])}
            />

            <br /><br />

            <button
                onClick={handleUpload}
                disabled={uploading}
            >

                {uploading ? "Uploading..." : "Upload"}

            </button>

            <br /><br />

            <p>{message}</p>

        </div>

    );

}