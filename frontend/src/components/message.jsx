export default function Message({ sender, text, sources }) {

    return (

        <div
            style={{
                marginBottom: "18px",
                padding: "12px",
                borderRadius: "8px",
                backgroundColor:
                    sender === "You"
                        ? "#dbeafe"
                        : "#f3f4f6"
            }}
        >

            <strong>{sender}</strong>

            <div
                style={{
                    marginTop: "6px",
                    whiteSpace: "pre-wrap",
                    lineHeight: "1.6"
                }}
            >
                {text}
            </div>

            {
                sender === "Assistant" &&
                sources &&
                sources.length > 0 && (

                    <div
                        style={{
                            marginTop: "12px",
                            borderTop: "1px solid #ddd",
                            paddingTop: "8px",
                            fontSize: "13px",
                            color: "#555"
                        }}
                    >

                        <strong>Sources</strong>

                        <ul
                            style={{
                                marginTop: "6px",
                                marginBottom: 0,
                                paddingLeft: "20px"
                            }}
                        >

                            {
                                sources.map((source, index) => (

                                    <li key={index}>

                                        📄 {source}

                                    </li>

                                ))
                            }

                        </ul>

                    </div>

                )
            }

        </div>

    );

}