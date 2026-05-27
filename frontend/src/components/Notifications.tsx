import React, { useEffect, useState} from "react";

const Notifications: React.FC = () => {
    const [messages, setMessages] = useState<string[]>([]);

    useEffect(() => {
        const socket: WebSocket = new WebSocket("ws://localhost:8000/ws/notifications/");

        socket.onmessage = (event: MessageEvent) => {
            const data = JSON.parse(event.data);
            setMessages((prev) => [...prev, data.message]);
        };

        socket.onclose = () => {
            console.log("WebSocket closed");
        };

        return () => socket.close();
    }, []);

    return (
        <div>
            <h2>Notifications</h2>
            <ul>
                {messages.map((msg, index) => (
                    <li key={index}>{msg}</li>
                ))}
            </ul>
        </div>
    );
};

export default Notifications;