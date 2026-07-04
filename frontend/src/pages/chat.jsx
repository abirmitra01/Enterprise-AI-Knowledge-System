import { useState } from "react";

import ChatBox from "../components/ChatBox";
import ChatInput from "../components/ChatInput";

export default function Chat() {

    const [messages, setMessages] = useState([]);

    return (

        <div
            style={{
                width: "70%",
                margin: "30px auto"
            }}
        >

            <p>
                Ask questions from your uploaded documents.
            </p>

            <ChatBox
                messages={messages}
            />

            <ChatInput
                messages={messages}
                setMessages={setMessages}
            />

        </div>

    );

}