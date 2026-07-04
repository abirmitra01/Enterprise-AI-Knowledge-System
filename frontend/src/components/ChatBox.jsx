import Message from "./Message";

export default function ChatBox({ messages }) {

    return (

        <div
            style={{
                border: "1px solid #ddd",
                borderRadius: "8px",
                padding: "20px",
                height: "500px",
                overflowY: "auto",
                marginBottom: "20px",
                background: "#fff"
            }}
        >

            {messages.length === 0 ? (

                <p>Start asking questions...</p>

            ) : (

                messages.map((m, index) => (

                    <Message
                        key={index}
                        sender={m.sender}
                        text={m.text}
                        sources={m.sources}
                    />

                ))

            )}

        </div>

    );

}