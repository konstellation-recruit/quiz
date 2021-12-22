import { HStack, VStack, Text, Button } from '@chakra-ui/react';
import { useContext, useState } from 'react';
import { WebSocketContext } from '../provider/WebSocketProvider';
import { useSelector } from 'react-redux';

export default function UserStatus() {
    const [trueContent, setTrueContent] = useState();
    const [falseContent, setFalseContent] = useState();

    const ws = useContext(WebSocketContext);

    // ws.current.onmessage = (event) => {
    //     const data = JSON.parse(event.data);
    //     if (data.msg_type == 'show_answer') {
    //         setTrueContent(data.select_o);
    //         setFalseContent(data.select_x);
    //     }
    // };

    const userId = useSelector((state) => state.userId);
    const userName = useSelector((state) => state.userName);
    const questionId = useSelector((state) => state.questionId);

    const handleClickTrue = async () => {
        ws.current.send(
            JSON.stringify({
                msg_type: 'submit',
                user_id: userId,
                name: userName,
                q_id: questionId,
                select: 'o',
            })
        );
    };

    const handleClickFalse = async () => {
        await ws.current.send(
            JSON.stringify({
                msg_type: 'submit',
                user_id: userId,
                name: 'bar',
                q_id: questionId,
                select: 'x',
            })
        );
    };

    return (
        <HStack boxShadow="dark-lg" borderRadius={20} h="350px" w="400px" justify="space-evenly" bg="#252d4a">
            <VStack h="full" p={5} justify="center" spacing={5}>
                <Button bg="#252d4a" fontSize="4xl" onClick={handleClickTrue}>
                    O
                </Button>
                <VStack>
                    <Text>6</Text>
                </VStack>
            </VStack>
            <VStack h="full" p={5} justify="center" spacing={5}>
                <Button bg="#252d4a" fontSize="4xl" onClick={handleClickFalse}>
                    X
                </Button>
                <VStack>
                    <Text>4</Text>
                </VStack>
            </VStack>
        </HStack>
    );
}
