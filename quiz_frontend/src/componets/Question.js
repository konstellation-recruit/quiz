import { useState, useContext } from 'react';
import { Box, Text, VStack, Button, HStack } from '@chakra-ui/react';
import { useSelector } from 'react-redux';
import { WebSocketContext } from '../provider/WebSocketProvider';
import { useTimer } from 'use-timer';
import { useDispatch } from 'react-redux';
import { updateQuestionId } from '../actions';

export default function Question() {
    const ws = useContext(WebSocketContext);

    ws.current.onmessage = (event) => {
        const data = JSON.parse(event.data);
        console.log(data);

        if (data.msg_type == 'create_question') {
            setId(data.q_id);
            setContent(data.question);
            reset();
            dispatch(updateQuestionId(data.q_id));
            start();
        } else if (data.msg_type == 'show_answer') {
            setContent(data.explanation);
            dispatch(updateQuestionId(data.q_id));
        }
    };

    const [content, setContent] = useState();
    const [id, setId] = useState(0);
    const dispatch = useDispatch();

    const { time, start, pause, reset, status } = useTimer({
        initialTime: 15 * 60,
        interval: 10,
        endTime: 0,
        timerType: 'DECREMENTAL',
    });

    const sec = Math.floor(time / 60) < 10 ? '0' + Math.floor(time / 60) : Math.floor(time / 60);
    const msec = time % 60 < 10 ? '0' + (time % 60) : time % 60;

    return (
        <VStack p={5} boxShadow="dark-lg" borderRadius={20} justify="space-between" w="400px" h="350px" bg="#252d4a">
            <HStack>
                <Text>{id}/10</Text>
            </HStack>
            <Text>{content}</Text>
            <HStack>
                <Text>
                    {sec} : {msec}
                </Text>
            </HStack>
        </VStack>
    );
}
