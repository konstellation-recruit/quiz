import { useState, useContext } from 'react';
import { Text, HStack, VStack } from '@chakra-ui/react';
import { WebSocketContext } from '../provider/WebSocketProvider';
import { useSelector } from 'react-redux';

export default function UserRank() {
    const userScore = useSelector((state) => state.userScore);

    const userArr = Object.entries(userScore);

    return (
        <VStack borderRadius={20} boxShadow="dark-lg" p={10} minH="350px" w="400px" bg="#252d4a">
            <Text>User Score</Text>
            <VStack w="full">
                <Text>
                    {userArr.map((value) => {
                        return (
                            <HStack justify="center">
                                <Text>{value[1].name}</Text>
                                <Text color="red">{value[1].score}</Text>
                            </HStack>
                        );
                    })}{' '}
                </Text>
            </VStack>
        </VStack>
    );
}
