import { HStack, VStack, Text, Button } from '@chakra-ui/react';
import { useContext } from 'react';
import { WebSocketContext } from '../provider/WebSocketProvider';
import { useSelector } from 'react-redux';

export default function UserStatus() {
    // const ws = useContext(WebSocketContext);

    const userId = useSelector((state) => state.userId);
    const questionId = useSelector((state) => state.questionId);

    const handleClickTrue = async () => {
        fetch(process.env.REACT_APP_REST_API_URL + 'api/v1/select/', {
            method: 'POST',
            body: JSON.stringify({
                user_id: userId,
                question_id: questionId,
                selection: 'o',
            }),
        })
            .then((response) => response.json())
            .then((response) => console.log(response));
    };

    const handleClickFalse = async () => {
        fetch(process.env.REACT_APP_REST_API_URL + 'api/v1/select/', {
            method: 'POST',
            body: JSON.stringify({
                user_id: userId,
                question_id: questionId,
                selection: 'x',
            }),
        })
            .then((response) => response.json())
            .then((response) => console.log(response));
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
