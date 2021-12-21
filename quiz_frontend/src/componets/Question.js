import { Box, Text, VStack, Button, HStack } from '@chakra-ui/react';
import Timer from './TImer';
import { useSelector } from 'react-redux';

export default function Question() {
    const questionId = useSelector((state) => state.questionId);

    return (
        <VStack p={5} boxShadow="dark-lg" borderRadius={20} justify="space-between" w="400px" h="350px" bg="#252d4a">
            <HStack>
                <Text>{questionId}/10</Text>
            </HStack>
            <Text>Lorem ipsum dolor sit amet, consectetur adip</Text>
            <Timer />
        </VStack>
    );
}
