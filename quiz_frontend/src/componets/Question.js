import { useState, useContext, useEffect } from 'react';
import { Box, Text, VStack, Button, HStack } from '@chakra-ui/react';
import { useSelector } from 'react-redux';
import { WebSocketContext } from '../provider/WebSocketProvider';
import { useTimer } from 'use-timer';
import { useDispatch } from 'react-redux';
import { updateQuestionId } from '../actions';

export default function Question() {
    const content = useSelector((state) => state.questionData);
    const id = useSelector((state) => state.questionId);
    const status = useSelector((state) => state.status);

    useEffect(() => {
        if (status == 'question') {
            reset();
            start();
        }
    }, [status]);

    const { time, start, pause, reset } = useTimer({
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
