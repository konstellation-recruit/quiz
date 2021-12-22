import React, { useRef } from 'react';
import { useDispatch } from 'react-redux';
import { updateQuestionId, updateImage, updateStatus, updateQuestionData, updateUserScore, updateTrueNumber, updateFalseNumber } from '../actions';

const WebSocketContext = React.createContext(null);
export { WebSocketContext };

export default ({ children }) => {
    let ws = useRef(null);

    const dispatch = useDispatch();

    if (!ws.current) {
        ws.current = new WebSocket(process.env.REACT_APP_WEB_SOCKET_URL);
        ws.current.onopen = () => {
            console.log('connected to ' + 'ws://3.34.190.189:8000/ws/quiz/');
        };
        ws.current.onclose = (error) => {
            console.log('disconnect from ' + 'ws://3.34.190.189:8000/ws/quiz/');
            console.log(error);
        };
        ws.current.onerror = (error) => {
            console.log('connection error ' + 'ws://3.34.190.189:8000/ws/quiz/');
            console.log(error);
        };

        ws.current.onmessage = (event) => {
            const data = JSON.parse(event.data);
            console.log(data);

            if (data.msg_type == 'create_question') {
                dispatch(updateQuestionId(data.q_id));
                dispatch(updateQuestionData(data.question));
                dispatch(updateTrueNumber([0]));
                dispatch(updateFalseNumber([0]));
                dispatch(updateStatus('question'));
                dispatch(updateImage(data.image_url));
            } else if (data.msg_type == 'receive_submit') {
                dispatch(updateTrueNumber([data.count.o]));
                dispatch(updateFalseNumber([data.count.x]));
            } else if (data?.answer_data.msg_type == 'show_answer') {
                dispatch(updateStatus('answer'));
                dispatch(updateQuestionData(data.answer_data.explanation));
                dispatch(updateUserScore(data.cum_scores));
                dispatch(updateTrueNumber(data.answer_data.select_o));
                dispatch(updateFalseNumber(data.answer_data.select_x));
            }
        };
    }

    return <WebSocketContext.Provider value={ws}>{children}</WebSocketContext.Provider>;
};
