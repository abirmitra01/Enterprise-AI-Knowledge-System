import { useEffect, useState } from "react";
import api from "../api/api";

export default function MyDocuments() {

    const [documents, setDocuments] = useState([]);

    useEffect(() => {

        loadDocuments();

    }, []);

    async function loadDocuments() {

        try {

            const token = localStorage.getItem("token");

            const response = await api.get(
                "/documents/my",
                {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                }
            );

            setDocuments(response.data);

        } catch (err) {

            console.log(err);

        }

    }

    async function handleDelete(id) {

        const confirmDelete = window.confirm(
            "Delete this document?"
        );

        if (!confirmDelete) return;

        try {

            const token = localStorage.getItem("token");

            await api.delete(
                `/documents/${id}`,
                {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                }
            );

            setDocuments(prev =>
                prev.filter(doc => doc.id !== id)
            );

        } catch (err) {

            console.log(err);

            alert("Failed to delete document.");

        }

    }

    return (

        <div
            style={{
                marginTop: 30,
                marginBottom: 30
            }}
        >

            <h2>My Uploaded Documents</h2>

            {

                documents.length === 0 ? (

                    <p>No documents uploaded.</p>

                ) : (

                    <ul
                        style={{
                            listStyle: "none",
                            padding: 0
                        }}
                    >

                        {

                            documents.map((doc) => (

                                <li
                                    key={doc.id}
                                    style={{
                                        display: "flex",
                                        justifyContent: "space-between",
                                        alignItems: "center",
                                        marginBottom: "10px",
                                        padding: "10px",
                                        border: "1px solid #ddd",
                                        borderRadius: "6px"
                                    }}
                                >

                                    <span>

                                        📄 {doc.filename}

                                    </span>

                                    <button
                                        onClick={() => handleDelete(doc.id)}
                                        style={{
                                            background: "#ef4444",
                                            color: "white",
                                            border: "none",
                                            padding: "6px 12px",
                                            borderRadius: "6px",
                                            cursor: "pointer"
                                        }}
                                    >

                                        Delete

                                    </button>

                                </li>

                            ))

                        }

                    </ul>

                )

            }

        </div>

    );

}