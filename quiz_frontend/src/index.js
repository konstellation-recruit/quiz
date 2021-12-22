import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import WebSocketProvider from './provider/WebSocketProvider';
import { Provider } from 'react-redux';
import store from './store';

ReactDOM.render(
    <React.StrictMode>
        <Provider store={store}>
            <WebSocketProvider>
                <App />
            </WebSocketProvider>
        </Provider>
    </React.StrictMode>,
    document.getElementById('root')
);
