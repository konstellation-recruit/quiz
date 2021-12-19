import { Button, Text, HStack } from '@chakra-ui/react';
import { useTimer } from 'use-timer';

export default function Timer() {
    const { time, start, pause, reset, status } = useTimer({
        initialTime: 15 * 60,
        interval: 10,
        endTime: 0,
        timerType: 'DECREMENTAL',
    });

    const sec = Math.floor(time / 60) < 10 ? '0' + Math.floor(time / 60) : Math.floor(time / 60);
    const msec = time % 60 < 10 ? '0' + (time % 60) : time % 60;

    return (
        <HStack>
            <Text>
                {sec} : {msec}
            </Text>
            <Button size="xs" color="black" onClick={start}>
                Start
            </Button>
            <Button size="xs" color="black" onClick={reset}>
                Reset
            </Button>
        </HStack>
    );
}
