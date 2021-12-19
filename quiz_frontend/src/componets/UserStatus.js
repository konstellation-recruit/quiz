import { Box, HStack, VStack, Text, Button } from '@chakra-ui/react';
import { useContext } from 'react';
import { WebSocketContext } from '../WebSocketProvider';

export default function UserStatus() {
    const ws = useContext(WebSocketContext);

    const handleClick = () => {
        ws.current.send(
            JSON.stringify({
                message: 'message',
            })
        );
    };

    return (
        <HStack boxShadow="dark-lg" borderRadius={20} h="350px" w="400px" justify="space-evenly" bg="#252d4a">
            <VStack h="full" p={5} justify="center" spacing={5}>
                <Text as={Button} bg="#252d4a" fontSize="4xl" onClick={handleClick}>
                    O
                </Text>
                <VStack>
                    <Text>6</Text>
                </VStack>
            </VStack>
            <VStack h="full" p={5} justify="center" spacing={5}>
                <Text as={Button} bg="#252d4a" fontSize="4xl">
                    X
                </Text>
                <VStack>
                    <Text>4</Text>
                </VStack>
            </VStack>
        </HStack>
    );
}
