import { useState } from "react";
import api from "../api/api";

export default function ChatInput({ messages, setMessages }) {

    const [question, setQuestion] = useState("");
    const [loading, setLoading] = useState(false);

    async function send() {

        if (!question.trim()) return;

        const userQuestion = question;

        setQuestion("");

        setMessages(prev => [
            ...prev,
            {
                sender: "You",
                text: userQuestion
            }
        ]);

        setLoading(true);

        try {

            const response = await api.post("/chat", {
                question: userQuestion
            });

           setMessages(prev => [
            ...prev,
            {
                sender: "Assistant",
                text: response.data.answer || "No response received.",
                sources: response.data.sources || []
            }]);
        } catch {

            setMessages(prev => [
                ...prev,
                {
                    sender: "Assistant",
                    text: "Unable to contact server."
                }
            ]);

        }

        setLoading(false);

    }

    return (

        <div>

            <input

                value={question}

                onChange={(e) => setQuestion(e.target.value)}

                onKeyDown={(e) => {

                    if (e.key === "Enter") {

                        send();

                    }

                }}

                placeholder="Ask anything..."

                style={{
                    width: "80%",
                    padding: "12px",
                    borderRadius: "6px"
                }}

            />

            <button

                onClick={send}

                disabled={loading}

                style={{
                    marginLeft: "10px",
                    padding: "12px 20px"
                }}

            >

                {loading ? "Thinking..." : "Send"}

            </button>

        </div>

    );

}