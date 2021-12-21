import React, { useRef } from 'react';

const WebSocketContext = React.createContext(null);
export { WebSocketContext };

export default ({ children }) => {
    let ws = useRef(null);

    if (!ws.current) {
        ws.current = new WebSocket(process.env.REACT_APP_WEB_SOCKET_URL);
        ws.current.onopen = () => {
            console.log('connected to ' + process.env.REACT_APP_WEB_SOCKET_URL);
        };
        ws.current.onclose = (error) => {
            console.log('disconnect from ' + process.env.REACT_APP_WEB_SOCKET_URL);
            console.log(error);
        };
        ws.current.onerror = (error) => {
            console.log('connection error ' + process.env.REACT_APP_WEB_SOCKET_URL);
            console.log(error);
        };
    }

    return <WebSocketContext.Provider value={ws}>{children}</WebSocketContext.Provider>;
};
